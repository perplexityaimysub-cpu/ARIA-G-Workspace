# -*- coding: utf-8 -*-
import os
import json
import shutil
import sys

# Reconfigure stdout/stderr to utf-8 if available
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

workspace_root = r"C:\Users\Admin\Documents\ARIA-G-Workspace"
json_base_dir = os.path.join(workspace_root, r"بایگانی\مدارک-سیستم\بایگانی اولیه ARIA-G\products")
html_base_dir = os.path.join(workspace_root, r"خروجی\محصول")

# Define products with brand = "متفرقه" and SKU prefix = "999" (General Miscellaneous)
# Folders will be categorized by site categories: "نوشت افزار", "دفتر و کاغذ", "دانش آموزی"

p1 = {
    "name_fa": "مداد بینهایت فانتزی (جادویی) طرح شخصیت‌های کارتونی",
    "product_type": "فیزیکی",
    "main_category": "لوازم تحریر > نوشت‌افزار > مداد و متعلقات",
    "brand": "متفرقه",
    "category_folder": "نوشت افزار",
    "tags": ["مداد بینهایت فانتزی", "مداد جادویی بدون نیاز به تراش", "مداد طرح ابرقهرمانان"],
    "unit": "عدد",
    "sku": "9991401001000",
    "weight": "۱۵",
    "stock_status": "موجود",
    "seo_title": "مداد بینهایت فانتزی (جادویی) طرح ابرقهرمانان بدون نیاز به تراش",
    "slug": "generic-magic-infinite-pencil-cartoon-topper",
    "keywords": "مداد بینهایت فانتزی، مداد جادویی، مداد بدون نیاز به تراش، مداد کاپیتان آمریکا، مداد آیرون من",
    "short_desc": "مداد بینهایت فانتزی با طرح‌های جذاب ابرقهرمانان؛ بدون نیاز به تراشیدن و بدون کثیف شدن دست و کیف دانش‌آموز با غبار گرافیت.",
    "shopfa_type": "ابزارهای نگارش (Writing Instruments)",
    "attributes": [
        {"name": "نوع نوک مداد", "val": "مغزی آلیاژی کربن فشرده"},
        {"name": "عدم نیاز به تراشیدن", "val": "بله (معادل ۱۰۰ مداد معمولی)"},
        {"name": "درجه سختی نوشتار", "val": "معادل سختی H (خاکستری ملایم و تمیز)"},
        {"name": "پاک‌کن داخلی", "val": "دارای پاک‌کن استوانه‌ای مخفی درون بدنه"}
    ],
    "variants": [
        {"type": "طرح شخصیت", "val": "کاپیتان آمریکا", "sku": "9991401001201", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح شخصیت", "val": "آیرون من", "sku": "9991401001202", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح شخصیت", "val": "استیچ", "sku": "9991401001203", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح شخصیت", "val": "بتمن", "sku": "9991401001204", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح شخصیت", "val": "سوپرمن", "sku": "9991401001205", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"}
    ],
    "long_html": """<div style="direction: rtl; font-family: Tahoma, Arial, sans-serif; padding: 25px; border: 1px solid #e2e8f0; border-radius: 12px; background-color: #ffffff; max-width: 800px; margin: auto; line-height: 1.8; color: #334155;">
  <h2 style="color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; font-size: 22px; font-weight: bold; margin-bottom: 15px; text-align: center;">خداحافظی با تراشیدن مداد! مداد بینهایت فانتزی, قهرمان جدید جامدادی شما</h2>
  
  <p>آیا از شکستن مداوم نوک مدادها وسط مشق‌نویسی خسته شده‌اید؟ یا از کثیف شدن دستان و لباس فرزندتان با پودر سیاه گرافیت و تراشه‌های چوب گلایه دارید؟ <strong>مداد بینهایت فانتزی</strong> با طرح‌های جذاب ابرقهرمانان (کاپیتان آمریکا، آیرون من، بتمن و سوپرمن) اینجاست تا نوشتن را برای کودکان به یک بازی شیرین و بدون دردسر تبدیل کند.</p>

  <h3 style="color: #1e293b; font-size: 16px; margin-top: 20px; margin-bottom: 10px; font-weight: bold;">چرا کودکان (و والدین) عاشق این مداد جادویی می‌شوند؟</h3>
  <ul style="margin-right: 20px; margin-bottom: 20px; list-style-type: square; color: #475569;">
    <li><strong>نوشتن بی‌وقفه و روان:</strong> نوک این مداد از ترکیب فشرده کربن و آلیاژ فلز ساخته شده که سایش فوق‌العاده کمی دارد. دیگر نیازی به تراشیدن نیست؛ مداد همیشه آماده نوشتن است!</li>
    <li><strong>جامدادی تمیز و بدون لک:</strong> از آنجا که نوشته‌های این مداد پخش نمی‌شوند، لبه‌ی دستان کودک حین نوشتن روی کاغذ سیاه نخواهد شد.</li>
    <li><strong>عروسک‌های سیلیکونی باکیفیت:</strong> سرمدادی‌های فانتزی از جنس سیلیکون نرم (Soft PVC) با جزئیات بالا ساخته شده‌اند که انگیزه نوشتن را در دانش‌آموزان دوچندان می‌کند.</li>
    <li><strong>پاک‌کن مخفی و جالب:</strong> با باز کردن بدنه مداد، یک پاک‌کن استوانه‌ای باکیفیت ظاهر می‌شود که در بدنه پیچ شده تا گم نشود.</li>
  </ul>

  <div style="margin-top: 25px; padding: 18px; border-right: 4px solid #f59e0b; background-color: #fffbeb; border-radius: 8px;">
    <h4 style="font-weight: bold; color: #b45309; margin-bottom: 10px; font-size: 16px;">💡 راهنمای دوستانه برای یک خرید موفق (مدیریت انتظارات):</h4>
    <p style="margin-bottom: 8px; font-weight: bold; color: #1e293b;">۱. رنگ مغزی این مداد چقدر پررنگ است؟</p>
    <p style="margin-bottom: 15px; margin-right: 10px; color: #475569;">نوک مدادهای بینهایت به دلیل سختی آلیاژ، اثری ملایم و خاکستری‌رنگ شبیه به مدادهای اچ‌بی استاندارد (H/HB) ثبت می‌کند. این رنگ برای مشق‌نویسی تمیز، یادداشت‌برداری روزانه و خط‌کشی عالی است؛ اما برای سیاه‌قلم یا طراحی‌های تیره توصیه نمی‌شود.</p>
    <p style="margin-bottom: 8px; font-weight: bold; color: #1e293b;">۲. آیا این مداد واقعاً هرگز نمی‌شکند؟</p>
    <p style="margin-right: 10px; margin-bottom: 0; color: #475569;">مغزی آلیاژی آن در اثر فشار دست حین نوشتن بسیار مقاوم است و نمی‌شکند؛ اما به دلیل ساختار گرافیتی فشرده، در صورت سقوط مستقیم و زاویه‌دار از ارتفاع زیاد روی سرامیک یا سنگ ممکن است آسیب ببیند. مراقبت از قلم همیشه توصیه می‌شود.</p>
  </div>
</div>"""
}

p2 = {
    "name_fa": "دفترچه یادداشت جیبی ۱/۱۶ جلد سخت ۵۰ برگ سیم از بالا",
    "product_type": "فیزیکی",
    "main_category": "لوازم تحریر > دفاتر و محصولات کاغذی > دفترچه یادداشت",
    "brand": "متفرقه",
    "category_folder": "دفتر و کاغذ",
    "tags": ["دفترچه یادداشت جیبی", "دفترچه یادداشت ۱/۱۶ سیمی", "دفترچه جلد سخت فانتزی"],
    "unit": "عدد",
    "sku": "9996102001000",
    "weight": "۶۰",
    "stock_status": "موجود",
    "seo_title": "دفترچه یادداشت جیبی سایز 1/16 جلد سخت 50 برگ سیمی",
    "slug": "generic-notebook-1-16-hardcover-50-sheets-top-spiral",
    "keywords": "دفترچه یادداشت جیبی، دفترچه یادداشت ۱/۱۶، دفترچه جلد سخت، دفترچه فانتزی سیمی، دفترچه هلو کیتی، دفترچه فروزن",
    "short_desc": "دفترچه یادداشت جیبی فانتزی با جلد سخت صلب؛ مناسب برای ثبت ایده‌ها، لیست خرید و برنامه‌ریزی‌های سریع روزانه در هر زمان و مکان.",
    "shopfa_type": "دفاتر و محصولات کاغذی (Notebooks & Paper Products)",
    "attributes": [
        {"name": "ابعاد دفترچه", "val": "قطع ۱/۱۶ (حدود ۸ × ۱۱.۵ سانتی‌متر)"},
        {"name": "تعداد برگ", "val": "۵۰ برگ"},
        {"name": "نوع جلد", "val": "جلد سخت مقوایی (هاردکاور با لایه سلفون)"},
        {"name": "نوع صحافی", "val": "فنر دوبل فلزی از بالا (ورق‌خوردن راحت ۳۶۰ درجه)"},
        {"name": "کیفیت کاغذ داخلی", "val": "کاغذ تحریر ۷۰ گرمی سفید خط‌دار"}
    ],
    "variants": [
        {"type": "طرح جلد", "val": "فروزن", "sku": "9996102001301", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح جلد", "val": "فضانورد", "sku": "9996102001302", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح جلد", "val": "طرح Love", "sku": "9996102001303", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح جلد", "val": "هلو کیتی", "sku": "9996102001304", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح جلد", "val": "تک شاخ", "sku": "9996102001305", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"}
    ],
    "long_html": """<div style="direction: rtl; font-family: Tahoma, Arial, sans-serif; padding: 25px; border: 1px solid #e2e8f0; border-radius: 12px; background-color: #ffffff; max-width: 800px; margin: auto; line-height: 1.8; color: #334155;">
  <h2 style="color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; font-size: 22px; font-weight: bold; margin-bottom: 15px; text-align: center;">ایده‌های بزرگ، در دفترچه‌های کوچک! همراه همیشگی جیب و کیف شما</h2>
  
  <p>چه در حال حرکت در اتوبوس باشید، چه در کلاس درس یا حتی در حال خرید بازار، بهترین ایده‌ها و لیست کارها ناگهانی به ذهن می‌رسند. <strong>دفترچه یادداشت جیبی ۱/۱۶ سیمی</strong> با ابعاد جمع‌وجور و طراحی‌های فانتزی شاداب، ابزاری سبک و همیشه در دسترس برای ثبت سریع نکته‌های زندگی شماست.</p>

  <h3 style="color: #1e293b; font-size: 16px; margin-top: 20px; margin-bottom: 10px; font-weight: bold;">ویژگی‌هایی که این دفترچه را متمایز می‌کند:</h3>
  <ul style="margin-right: 20px; margin-bottom: 20px; list-style-type: square; color: #475569;">
    <li><strong>جلدی محکم شبیه به تخته‌شاسی:</strong> جلد سخت مقوایی این محصول مقاومت بالایی در برابر تا خوردن درون کیف یا جیب دارد؛ همچنین تکیه‌گاه صلب آن به شما اجازه می‌دهد در حالت ایستاده نیز به راحتی روی صفحات بنویسید.</li>
    <li><strong>فنر دوبل از بالا (ضد گیر کردن):</strong> بر خلاف دفترچه‌های سیمی معمولی که از بغل باز می‌شوند و به لبه جیب گیر می‌کنند، صحافی این دفترچه از بالاست و ورق خوردن کامل ۳۶۰ درجه را ممکن می‌سازد.</li>
    <li><strong>کاغذ ۷۰ گرمی سفید و استاندارد:</strong> صفحات خط‌دار داخلی از کاغذ تحریر سفید استاندارد تهیه شده‌اند تا نوشته‌های شما کاملاً خوانا ثبت شوند.</li>
  </ul>

  <div style="margin-top: 25px; padding: 18px; border-right: 4px solid #3b82f6; background-color: #eff6ff; border-radius: 8px;">
    <h4 style="font-weight: bold; color: #1d4ed8; margin-bottom: 10px; font-size: 16px;">💡 راهنمای دوستانه برای یک خرید موفق (مدیریت انتظارات):</h4>
    <p style="margin-bottom: 8px; font-weight: bold; color: #1e293b;">۱. ابعاد دقیق دفترچه چقدر است؟</p>
    <p style="margin-bottom: 15px; margin-right: 10px; color: #475569;">قطع ۱/۱۶ معادل حدود ۸ در ۱۱.۵ سانتی‌متر است؛ یعنی به راحتی در یک دست یا در جیب جا می‌گیرد. لطفاً قبل از خرید، سایز مینیاتوری آن را در نظر بگیرید.</p>
    <p style="margin-bottom: 8px; font-weight: bold; color: #1e293b;">۲. آیا کاغذ آن برای روان‌نویس‌های خیس مناسب است؟</p>
    <p style="margin-right: 10px; margin-bottom: 0; color: #475569;">کاغذ ۷۰ گرمی این دفترچه برای نوشتن روزانه با خودکار عالی است. اما اگر از روان‌نویس‌های فوق‌العاده خیس، ماژیک‌های رنگ‌آمیزی یا هایلایترها استفاده می‌کنید، ممکن است سایه جوهر در پشت برگه دیده شود که این امر در دفترچه‌های اقتصادی طبیعی است.</p>
  </div>
</div>"""
}

p3 = {
    "name_fa": "جامدادی برزنتی پسرانه طرح T-Rex و فضا",
    "product_type": "فیزیکی",
    "main_category": "لوازم تحریر > کیف و جامدادی > جامدادی",
    "brand": "متفرقه",
    "category_folder": "دانش آموزی",
    "tags": ["جامدادی پسرانه دایناسور", "جامدادی برزنتی زیپ دار", "جامدادی طرح فضایی T-Rex"],
    "unit": "عدد",
    "sku": "9997103001000",
    "weight": "۴۵",
    "stock_status": "موجود",
    "seo_title": "جامدادی برزنتی پسرانه طرح دایناسور T-Rex و فضا زیپ دار",
    "slug": "generic-pencil-case-t-rex-dino-space-washable",
    "keywords": "جامدادی پسرانه، جامدادی دایناسور، جامدادی برزنتی، جامدادی فضا، جامدادی زیپ دار، جامدادی با کیفیت، جامدادی قابل شستشو",
    "short_desc": "جامدادی برزنتی پسرانه جادار با طرح محبوب دایناسور T-Rex و فضا؛ مجهز به آستر داخلی و زیپ استخوانی روان جهت نگهداری از نوشت‌افزارها.",
    "shopfa_type": "کیف و جامدادی (Bags & Pencil Cases)",
    "attributes": [
        {"name": "جنس بدنه اصلی", "val": "پارچه برزنت جودون متراکم"},
        {"name": "طرح گرافیکی چاپ", "val": "دایناسور T-Rex و فضا (پسرانه)"},
        {"name": "مشخصات آستر داخلی", "val": "آستر ضدآب و ضدلک تیره رنگ"},
        {"name": "قابلیت شست‌وشو", "val": "بله (با ماشین لباس‌شویی با آب سرد)"},
        {"name": "نوع زیپ و سرزیپ", "val": "زیپ رزینی دندانه درشت با سرزیپ تمام فلزی"}
    ],
    "variants": [
        {"type": "طرح جامدادی", "val": "طرح فضایی", "sku": "9997103001401", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"},
        {"type": "طرح جامدادی", "val": "طرح دایناسور", "sku": "9997103001402", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"}
    ],
    "long_html": """<div style="direction: rtl; font-family: Tahoma, Arial, sans-serif; padding: 25px; border: 1px solid #e2e8f0; border-radius: 12px; background-color: #ffffff; max-width: 800px; margin: auto; line-height: 1.8; color: #334155;">
  <h2 style="color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; font-size: 22px; font-weight: bold; margin-bottom: 15px; text-align: center;">نگهبان قدرتمند نوشت‌افزارها! جامدادی برزنتی طرح کهکشان و دایناسور</h2>
  
  <p>آیا به دنبال یک جامدادی محکم و جادار هستید که در برابر بازیگوشی‌ها و استفاده روزمره فرزندتان در مدرسه خم به ابرو نیاورد؟ <strong>جامدادی برزنتی طرح T-Rex و فضا</strong> یک محصول جادار و بادوام با طرح‌های پرانرژی است که به راحتی جای خود را در دل پسربچه‌ها باز می‌کند.</p>

  <h3 style="color: #1e293b; font-size: 16px; margin-top: 20px; margin-bottom: 10px; font-weight: bold;">ویژگی‌های مقاومتی و کاربردی جامدادی:</h3>
  <ul style="margin-right: 20px; margin-bottom: 20px; list-style-type: square; color: #475569;">
    <li><strong>پارچه برزنتی مقاوم و بادوام:</strong> این جامدادی از پارچه برزنت جودون ضخیم و باکیفیت ساخته شده تا در برابر مالش، خط‌وخش و پارگی مقاومت بالایی داشته باشد.</li>
    <li><strong>آستر داخلی ضدلک مشکی:</strong> یک لایه آستر تیره مجزا در داخل جامدادی دوخته شده است. اگر نوک مداد یا پودر گرافیتی در جامدادی رها شود، آستر مشکی کثیفی را پنهان کرده و مانع از سرایت لکه به بدنه اصلی می‌شود.</li>
    <li><strong>زیپ دندانه درشت رزینی:</strong> زیپ استخوانی با دندانه‌های درشت رزینی و سرزیپ فلزی روان، باز و بسته کردن مداوم جامدادی را برای کودکان فوق‌العاده راحت و لذت‌بخش می‌کند.</li>
  </ul>

  <div style="margin-top: 25px; padding: 18px; border-right: 4px solid #10b981; background-color: #ecfdf5; border-radius: 8px;">
    <h4 style="font-weight: bold; color: #047857; margin-bottom: 10px; font-size: 16px;">💡 راهنمای دوستانه برای یک خرید موفق (مدیریت انتظارات):</h4>
    <p style="margin-bottom: 8px; font-weight: bold; color: #1e293b;">۱. گنجایش این جامدادی چقدر است؟</p>
    <p style="margin-bottom: 15px; margin-right: 10px; color: #475569;">این جامدادی تک‌خانه است اما دهانه بازی دارد و حدود ۲۵ تا ۳۰ نوشت‌افزار معمولی (خودکار، مداد، خط‌کشی کوتاه و پاک‌کن) را بدون فشار در خود جای می‌دهد.</p>
    <p style="margin-bottom: 8px; font-weight: bold; color: #1e293b;">۲. بهترین روش برای تمیز کردن و شست‌وشو چیست؟</p>
    <p style="margin-right: 10px; margin-bottom: 0; color: #475569;">محصول کاملاً قابل شست‌وشو است. برای حفظ کیفیت رنگ‌های چاپ کهکشانی و طول عمر زیپ فلزی، پیشنهاد می‌شود آن را کاملاً خالی کرده، زیپ آن را ببندید و در آب سرد (۳۰ درجه) با مایع شوینده ملایم بشویید.</p>
  </div>
</div>"""
}

p4 = {
    "name_fa": "مغزی اتود (نوک مداد نوکی) ۲ میلی‌متری قرمز بسته ۶ عددی",
    "product_type": "فیزیکی",
    "main_category": "لوازم تحریر > نوشت‌افزار > مغزی اتود",
    "brand": "متفرقه",
    "category_folder": "نوشت افزار",
    "tags": ["نوک ۲ میل قرمز", "مغزی اتود ۲ میلی متری", "نوک اتود ضخیم قرمز"],
    "unit": "بسته",
    "sku": "9991304001103",
    "weight": "۸",
    "stock_status": "موجود",
    "seo_title": "مغزی مداد نوکی (نوک اتود) 2 میلی متری قرمز بسته 6 تایی",
    "slug": "generic-pencil-lead-2mm-red-6-pack",
    "keywords": "نوک ۲ میل اتود، مغزی اتود ۲ میل قرمز، نوک اتود قرمز، خرید نوک اتود ۲ میل، مغزی اتود ضخیم قرمز",
    "short_desc": "بسته ۶ عددی مغزی اتود ۲ میلی‌متری قرمز پلیمری خط خوانا و بدون شکستگی؛ ایده‌آل برای تصحیح اوراق امتحانی و کادربندی‌های درسی.",
    "shopfa_type": "ابزارهای نگارش (Writing Instruments)",
    "attributes": [
        {"name": "سایز مغزی (ضخامت)", "val": "۲.۰ میلی‌متر"},
        {"name": "رنگ مغزی کالا", "val": "قرمز"},
        {"name": "تعداد در بسته", "val": "۶ عدد مغزی"},
        {"name": "طول هر مغزی کالا", "val": "۹۰ میلی‌متر"},
        {"name": "درجه سختی مغزی", "val": "معادل نرم و پررنگ ۲B"}
    ],
    "variants": [
        {"type": "رنگ مغزی", "val": "قرمز", "sku": "9991304001103", "stock": "تعیین توسط کاربر", "price": "تعیین توسط کاربر"}
    ],
    "long_html": """<div style="direction: rtl; font-family: Tahoma, Arial, sans-serif; padding: 25px; border: 1px solid #e2e8f0; border-radius: 12px; background-color: #ffffff; max-width: 800px; margin: auto; line-height: 1.8; color: #334155;">
  <h2 style="color: #ef4444; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; font-size: 22px; font-weight: bold; margin-bottom: 15px; text-align: center;">روان و بی‌وقفه بنویسید! بسته ۶ تایی مغزی ۲ میلی‌متری قرمز</h2>
  
  <p>هیچ‌چیز آزاردهنده‌تر از این نیست که وسط تصحیح برگه یا کشیدن کادر یک نقشه فنی، نوک اتود به صورت مداوم بشکند. <strong>مغزی اتود ۲ میلی‌متری قرمز</strong> با ضخامت بالای خود، مقاومت فوق‌العاده‌ای در برابر فشارهای ناگهانی دست دارد و تجربه‌ای روان و بدون وقفه را به شما هدیه می‌دهد.</p>

  <h3 style="color: #1e293b; font-size: 16px; margin-top: 20px; margin-bottom: 10px; font-weight: bold;">کاربردها و نکات مثبت نوک پلیمری قرمز:</h3>
  <ul style="margin-right: 20px; margin-bottom: 20px; list-style-type: square; color: #475569;">
    <li><strong>رنگدهی غلیظ و بدون واکس:</strong> این مغزی برخلاف مدل‌های مومی ارزان‌قیمت، رنگ قرمز یکنواخت و خوانایی به شما می‌دهد که در حین مالش دست روی کاغذ پخش نشده و به سادگی پاک می‌شود.</li>
    <li><strong>بسته‌بندی ایمن پلاستیکی:</strong> ۶ عدد مغزی با طول بلند ۹۰ میلی‌متر درون یک غلاف کشویی محکم عرضه می‌شوند تا از شکستن آن‌ها در کیف جلوگیری شود.</li>
    <li><strong>مناسب معلمان و طراحان:</strong> ابزاری ایده‌آل برای تصحیح، علامت‌گذاری متون و ترسیم خطوط راهنما در نقشه‌های مهندسی.</li>
  </ul>

  <div style="margin-top: 25px; padding: 18px; border-right: 4px solid #ef4444; background-color: #fef2f2; border-radius: 8px;">
    <h4 style="font-weight: bold; color: #991b1b; margin-bottom: 10px; font-size: 16px;">💡 راهنمای دوستانه برای یک خرید موفق (مدیریت انتظارات):</h4>
    <p style="margin-bottom: 8px; font-weight: bold; color: #1e293b;">۱. این مغزی روی چه اتودهایی قابل استفاده است؟</p>
    <p style="margin-bottom: 15px; margin-right: 10px; color: #475569;">توجه داشته باشید که به دلیل ضخامت بالای ۲.۰ میلی‌متری، این نوک‌ها فقط درون اتودهای کلاچ ضخیم (۲ میل) یا مداد نوکی‌های مخصوص طراحی قرار می‌گیرند و برای اتودهای ظریف روزمره (مانند ۰.۵ و ۰.۷) مناسب نیستند.</p>
    <p style="margin-bottom: 8px; font-weight: bold; color: #1e293b;">۲. آیا این نوک با پاک‌کن تمیز می‌شود؟</p>
    <p style="margin-right: 10px; margin-bottom: 0; color: #475569;">بله، این مغزی از متریال پلیمری پیشرفته بدون واکس‌های روغنی سنگین ساخته شده که به راحتی با پاک‌کن‌های استاندارد و بدون آسیب به بافت کاغذ یا پخش شدن لکه قرمز رنگ پاک می‌شود.</p>
  </div>
</div>"""
}

test_products = [p1, p2, p3, p4]

# Read the official master HTML template
template_path = os.path.join(workspace_root, r"scratch\product_template.html")
with open(template_path, "r", encoding="utf-8") as f:
    HTML_TEMPLATE = f.read()

# Make directories and compile
for p in test_products:
    slug = p['slug']
    cat_folder = p['category_folder']
    
    # 1. Save JSON Archive in categorized folder
    json_dir = os.path.join(json_base_dir, cat_folder)
    os.makedirs(json_dir, exist_ok=True)
    
    json_path = os.path.join(json_dir, f"{slug}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(p, f, indent=4, ensure_ascii=False)
    
    # Clean old flat or incorrectly placed JSONs if any
    flat_json = os.path.join(json_base_dir, f"{slug}.json")
    if os.path.exists(flat_json):
        try:
            os.remove(flat_json)
        except Exception:
            pass
            
    # 2. Render and Save HTML Dashboard in categorized folder
    html_dir = os.path.join(html_base_dir, cat_folder)
    os.makedirs(html_dir, exist_ok=True)
        
    html_path = os.path.join(html_dir, f"{slug}-product.html")
    
    # Render attributes list HTML
    attr_html_list = []
    for i, attr in enumerate(p['attributes']):
        attr_id = f"attr-val-{i}"
        html_chunk = f"""                <div class="info-item">
                    <span class="info-label">{attr['name']}</span>
                    <div class="info-value-row">
                        <span class="info-value" id="{attr_id}">{attr['val']}</span>
                        <button class="btn-copy-small" onclick="copyTextDirect('{attr_id}')">کپی</button>
                    </div>
                </div>"""
        attr_html_list.append(html_chunk)
    attributes_html = "\n".join(attr_html_list)
    
    # Render variants list HTML
    var_html_list = []
    for var in p['variants']:
        html_chunk = f"""                    <tr>
                        <td>{var['type']}</td>
                        <td>{var['val']}</td>
                        <td><strong style="color: var(--accent-orange);">{var['sku']}</strong></td>
                        <td>{var['stock']}</td>
                        <td>{var['price']}</td>
                    </tr>"""
        var_html_list.append(html_chunk)
    variants_html = "\n".join(var_html_list)
    
    # Render tags as copyable badges
    tag_html_list = []
    for t in p['tags']:
        tag_html_list.append(f'<span class="badge badge-tag" onclick="copyTagDirect(\'{t}\')">{t}</span>')
    tags_html = "\n".join(tag_html_list)
    
    # Populate the template
    long_escaped = p['long_html'].replace('<', '&lt;').replace('>', '&gt;')
    long_html_js = json.dumps(p['long_html'], ensure_ascii=False)
    
    product_dashboard = HTML_TEMPLATE
    product_dashboard = product_dashboard.replace("[NAME_FA]", p['name_fa'])
    product_dashboard = product_dashboard.replace("[PRODUCT_TYPE]", p['product_type'])
    product_dashboard = product_dashboard.replace("[MAIN_CATEGORY]", p['main_category'])
    product_dashboard = product_dashboard.replace("[BRAND]", p['brand'])
    product_dashboard = product_dashboard.replace("[UNIT]", p['unit'])
    product_dashboard = product_dashboard.replace("[SKU]", p['sku'])
    product_dashboard = product_dashboard.replace("[WEIGHT]", p['weight'])
    product_dashboard = product_dashboard.replace("[STOCK_STATUS]", p['stock_status'])
    product_dashboard = product_dashboard.replace("[SEO_TITLE]", p['seo_title'])
    product_dashboard = product_dashboard.replace("[SLUG]", p['slug'])
    product_dashboard = product_dashboard.replace("[KEYWORDS]", ", ".join(p['tags']))
    product_dashboard = product_dashboard.replace("[SHOPFA_TYPE]", p['shopfa_type'])
    product_dashboard = product_dashboard.replace("[ATTRIBUTES_HTML]", attributes_html)
    product_dashboard = product_dashboard.replace("[TAGS_HTML]", tags_html)
    product_dashboard = product_dashboard.replace("[VARIANTS_HTML]", variants_html)
    product_dashboard = product_dashboard.replace("[SHORT_DESC]", p['short_desc'])
    product_dashboard = product_dashboard.replace("[LONG_HTML_ESCAPED]", long_escaped)
    product_dashboard = product_dashboard.replace("[LONG_HTML_JS]", long_html_js)
    
    with open(html_path, 'w', encoding='utf-8') as fh:
        fh.write(product_dashboard)

print("SUCCESS")
