import os
import re
import sys
import zipfile
import threading
import time
from pathlib import Path
from flask import Flask, request, jsonify, send_file, render_template_string
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')

# Global state for folder processing
process_lock = threading.Lock()
state = {
    "running": False,
    "current_file": "",
    "processed_count": 0,
    "total_files": 0,
    "total_original_size": 0,
    "total_optimized_size": 0,
    "logs": [],
    "stop_requested": False,
    "completed": False,
    "error": None
}

SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif'}

def log_message(msg):
    timestamp = time.strftime("%H:%M:%S")
    state["logs"].append(f"[{timestamp}] {msg}")
    print(f"[{timestamp}] {msg}")

def sanitize_filename(filename, style='original'):
    """
    Sanitize filename for SEO and web standards.
    """
    name, ext = os.path.splitext(filename)
    if style in ('clean', 'parent_folder'):
        # Replace spaces and underscores with dashes
        name = name.replace(' ', '-').replace('_', '-')
        # Remove non-alphanumeric characters (except Persian chars, letters, numbers, and dashes)
        # Persian characters range: \u0600-\u06FF
        name = re.sub(r'[^\w\-\u0600-\u06FF]', '', name)
        # Replace multiple consecutive dashes with a single dash
        name = re.sub(r'-+', '-', name)
        # Trim dashes from ends
        name = name.strip('-')
        # Convert English letters to lowercase
        name = name.lower()
    return name

def select_directory_gui(title="انتخاب پوشه"):
    """
    Opens a native Windows folder selection dialog.
    Runs in a separate thread to prevent blocking.
    """
    result = []
    def ask():
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            path = filedialog.askdirectory(parent=root, title=title)
            result.append(path)
            root.destroy()
        except Exception as e:
            print(f"Error in Tkinter: {e}")
            result.append("")
    
    t = threading.Thread(target=ask)
    t.start()
    t.join()
    return result[0] if result else ""

def optimize_image(input_path, output_path, format_ext, quality=80, max_width=None, max_height=None):
    """
    Optimizes a single image, resizes it if needed, and saves it.
    """
    img = Image.open(input_path)
    
    # Handle transparency when converting to JPEG
    if format_ext.upper() == 'JPEG' and img.mode in ('RGBA', 'LA', 'P'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        # If image has alpha channel, paste it on the background
        if img.mode == 'RGBA':
            background.paste(img, mask=img.split()[3])
        elif img.mode == 'LA':
            background.paste(img, mask=img.split()[1])
        else:
            background.paste(img.convert('RGBA'), mask=img.convert('RGBA').split()[3])
        img = background
    elif img.mode not in ('RGB', 'RGBA') and format_ext.upper() == 'WEBP':
        # WebP supports RGB and RGBA
        img = img.convert('RGBA' if 'transparency' in img.info or img.mode == 'P' else 'RGB')

    # Resize if needed while maintaining aspect ratio
    width, height = img.size
    if max_width or max_height:
        ratio = 1.0
        if max_width and width > max_width:
            ratio = min(ratio, max_width / width)
        if max_height and height > max_height:
            ratio = min(ratio, max_height / height)
            
        if ratio < 1.0:
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
    # Save optimized image
    save_args = {'quality': quality}
    if format_ext.upper() == 'JPEG':
        save_args['optimize'] = True
    elif format_ext.upper() == 'PNG':
        # PNG is lossless, quality is not applicable but optimization is
        save_args['optimize'] = True
        del save_args['quality']
    elif format_ext.upper() == 'WEBP':
        save_args['method'] = 6  # Highest compression method
        
    img.save(output_path, format=format_ext.upper(), **save_args)
    return os.path.getsize(output_path)

def folder_processor_thread(input_dir, output_dir, format_ext, quality, max_width, max_height, naming_style):
    """
    Crawls directories, recreates folders, and processes images.
    """
    global state
    try:
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        
        # 1. Scan for all files
        image_files = []
        for root_dir, _, files in os.walk(input_dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in SUPPORTED_EXTENSIONS:
                    image_files.append(Path(root_dir) / file)
                    
        state["total_files"] = len(image_files)
        state["processed_count"] = 0
        state["total_original_size"] = 0
        state["total_optimized_size"] = 0
        
        log_message(f"شروع پردازش پوشه. تعداد کل تصاویر یافت شده: {len(image_files)}")
        
        # Keep track of file counters per folder to support parent folder naming
        folder_counters = {}
        
        for file_path in image_files:
            if state["stop_requested"]:
                log_message("پردازش توسط کاربر متوقف شد.")
                break
                
            # Update state
            rel_path = file_path.relative_to(input_path)
            state["current_file"] = str(rel_path)
            
            # Recreate folder structure in output path
            dest_dir = output_path / rel_path.parent
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            # Determine naming
            if naming_style == 'parent_folder':
                parent_name = file_path.parent.name
                # If root input dir has no name, fallback
                if parent_name == input_path.name or not parent_name:
                    parent_name = "product"
                clean_parent = sanitize_filename(parent_name, style='clean')
                if not clean_parent:
                    clean_parent = "product"
                    
                counter = folder_counters.get(parent_name, 1)
                new_name = f"{clean_parent}-{counter}"
                folder_counters[parent_name] = counter + 1
            else:
                new_name = sanitize_filename(file_path.name, style=naming_style)
                
            dest_file = dest_dir / f"{new_name}.{format_ext.lower()}"
            
            # Process
            orig_size = os.path.getsize(file_path)
            state["total_original_size"] += orig_size
            
            try:
                opt_size = optimize_image(
                    input_path=file_path,
                    output_path=dest_file,
                    format_ext=format_ext,
                    quality=quality,
                    max_width=max_width,
                    max_height=max_height
                )
                state["total_optimized_size"] += opt_size
                
                reduction = ((orig_size - opt_size) / orig_size) * 100 if orig_size > 0 else 0
                log_message(f"موفق: {rel_path} -> کاهش حجم: {reduction:.1f}% ({orig_size/1024:.1f} KB -> {opt_size/1024:.1f} KB)")
            except Exception as e:
                log_message(f"خطا در پردازش {rel_path}: {str(e)}")
            
            state["processed_count"] += 1
            
        state["completed"] = True
        log_message("پردازش پوشه با موفقیت به پایان رسید.")
        
    except Exception as e:
        state["error"] = str(e)
        log_message(f"خطای کلی در پردازش پوشه: {str(e)}")
    finally:
        state["running"] = False

# Flask Routes
@app.route('/')
def index():
    try:
        return send_file(os.path.join('templates', 'index.html'))
    except Exception as e:
        return f"خطا در بارگذاری قالب: {str(e)}"

@app.route('/api/select-folder', methods=['POST'])
def select_folder():
    data = request.json or {}
    title = data.get('title', 'انتخاب پوشه')
    folder_path = select_directory_gui(title)
    return jsonify({"path": folder_path})

@app.route('/api/start-folder', methods=['POST'])
def start_folder_process():
    global state
    with process_lock:
        if state["running"]:
            return jsonify({"error": "یک فرآیند دیگر در حال اجرا است."}), 400
            
        data = request.json or {}
        input_dir = data.get('input_folder')
        output_dir = data.get('output_folder')
        format_ext = data.get('format', 'webp').lower()
        quality = int(data.get('quality', 80))
        max_width = data.get('max_width')
        max_height = data.get('max_height')
        naming_style = data.get('naming_style', 'original')
        
        # Parse max width/height
        max_width = int(max_width) if max_width else None
        max_height = int(max_height) if max_height else None
        
        if not input_dir or not os.path.exists(input_dir):
            return jsonify({"error": "پوشه ورودی نامعتبر است."}), 400
        if not output_dir:
            return jsonify({"error": "پوشه خروجی مشخص نشده است."}), 400
            
        # Reset state
        state = {
            "running": True,
            "current_file": "",
            "processed_count": 0,
            "total_files": 0,
            "total_original_size": 0,
            "total_optimized_size": 0,
            "logs": [],
            "stop_requested": False,
            "completed": False,
            "error": None
        }
        
        # Start thread
        t = threading.Thread(
            target=folder_processor_thread,
            args=(input_dir, output_dir, format_ext, quality, max_width, max_height, naming_style)
        )
        t.start()
        
        return jsonify({"status": "started"})

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify(state)

@app.route('/api/stop-folder', methods=['POST'])
def stop_folder_process():
    global state
    state["stop_requested"] = True
    log_message("درخواست توقف پردازش ارسال شد...")
    return jsonify({"status": "stopping"})

@app.route('/api/process-files', methods=['POST'])
def process_uploaded_files():
    if 'files' not in request.files:
        return jsonify({"error": "فایلی ارسال نشده است."}), 400
        
    uploaded_files = request.files.getlist('files')
    format_ext = request.form.get('format', 'webp').lower()
    quality = int(request.form.get('quality', 80))
    
    max_width = request.form.get('max_width')
    max_height = request.form.get('max_height')
    max_width = int(max_width) if max_width else None
    max_height = int(max_height) if max_height else None
    
    naming_style = request.form.get('naming_style', 'original')
    
    if not uploaded_files or uploaded_files[0].filename == '':
        return jsonify({"error": "هیچ فایلی انتخاب نشده است."}), 400
        
    temp_dir = Path("temp_processing")
    temp_dir.mkdir(exist_ok=True)
    
    processed_paths = []
    
    try:
        # For batch uploads, parent_folder naming defaults to prefix "product"
        counter = 1
        for file in uploaded_files:
            ext = os.path.splitext(file.filename)[1].lower()
            if ext not in SUPPORTED_EXTENSIONS:
                continue
                
            input_path = temp_dir / file.filename
            file.save(input_path)
            
            if naming_style == 'parent_folder':
                new_name = f"product-{counter}"
                counter += 1
            else:
                new_name = sanitize_filename(file.filename, style=naming_style)
                
            output_filename = f"{new_name}.{format_ext}"
            output_path = temp_dir / f"opt_{output_filename}"
            
            optimize_image(
                input_path=input_path,
                output_path=output_path,
                format_ext=format_ext,
                quality=quality,
                max_width=max_width,
                max_height=max_height
            )
            
            processed_paths.append((output_path, output_filename))
            if os.path.exists(input_path):
                os.remove(input_path)
                
        if not processed_paths:
            return jsonify({"error": "هیچ تصویر معتبری برای پردازش یافت نشد."}), 400
            
        if len(processed_paths) == 1:
            file_path, filename = processed_paths[0]
            response = send_file(
                file_path,
                mimetype=f'image/{format_ext}',
                as_attachment=True,
                download_name=filename
            )
            
            def delay_delete(path):
                time.sleep(2)
                try:
                    if os.path.exists(path):
                        os.remove(path)
                except Exception:
                    pass
            threading.Thread(target=delay_delete, args=(file_path,)).start()
            
            return response
        else:
            zip_filename = f"optimized_images_{int(time.time())}.zip"
            zip_path = temp_dir / zip_filename
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file_path, filename in processed_paths:
                    zipf.write(file_path, arcname=filename)
                    try:
                        os.remove(file_path)
                    except Exception:
                        pass
            
            response = send_file(
                zip_path,
                mimetype='application/zip',
                as_attachment=True,
                download_name=zip_filename
            )
            
            def delay_delete(path):
                time.sleep(2)
                try:
                    if os.path.exists(path):
                        os.remove(path)
                except Exception:
                    pass
            threading.Thread(target=delay_delete, args=(zip_path,)).start()
            
            return response
            
    except Exception as e:
        return jsonify({"error": f"خطا در پردازش فایل‌ها: {str(e)}"}), 500

if __name__ == '__main__':
    if os.path.exists("temp_processing"):
        for f in os.listdir("temp_processing"):
            try:
                os.remove(os.path.join("temp_processing", f))
            except Exception:
                pass
                
    port = 5000
    
    # Auto-open default browser after 1.5 seconds delay
    import webbrowser
    def open_browser():
        time.sleep(1.5)
        try:
            webbrowser.open(f"http://127.0.0.1:{port}")
        except Exception as e:
            print(f"Failed to open browser: {e}")
            
    threading.Thread(target=open_browser, daemon=True).start()
    
    print(f"Starting server on http://localhost:{port}")
    app.run(host='127.0.0.1', port=port, debug=False)
