# **معماری پایگاه داده و مهندسی تجربه کاربری فیلترینگ تکامل‌پذیر در کاتالوگ‌های نوشت‌افزار مقیاس‌بزرگ**

گسترش کاتالوگ محصولات در پلتفرم‌های تجارت الکترونیک، به‌ویژه در صنف نوشت‌افزار که با تنوع گستردگی ویژگی‌های ساختاری و نوسانات مداوم کالاها مواجه است، نیازمند تلفیق معماری پایگاه داده و طراحی رابط کاربری تعاملی است1. چالش اساسی در توسعه سیستم‌های فیلترینگ مقیاس‌بزرگ، برقراری توازن میان انعطاف‌پذیری کاتالوگ در پذیرش مشخصات فنی جدید و بهینه‌سازی مسیر خرید برای جلوگیری از فرسودگی اسکرول (Scroll Fatigue) است1. این گزارش پژوهشی با تحلیل عمیق الگوهای فیلترینگ رقبای پیشرو مانند دیجی‌کالا و تبیین مدل‌های داده‌ای پیشرفته نظیر PostgreSQL JSONB و مدل‌های رابطه‌ای سخت، فرمول‌بندی جامعی را جهت استقرار کاتالوگ پویای برند سی‌کلاس (C-Class) ارائه می‌دهد4.

## **سیستم ارث‌بری ویژگی‌ها و مدیریت فرسودگی اسکرول**

در ساختار کاتالوگ محصولات نوشت‌افزار، تفاوت‌های عمیقی میان ابزارهای عمومی و تخصصی وجود دارد4. عدم مدیریت صحیح این تفاوت‌ها در قالب یک سیستم ارث‌بری ویژگی‌ها (Attribute Inheritance) منسجم، به شلوغی بیش از حد سایدبار فیلترینگ و سردرگمی کاربر می‌انجامد3.

### **تحلیل تمایز فیلترها: مداد طراحی تخصصی در برابر مداد معمولی**

بررسی کاتالوگ رقبای اصلی نظیر دیجی‌کالا نشان می‌دهد که یک مداد معمولی تنها با ویژگی‌های پایه‌ای مانند برند، رنگ، فرم سطح مقطع (گرد، مثلث، شش‌ضلعی) و تعداد موجود در بسته دسته‌بندی می‌شود4. در مقابل، برای یک «مداد طراحی تخصصی»، فیلترها باید پارامترهای فیزیکی و شیمیایی پیشرفته‌تری را پوشش دهند تا پاسخگوی نیاز طراحان حرفه‌ای باشند11:

* **درجه سختی نوک (Lead Hardness):** مغزی مدادهای طراحی از طیف بسیار سخت ![][image1] تا بسیار نرم و سیاه ![][image2] گریدبندی می‌شوند که مدهای متداول ![][image3] و ![][image4] در میانه این گستره قرار دارند11.  
* **ضخامت و قطر مغزی (Core Diameter):** بر خلاف مدادهای سنتی، مدادهای حرفه‌ای با قطر نوشتاری متفاوت (نظیر مدادهای طراحی ضخیم یا شمش‌های گرافیتی با قطرهای ۷ تا ۱۰ میلی‌متر) فیلتر می‌شوند11.  
* **جنس و فرمولاسیون مغزی (Core Material):** تمایز میان گرافیت خالص چسبیده به چوب، مغزی زغالی (Charcoal)، مداد کنته پاریس و شمش‌های گرافیتی بدون غلاف12.  
* **ساختار بدنه و ارگونومی تخصصی:** فرم سطح مقطع سه‌گوش ارگونومیک که انگشتان را به صورت طبیعی هدایت کرده و مانع از بروز مشکلات عضلانی یا خستگی دست می‌شود در مقایسه با فرم شش‌ضلعی سنتی مدادهای مهندسی10.  
* **فناوری اتصال ایمن مغزی (SV Bonding):** اتصال نوک کاملاً به بدنه چوبی که مقاومت فوق‌العاده‌ای در برابر شکستگی حین کار و تراشیدن ایجاد می‌کند11.  
* **جنس جعبه و نوع بسته‌بندی:** فیلترهای تفکیک‌کننده میان جعبه‌های چوبی حرفه‌ای، جعبه‌های فلزی مستحکم و جعبه‌های مقوایی هنرجویی4.

### **مدیریت فرسودگی اسکرول (Scroll Fatigue) در لایه رابط کاربری**

ترکیب فیلترهای عمومی با ویژگی‌های فوق‌تخصصی در صورت عدم مهار، سایدبار فیلتر را به طوماری طولانی تبدیل کرده و باعث ریزش سریع کاربران موبایل می‌شود2. رقبای پیشرو برای حل این چالش از رویکردهای مهندسی زیر استفاده می‌کنند:

1. **افشای تدریجی بر پایه کوئری (Progressive Disclosure by Query):** فیلترهای فوق‌تخصصی نظیر "درجه سختی مغزی" یا "ضخامت نوک" به صورت پیش‌فرض در صفحات بالادستی کاتالوگ پنهان هستند14. این فیلترها تنها زمانی فعال شده و در ساختار سایدبار پدیدار می‌شوند که کاربر دسته‌بندی را به سطح انتهایی (نظیر /category-mechanical-pencils/) محدود کرده یا کلیدواژه تخصصی را جستجو کند15.  
2. **جدا کردن فیلترینگ از رفرش آنی صفحه (Decoupled Filtering):** اعمال مستقیم فیلتر و بارگذاری مجدد نتایج پس از هر کلیک، منجر به پرش‌های مکرر صفحه و خستگی بصری می‌شود3. راه‌حل بهینه، اجازه انتخاب چندگانه به کاربر و استفاده از دکمه تعاملی اعمال فیلتر ("نمایش X کالا") است که به صورت لحظه‌ای تعداد نتایج مطابق فیلترها را بدون لود مجدد صفحه نشان می‌دهد16.  
3. **طراحی موبایل‌محور مبتنی بر دراور پایین‌صفحه (Mobile Bottom-Sheet):** فیلترها در نسخه موبایل در اورلی تمام‌صفحه یا دراورهایی با اهداف لمسی بزرگ (حداقل ![][image5] pt) قرار می‌گیرند16. دکمه فیلتر به صورت چسبنده (Sticky) در پایین صفحه شناور می‌ماند تا کاربر در هر عمقی از اسکرول به آن دسترسی داشته باشد17.

## **مکانیزم فیلترینگ متغیرهای بازه‌ای، اوزان و ابعاد در نوشت‌افزار**

کنترل ابعاد فیزیکی و طیف‌های رنگی گسترده در صنف نوشت‌افزار نیازمند پیاده‌سازی مکانیزم‌های نمایش متفاوتی در سایدبار است19.

### **مدیریت وزن چسب‌های ماتیکی: چک‌باکس تکی یا بازه گروهی؟**

بررسی سبد محصولات برندهای پیشرو نظیر اوهو، کنکو، پنتر، اینوکس، ماین و سی‌کلاس نشان می‌دهد که اوزان چسب‌های ماتیکی در صنعت به صورت کاملاً استاندارد و گسسته تولید می‌شوند5:  
![][image6]  
\[cite: 5, 19, 22, 23, 24, 25\]  
در این سناریو، رقبای بزرگ از **چک‌باکس‌های تکی عددی دقیق** به جای اسلایدرهای بازه‌ای یا بازه‌های گروهی (مانند ۵ تا ۱۵ گرم) استفاده می‌کنند5. دلایل ارجحیت این الگوی رابط کاربری عبارتند از:

* **ثبات و تراکم پایین داده‌ها (Low Cardinality):** تعداد کل گزینه‌های وزنی استاندارد کمتر از ۸ مورد است؛ بنابراین نمایش چک‌باکس‌های گسسته فضای بسیار کمی اشغال کرده و نیازی به تعریف بازه‌های مبهم ندارد5.  
* **دقت در خرید کاربردی:** در خرید نوشت‌افزار مدارس یا اداری، کاربران وزن دقیق کالا را بر اساس ارگونومی و میزان مصرف انتخاب می‌کنند (مثلاً انتخاب دقیق چسب ۸ گرمی برای کودکان دبستانی)5.  
* **ترکیب با متغیر تعداد:** اوزان چسب ماتیکی اغلب با بسته‌بندی‌های چندعددی (مانند بسته‌های ۳ عددی، ۱۲ عددی یا جعبه‌های ۲۴ تایی) ترکیب می‌شوند5. از این رو، تعبیه یک فیلتر مجزا برای "تعداد در بسته" در کنار چک‌باکس‌های وزن دقیق بسیار اثربخش‌تر است5.

### **راه‌حل‌های جلوگیری از شلوغی سایدبار در فیلتر تنوع رنگی بالا (ماژیک نقاشی)**

ماژیک‌های نقاشی و ابزارهای رنگ‌آمیزی با تنوع رنگی بسیار بالا (از پکیج‌های ۶ رنگ تا جعبه‌های ۱۰۰ رنگ تخصصی) چالش جدی شلوغی سایدبار را ایجاد می‌کنند21. برای رفع این موضوع، رقبای موفق از معماری سه‌لایه‌ای زیر برای فیلتر رنگ بهره می‌برند:

1. **دسته‌بندی پالت‌های موضوعی (Theme/Spectrum Classification):** به جای لیست کردن ده‌ها طیف رنگی، کالاها بر اساس تم کاربردی فیلتر می‌شوند؛ نظیر تم رنگ‌های پاستلی (Pastel)، نئونی (Neon)، طیف پوست برای کارهای پرتره و راندو (Skin Tones)، رنگ‌های متالیک (Metallic) و اکلیلی20.  
2. **فیلتر بسته‌بندی‌های استاندارد (Pack Size Buckets):** فیلترینگ بر اساس بازه‌های پرتقاضا انجام می‌شود: بسته‌های کمتر از ۱۲ رنگ، ۱۲ تا ۲۴ رنگ، ۲۴ تا ۵۰ رنگ و پکیج‌های تخصصی حرفه‌ای بیش از ۵۰ تا ۱۰۰ رنگ20.  
3. **تراشه‌های تصویری با افشای محدود (Visual Color Swatches with Show More):** رنگ‌های پرکاربرد (مانند قرمز، آبی، سبز، زرد و مشکی) به صورت دایره‌های رنگی کوچک با ارتفاع و پهنای مناسب در سایدبار نمایش داده می‌شوند و بقیه رنگ‌ها تحت دکمه تعاملی "مشاهده بیشتر" پنهان می‌شوند تا تعادل بصری سایدبار حفظ گردد9.

## **تحلیل فنی دیتابیس: مدل‌های رابطه‌ای، EAV و PostgreSQL JSONB**

پیاده‌سازی فیلترهای پویا و تکامل‌پذیر برای صنف نوشت‌افزار، چالش بزرگی در طراحی پایگاه داده ایجاد می‌کند1. انتخاب نوع معماری ذخیره‌سازی، تأثیر مستقیمی بر کارایی سیستم در زمان افزایش حجم داده‌ها دارد1.

### **مدل موجودیت-ویژگی-مقدار (EAV) و چالش انفجار پیوندها (Join Explosion)**

در مدل سنتی EAV، هر صفت کالا به صورت رکوردی مجزا در جدولی شامل سه ستون entity\_id و attribute\_id و value ذخیره می‌شود1. اگر کاربر بخواهد مداد طراحی را با چند ویژگی ترکیبی فیلتر کند (به عنوان مثال: سختی مغزی ![][image7]، ساختار بدنه شش‌ضلعی و بسته‌بندی جعبه فلزی)11، پایگاه داده ناگزیر است به تعداد ویژگی‌های انتخاب شده عملیات اتصال (JOIN) یا کوئری‌های تودرتوی EXISTS را بر روی جدول بزرگ ویژگی‌ها اجرا کند28.  
با افزایش تعداد فیلترها (![][image8])، سیستم دچار افت شدید سرعت و قفل شدن منابع پردازشی دیتابیس (CPU) می‌شود28:  
![][image9]  
\[cite: 28\]  
به همین دلیل، استفاده از مدل EAV برای کاتالوگ‌های مقیاس‌بزرگ با فیلترهای همزمان توصیه نمی‌شود1.

### **مدل پویا و سندمحور PostgreSQL JSONB و مزایای آن**

پایگاه داده PostgreSQL با ارائه تایپ داده‌ای JSONB بستری مناسب برای پیاده‌سازی ساختارهای پویا و بی‌نیاز از طرحواره صلب ایجاد کرده است7. داده‌ها در قالب فرمت باینری تجزیه‌شده ذخیره می‌شوند و نیاز به پردازش مداوم در زمان اجرای کوئری را برطرف می‌کنند7.

* **اعتبارسنجی در سطح دیتابیس (Schema Validation):** با استفاده از محدودیت‌های کنترلی (CHECK Constraints) و توابع سیستمی نظیر jsonb\_typeof یا IS JSON OBJECT می‌توان یکپارچگی داده‌ها را در سطح پایگاه داده بدون واگذاری کامل به اپلیکیشن کنترل کرد7.  
* **پشتیبانی از انواع داده‌های توکار:** امکان ذخیره‌سازی آرایه‌های چندمقادیری و دسترسی سریع به اشیاء تودرتو بدون نیاز به جداول رابطه‌ای واسط28.

### **چالش ذخیره‌سازی خارج از صفحه (TOAST Table Hazard)**

یکی از نقایص پنهان در استفاده از ستون‌های بزرگ JSONB در سیستم‌های مقیاس‌بزرگ، معماری ذخیره‌سازی خارج از صفحه در PostgreSQL است31. طبق این سازوکار، اسناد جی‌سان بزرگی که حجم آن‌ها پس از فشرده‌سازی از مرز ۲ کیلوبایت فراتر برود، به جدول جانبی به نام TOAST منتقل شده و در صفحات ۸ کیلوبایتی خرد می‌شوند31. در زمان اعمال فیلترهای مکرر، دیتابیس ناگزیر است به طور مداوم این رکوردهای TOAST را بازخوانی و دکامپرس کند که این فرآیند سرعت پاسخ‌دهی را به شدت کاهش می‌دهد31.

### **رویکرد بهینه: مدل هیبریدی ارتقایافته (Hybrid Promoted Columns)**

به منظور ترکیب انعطاف‌پذیری JSONB و سرعت بی‌رقیب جداول رابطه‌ای، بهترین مدل برای پیاده‌سازی سیستم سی‌کلاس، معماری هیبریدی است1. در این الگو:

1. **ستون‌های ارتقایافته (Promoted Columns):** فیلترهای عمومی و بسیار پرتراکم که در ۹۰٪ صفحات کاتالوگ تکرار می‌شوند (مانند برند، قیمت، طبقه‌بندی کالا و وضعیت موجودی) به عنوان ستون‌های معمولی و تایپ‌شده رابطه‌ای تعریف می‌شوند و ایندکس‌های استاندارد B-Tree روی آن‌ها اعمال می‌گردد1.  
2. **ستون صفت‌های متغیر (JSONB Column):** ویژگی‌های متغیر، تخصصی و طولانی‌دم (مانند درجه سختی، اوزان چسب، طیف رنگی ماژیک) در یک ستون پویای JSONB به نام attributes قرار می‌گیرند1.  
3. **بهینه‌سازی نمایه GIN با کلاس اپراتور مسیر (jsonb\_path\_ops):** برای کوئری‌هایی که صرفاً از اپراتور شمول (@\>) استفاده می‌کنند، این نوع ایندکس نسبت به حالت عمومی jsonb\_ops تا ۳ برابر فضای دیسک کمتری اشغال کرده و سرعت فیلترینگ را چندین برابر ارتقا می‌دهد30.

## **فرمول‌بندی کوئری‌های پایش ایمن رقبا**

پایش فنی و مهندسی معکوس ساختار فیلترهای رقبا در وب مستلزم استفاده از کوئری‌های جستجوی پیشرفته و هدفمند موتورهای جستجو (Google Dorks) است تا اطلاعات مربوط به ساختار داده‌ها بدون افشای هویت پایشگر استخراج شوند6.

### **فرمول کوئری اول: پایش مدادهای نوکی و اتودهای دیجی‌کالا**

site:digikala.com/category-mechanical-pencils/ "فیلتر" AND "سختی" AND "قطر" \-انتخابات \-احزاب

* **مکانیسم اثر:** این جستار مستقیماً دایرکتوری اصلی دسته‌بندی مداد نوکی دیجی‌کالا را هدف قرار می‌دهد6. استفاده از عملگرهای اجباری "سختی" و "قطر" باعث می‌شود تا صفحات فرعی محصولات فاقد شناسنامه فنی حذف شده و الگوهای نام‌گذاری و فیلترهای فعال رقبا (مانند ضخامت نوک‌های گوناگون نظیر ۰.۵، ۰.۷، ۲.۰، ۵.۰، ۵.۶ میلی‌متر و نشانگر درجه سختی ۴H تا ۲B) استخراج گردند35.  
* **پایداری در برابر آلودگی اطلاعاتی:** استفاده از عبارت‌های منفی (-انتخابات \-احزاب) باعث فیلتر شدن نویزهای خبری روز شده و جلوی انحراف کوئری به سمت نتایج نامربوط در بسترهای میزبانی رقیب را می‌گیرد.

### **فرمول کوئری دوم: پایش مشخصات فنی مدادرنگی برایتون**

site:braitore.ir "مشخصات فنی" AND "مدادرنگی" AND "جعبه فلزی"

* **مکانیسم اثر:** برایتون به عنوان یک فروشگاه تخصصی نوشت‌افزار دارای کاتالوگ دقیقی از برندهای لوکس است. این جستار به طور هدفمند روی مشخصات ساختاری مدادرنگی‌های مجهز به بسته‌بندی لوکس جعبه فلزی متمرکز می‌شود4. خروجی این کوئری، متغیرهای متالورژیکی و ابعادی کالاها را برای همخوانی در سیستم فنی کاتالوگ سی‌کلاس استخراج می‌کند4.

## **انطباق ساختاری کاتالوگ فنی با پایگاه داده سی‌کلاس**

جهت پیاده‌سازی بهینه سیستم فیلترینگ در پایگاه داده فعلی سی‌کلاس بدون تداخل با تراکنش‌های موجود، کدهای استاندارد PostgreSQL DDL و نمونه سناریوی کوئری تعاملی در لایه سرور پیاده‌سازی شده است5.

### **پیاده‌سازی طرحواره پایگاه داده در سطح PostgreSQL DDL**

SQL  
\-- جدول دسته‌بندی با الگوی والد-فرزندی جهت ارث‌بری خودکار ویژگی‌ها  
CREATE TABLE product\_categories (  
    category\_id SERIAL PRIMARY KEY,  
    category\_name VARCHAR(150) NOT NULL,  
    parent\_id INT REFERENCES product\_categories(category\_id) ON DELETE SET NULL,  
    category\_path VARCHAR(255) NOT NULL, \-- مثال: /stationery/writing/pencils  
    created\_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT\_TIMESTAMP  
);

\-- جدول اصلی محصولات با مدل هیبریدی (ستون‌های ارتقایافته عمومی \+ JSONB پویا)  
CREATE TABLE enterprise\_products (  
    product\_id SERIAL PRIMARY KEY,  
    category\_id INT NOT NULL REFERENCES product\_categories(category\_id) ON DELETE RESTRICT,  
    sku VARCHAR(50) UNIQUE NOT NULL,  
    title\_fa VARCHAR(255) NOT NULL,  
    title\_en VARCHAR(255),  
      
    \-- ستون‌های ارتقایافته (Promoted Columns) جهت تضمین سرعت فیلترینگ‌های پرتکرار  
    brand\_name VARCHAR(100) NOT NULL,  
    unit\_price DECIMAL(15, 2) NOT NULL,  
    stock\_qty INT NOT NULL DEFAULT 0,  
    is\_active BOOLEAN DEFAULT TRUE,  
      
    \-- ذخیره‌سازی داده‌های تکامل‌پذیر صنف نوشت‌افزار در قالب سند باینری  
    dynamic\_attributes JSONB NOT NULL DEFAULT '{}'::jsonb,  
      
    \-- اعتبارسنجی ساختار داده‌ها در سطح پایگاه داده برای جلوگیری از ورود فیلدهای هرز \[cite: 7\]  
    CONSTRAINT chk\_dynamic\_attributes\_format CHECK (jsonb\_typeof(dynamic\_attributes) \= 'object'),  
    CONSTRAINT chk\_unit\_price\_positive CHECK (unit\_price \>= 0),  
    CONSTRAINT chk\_stock\_qty\_positive CHECK (stock\_qty \>= 0)  
);

\-- ساخت شاخص‌های استاندارد B-Tree برای ستون‌های ارتقایافته  
CREATE INDEX idx\_ent\_products\_base\_filters ON enterprise\_products (brand\_name, unit\_price, is\_active);  
CREATE INDEX idx\_ent\_products\_cat\_id ON enterprise\_products (category\_id);

\-- ساخت شاخص تعمیم‌یافته معکوس (GIN) مبتنی بر بهینه‌ترین کلاس اپراتور مسیر برای فیلترهای پویا  
CREATE INDEX idx\_ent\_products\_dyn\_attr\_path\_gin ON enterprise\_products USING GIN (dynamic\_attributes jsonb\_path\_ops);

### **سناریوی کوئری فیلترینگ ترکیبی بهینه**

جهت اعمال فیلتر ترکیبی برای کاربری که در دسته‌بندی مدادهای نوکی به دنبال برند "سی‌کلاس" با قیمت متوسط، ضخامت نوشتاری 0.7 میلی‌متر و بدنه ارگونومیک پلاستیکی با فرم چسبنده مثلثی است، سیستم کوئری زیر را با کارایی بهینه اجرا می‌کند5:

SQL  
SELECT product\_id, sku, title\_fa, unit\_price, dynamic\_attributes\-\>\>'body\_material' AS material  
FROM enterprise\_products  
WHERE category\_id \= 120 \-- شناسه دسته مداد نوکی  
  AND brand\_name \= 'C-Class' \-- فیلتر مستقیم روی ستون ارتقایافته (حذف اسکن کلیدهای بزرگ)  
  AND unit\_price BETWEEN 120000 AND 450000 \-- رنج قیمت ارتقایافته  
  AND is\_active \= TRUE  
  \-- کوئری شمول متغیرهای پویا مبتنی بر شاخص GIN با سرعت میلی‌ثانیه \[cite: 34, 41\]  
  AND dynamic\_attributes @\> '{"lead\_diameter": "0.7mm", "body\_material": "Plastic", "cross\_section": "Triangle"}';

## **ماتریس مشخصات فنی دسته‌های جدید نوشت‌افزار**

این ماتریس فکت‌های استخراج شده از نمونه‌های فنی رقبای فعال در بازار (نظیر فابر کاستل، زبرا، اوهو، کنکو و پنتر) را به عنوان ساختار مرجع مشخصات فنی جهت پیاده‌سازی در سیستم سی‌کلاس ترسیم می‌کند11.

| ردیف | دسته محصول | ویژگی‌های کلیدی در JSONB | نوع داده (Datatype) | نمونه مقادیر استاندارد بازار (Factual Data) | توجیه تجربه کاربری و مهندسی داده |
| ----: | ----: | ----: | ----: | ----: | ----: |
| ۱ | **مداد طراحی** \[cite: 4, 11\] | lead\_hardness \[cite: 11\] core\_material \[cite: 12\] body\_length \[cite: 11\] casing\_wood \[cite: 11\] pack\_material \[cite: 4, 13\] | String String Integer (mm) String String | ![][image1] to ![][image2], ![][image3], ![][image4] \[cite: 11\] گرافیت، کنته، زغال12 ۱۷۵ میلی‌متر11 چوب سدر، شمش بی‌روکش12 جعبه فلزی، جعبه مقوایی4 | نمایش سختی نوک به صورت ماتریس عمودی جهت تسهیل انتخاب طراحان؛ تفکیک جنس جعبه برای خرید هدیه یا هنرجویی11. |
| ۲ | **اتود (مداد نوکی)** \[cite: 6, 44\] | lead\_diameter \[cite: 35, 42\] grip\_material \[cite: 36, 45\] break\_resistant \[cite: 36, 43\] built\_in\_sharpener \[cite: 38\] body\_weight \[cite: 40, 43\] | String String Boolean Boolean Integer (g) | ۰.۳، ۰.۵، ۰.۷، ۰.۹، ۲.۰، ۵.۶ میلی‌متر38 سیلیکونی، فلزی، پوشش ارگونومیک لاستیکی36 true (سیستم‌های دو زمانه یا دلگارد)36 true (مخصوص اتودهای طراحی ضخیم)38 ۱۶ گرم تا ۴۸ گرم38 | نمایش گزینه‌های قطر نوشتاری به صورت نمادهای دایره‌ای لمسی؛ ارائه فیلترهای دودویی (Toggle) برای ویژگی‌های مقاومتی17. |
| ۳ | **چسب ماتیکی** \[cite: 5, 19\] | weight\_grams \[cite: 5, 19\] pack\_quantity \[cite: 5, 19\] solvent\_free \[cite: 22\] washable \[cite: 26\] | Integer Integer Boolean Boolean | ۸، ۹، ۱۵، ۲۱، ۲۵، ۳۶، ۴۰ گرم5 ۱ عددی، ۳ عددی، ۶ عددی، ۲۴ عددی5 true / false \[cite: 22\] true / false \[cite: 26\] | استفاده از چک‌باکس تکی دقیق وزن به دلیل استانداردهای ثابت صنعتی؛ استفاده از بسته‌بندی چندتایی برای مخاطبان مدارس5. |
| ۴ | **ماژیک نقاشی** \[cite: 20, 21\] | color\_pack\_count \[cite: 20, 26\] spectrum\_theme \[cite: 20\] tip\_type \[cite: 27, 47\] water\_based\_ink \[cite: 26\] | Integer String String Boolean | ۶، ۱۲، ۱۸، ۲۴، ۳۶، ۵۰، ۶۰، ۱۰۰ رنگ20 کلاسیک، پاستلی، نئونی، نود/پوست، اکلیلی20 نمدی، فیبری، اسفنجی نشکن، قلمویی (Brush)26 true / false \[cite: 26\] | مهار شلوغی سایدبار با تقسیم‌بندی بسته‌ها به پله‌های فیلترینگ و پالت‌های تصویری هوشمند و تم‌های رنگی کاربرپسند17. |

## **استراتژی مپینگ فیلترهای ناوبری (Navigation Filters Map) برای سیستم جدید سی‌کلاس**

این بخش نحوه اتصال لایه تعاملی فرانت‌اند به لایه داده‌ای پایگاه داده برای فیلترهای نهایی دسته‌بندی‌ها را تعریف می‌کند1.

### **مداد طراحی و مداد مشکی عمومی**

* **فیلتر قیمت و برند:** کنترلر اسلایدر دوگانه عددی دسکتاپ و ستون مستقیم ایندکس‌شده در پایگاه داده17.  
* **درجه سختی مغز:** کلید lead\_hardness در قالب فیلتر تعاملی چندانتخابی آکاردئونی بدون بسته شدن خودکار11.  
* **فرم سطح مقطع بدنه:** کلید cross\_section با دکمه‌های آیکون‌دار سه‌بعدی ارگونومیک (مثل آیکون مثلث برای مدادهای ارگونومیک)10.

### **اتود و مغز اتود**

* **قطر نوشتاری (ضخامت نوک):** کلید lead\_diameter؛ نمایش در قالب دایره‌های لمسی مجهز به اعداد (مانند 0.5 و 0.7) در لایه فرانت‌اند جهت افزایش سرعت فیلترینگ17.  
* **ساختار بدنه و گریپ:** کلید grip\_material؛ تفکیک اتودهای با گریپ لاستیکی و ارگونومیک برای نگارش‌های طولانی‌مدت آموزشی36.

### **چسب‌های ماتیکی**

* **وزن دقیق کالا:** کلید weight\_grams؛ نمایش به صورت چک‌باکس‌های تکی گسسته؛ فیلدهای تکراری مخفی شده و فاقد موجودی به صورت خودکار به رنگ خاکستری غیرفعال در می‌آیند تا خطای "Nothing Found" برطرف شود5.  
* **بسته‌بندی عددی:** کلید pack\_quantity؛ فیلتر تفکیک‌کننده برای خریداران سازمانی نوشت‌افزار اداری5.

### **ماژیک‌های رنگ‌آمیزی و راندو**

* **تم رنگی:** کلید spectrum\_theme؛ نمایش پالت‌های گرد رنگی بصری (Pastel, Metallic, Neon) با قابلیت فعال‌سازی چندگانه17.  
* **تعداد رنگ در بسته:** کلید color\_pack\_count؛ چک‌باکس‌های گروه‌بندی‌شده همراه با دکمه "مشاهده بیشتر" برای جلوگیری از دراز شدن سایدبار موبایل9.

با اجرای این معماری هیبریدی و بهینه‌سازی‌های رابط کاربری، پایگاه داده پلتفرم سی‌کلاس علاوه بر حفظ پایداری پردازشی در مقیاس‌های بزرگ، سریع‌ترین مسیر دسترسی به محصول را برای مخاطبان فراهم می‌سازد5.

#### **Works cited**

1. Ecommerce product attributes database design: Best practices & patterns \- ALLSTARSIT, [https://www.allstarsit.com/blog/ecommerce-product-attributes-database-design-best-practices-patterns](https://www.allstarsit.com/blog/ecommerce-product-attributes-database-design-best-practices-patterns)  
2. Ultimate Guide to Mobile-First Design with Examples \- GitNexa, [https://www.gitnexa.com/blogs/mobile-first-design-guide](https://www.gitnexa.com/blogs/mobile-first-design-guide)  
3. WordPress Agency UK for Complex Websites That Need to Scale \- Prime Lion Digital, [https://primeliondigital.co.uk/services/web-design-development/cms-development/wordpress-agency/](https://primeliondigital.co.uk/services/web-design-development/cms-development/wordpress-agency/)  
4. مداد اونر \- خرید انواع جدید مداد Owner با بهترین قیمت \- Digikala, [https://www.digikala.com/search/category-pencil/owner/](https://www.digikala.com/search/category-pencil/owner/)  
5. خرید و قیمت چسب سی.کلاس \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-glue/c-class/](https://www.digikala.com/search/category-glue/c-class/)  
6. خرید و قیمت مداد نوکی سی.کلاس \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-mechanical-pencils/c-class/](https://www.digikala.com/search/category-mechanical-pencils/c-class/)  
7. PostgreSQL as a JSON database: Advanced patterns and best practices \- AWS, [https://aws.amazon.com/blogs/database/postgresql-as-a-json-database-advanced-patterns-and-best-practices/](https://aws.amazon.com/blogs/database/postgresql-as-a-json-database-advanced-patterns-and-best-practices/)  
8. خرید جدیدترین انواع مداد مشکی و گلی \- Digikala, [https://www.digikala.com/search/category-pencil/](https://www.digikala.com/search/category-pencil/)  
9. 16 Hacks to Build Ultimate Filter UX/UI \- Searchanise, [https://searchanise.io/blog/filter-ui/](https://searchanise.io/blog/filter-ui/)  
10. مداد سه‌گوش ارگونومیک | خرید اینترنتی، قیمت، بررسی مدل‌ها \- Digikala, [https://www.digikala.com/search/facet/category-pencil/cross-sectional-form-triangle/](https://www.digikala.com/search/facet/category-pencil/cross-sectional-form-triangle/)  
11. فروشگاه اینترنتی دیجی‌کالا, [https://www.digikala.com/product/dkp-82599/%D9%85%D8%AF%D8%A7%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%D9%81%D8%A7%D8%A8%D8%B1-%DA%A9%D8%A7%D8%B3%D8%AA%D9%84-%D9%85%D8%AF%D9%84-9000-%D8%A8%D8%A7-%D8%AF%D8%B1%D8%AC%D9%87-%D8%B3%D8%AE%D8%AA%DB%8C-%D9%86%D9%88%DA%A9-hb](https://www.digikala.com/product/dkp-82599/%D9%85%D8%AF%D8%A7%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%D9%81%D8%A7%D8%A8%D8%B1-%DA%A9%D8%A7%D8%B3%D8%AA%D9%84-%D9%85%D8%AF%D9%84-9000-%D8%A8%D8%A7-%D8%AF%D8%B1%D8%AC%D9%87-%D8%B3%D8%AE%D8%AA%DB%8C-%D9%86%D9%88%DA%A9-hb)  
12. مداد کنته پاریس \- خرید بهترین انواع مداد Conte a Paris \- Digikala, [https://www.digikala.com/search/category-pencil/conte-a-paris/](https://www.digikala.com/search/category-pencil/conte-a-paris/)  
13. قیمت و خرید مداد طراحی کرتاکالر کد 16003 با درجه سختی 3B بسته 3, [https://www.digikala.com/product/dkp-514274/%D9%85%D8%AF%D8%A7%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%DA%A9%D8%B1%D8%AA%D8%A7%DA%A9%D8%A7%D9%84%D8%B1-%DA%A9%D8%AF-16003-%D8%A8%D8%A7-%D8%AF%D8%B1%D8%AC%D9%87-%D8%B3%D8%AE%D8%AA%DB%8C-3b-%D8%A8%D8%B3%D8%AA%D9%87-3-%D8%B9%D8%AF%D8%AF%DB%8C](https://www.digikala.com/product/dkp-514274/%D9%85%D8%AF%D8%A7%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%DA%A9%D8%B1%D8%AA%D8%A7%DA%A9%D8%A7%D9%84%D8%B1-%DA%A9%D8%AF-16003-%D8%A8%D8%A7-%D8%AF%D8%B1%D8%AC%D9%87-%D8%B3%D8%AE%D8%AA%DB%8C-3b-%D8%A8%D8%B3%D8%AA%D9%87-3-%D8%B9%D8%AF%D8%AF%DB%8C)  
14. 19+ Filter UI Examples for SaaS: Design Patterns & Best Practices \- Eleken, [https://www.eleken.co/blog-posts/filter-ux-and-ui-for-saas](https://www.eleken.co/blog-posts/filter-ux-and-ui-for-saas)  
15. Ecommerce Search Filters | Best Practices to Improve UX and Boost Conversions \- Evinent, [https://evinent.com/blog/ecommerce-search-filters](https://evinent.com/blog/ecommerce-search-filters)  
16. Designing Search UX: Filter Design Patterns and Key Takeaways | by Neha Tibrewal, [https://medium.com/@tibrewal.n99/designing-search-ux-filter-design-patterns-and-key-takeaways-748ad1321e4d](https://medium.com/@tibrewal.n99/designing-search-ux-filter-design-patterns-and-key-takeaways-748ad1321e4d)  
17. What Is an Ecommerce Filter? UI Best Practices \- Baymard, [https://baymard.com/learn/ecommerce-filter-ui](https://baymard.com/learn/ecommerce-filter-ui)  
18. 12 Best Ecommerce Filters Strategies & Solutions to to Boost Conversions \- Wizzy.ai, [https://wizzy.ai/blog/ecommerce-filters-strategies/](https://wizzy.ai/blog/ecommerce-filters-strategies/)  
19. خرید و قیمت چسب اینوکس \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-glue/inox/](https://www.digikala.com/search/category-glue/inox/)  
20. ماژیک فابر کاستل \- خرید بهترین انواع ماژیک Faber Castell \- Digikala, [https://www.digikala.com/search/category-marker/faber-castell/](https://www.digikala.com/search/category-marker/faber-castell/)  
21. ماژیک پیکاسو \- خرید بهترین انواع ماژیک Picasso با قیمت عالی \- Digikala, [https://www.digikala.com/search/category-marker/picasso/](https://www.digikala.com/search/category-marker/picasso/)  
22. چسب اوهو \- خرید و لیست قیمت بهترین انواع چسب Uhu \- Digikala, [https://www.digikala.com/search/category-glue/uhu/](https://www.digikala.com/search/category-glue/uhu/)  
23. خرید و قیمت چسب کنکو \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-glue/canco/](https://www.digikala.com/search/category-glue/canco/)  
24. چسب پنتر \- خرید بهترین انواع چسب Panter با قیمت ارزان \- Digikala, [https://www.digikala.com/search/category-glue/panter/](https://www.digikala.com/search/category-glue/panter/)  
25. خرید و قیمت چسب ماین \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-glue/mine/](https://www.digikala.com/search/category-glue/mine/)  
26. ماژیک رنگ آمیزی 100 رنگ اسکول فنز مدل جونیور کد 922206 \- Digikala, [https://www.digikala.com/product/dkp-21274731/%D9%85%D8%A7%DA%98%DB%8C%DA%A9-%D8%B1%D9%86%DA%AF-%D8%A2%D9%85%DB%8C%D8%B2%DB%8C-100-%D8%B1%D9%86%DA%AF-%D8%A7%D8%B3%DA%A9%D9%88%D9%84-%D9%81%D9%86%D8%B2-%D9%85%D8%AF%D9%84-%D8%AC%D9%88%D9%86%DB%8C%D9%88%D8%B1-%DA%A9%D8%AF-922206](https://www.digikala.com/product/dkp-21274731/%D9%85%D8%A7%DA%98%DB%8C%DA%A9-%D8%B1%D9%86%DA%AF-%D8%A2%D9%85%DB%8C%D8%B2%DB%8C-100-%D8%B1%D9%86%DA%AF-%D8%A7%D8%B3%DA%A9%D9%88%D9%84-%D9%81%D9%86%D8%B2-%D9%85%D8%AF%D9%84-%D8%AC%D9%88%D9%86%DB%8C%D9%88%D8%B1-%DA%A9%D8%AF-922206)  
27. ماژیک رنگ آمیزی وای پلاس مدل 24S بسته 24 عددی \- Digikala, [https://www.digikala.com/product/dkp-21102067/%D9%85%D8%A7%DA%98%DB%8C%DA%A9-%D8%B1%D9%86%DA%AF-%D8%A2%D9%85%DB%8C%D8%B2%DB%8C-%D9%88%D8%A7%DB%8C-%D9%BE%D9%84%D8%A7%D8%B3-%D9%85%D8%AF%D9%84-24s-%D8%A8%D8%B3%D8%AA%D9%87-24-%D8%B9%D8%AF%D8%AF%DB%8C](https://www.digikala.com/product/dkp-21102067/%D9%85%D8%A7%DA%98%DB%8C%DA%A9-%D8%B1%D9%86%DA%AF-%D8%A2%D9%85%DB%8C%D8%B2%DB%8C-%D9%88%D8%A7%DB%8C-%D9%BE%D9%84%D8%A7%D8%B3-%D9%85%D8%AF%D9%84-24s-%D8%A8%D8%B3%D8%AA%D9%87-24-%D8%B9%D8%AF%D8%AF%DB%8C)  
28. JSONB vs EAV in PostgreSQL: Which Is Better for Dynamic Attributes? \- BSWEN, [https://docs.bswen.com/blog/2026-04-24-jsonb-vs-eav-postgresql/](https://docs.bswen.com/blog/2026-04-24-jsonb-vs-eav-postgresql/)  
29. Refining a Product Catalog: EAV vs. PostgreSQL JSONB for a pharmacy e-commerce platform \- Stack Overflow, [https://stackoverflow.com/questions/79885346/refining-a-product-catalog-eav-vs-postgresql-jsonb-for-a-pharmacy-e-commerce-p](https://stackoverflow.com/questions/79885346/refining-a-product-catalog-eav-vs-postgresql-jsonb-for-a-pharmacy-e-commerce-p)  
30. How to Index JSONB Columns in PostgreSQL \- Tiger Data, [https://www.tigerdata.com/learn/how-to-index-json-columns-in-postgresql](https://www.tigerdata.com/learn/how-to-index-json-columns-in-postgresql)  
31. Scaling Postgres for Dynamic Schema Search on Billions of Rows \- Unfinished Side Projects, [https://blog.jakesaunders.dev/schemaless-search-in-postgres/](https://blog.jakesaunders.dev/schemaless-search-in-postgres/)  
32. PostgreSQL Querying & Filtering JSON Fields \- DataCamp, [https://www.datacamp.com/doc/postgresql/querying-&-filtering-json-fields](https://www.datacamp.com/doc/postgresql/querying-&-filtering-json-fields)  
33. JSONB: PostgreSQL's Secret Weapon for Flexible Data Modeling | by Rick Hightower, [https://medium.com/@richardhightower/jsonb-postgresqls-secret-weapon-for-flexible-data-modeling-cf2f5087168f](https://medium.com/@richardhightower/jsonb-postgresqls-secret-weapon-for-flexible-data-modeling-cf2f5087168f)  
34. PostgreSQL GIN Indexes: JSONB, Arrays & Full-Text Search \- DEV Community, [https://dev.to/philip\_mcclarence\_2ef9475/postgresql-gin-indexes-jsonb-arrays-full-text-search-29i2](https://dev.to/philip_mcclarence_2ef9475/postgresql-gin-indexes-jsonb-arrays-full-text-search-29i2)  
35. اتود کرند مدل pelin قطر نوشتاری 0.7 میلی متر بسته 12عددی \- Digikala, [https://www.digikala.com/product/dkp-1016331/%D8%A7%D8%AA%D9%88%D8%AF-%DA%A9%D8%B1%D9%86%D8%AF-%D9%85%D8%AF%D9%84-pelin-%D9%82%D8%B7%D8%B1-%D9%86%D9%88%D8%B4%D8%AA%D8%A7%D8%B1%DB%8C-07-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1-%D8%A8%D8%B3%D8%AA%D9%87-12%D8%B9%D8%AF%D8%AF%DB%8C](https://www.digikala.com/product/dkp-1016331/%D8%A7%D8%AA%D9%88%D8%AF-%DA%A9%D8%B1%D9%86%D8%AF-%D9%85%D8%AF%D9%84-pelin-%D9%82%D8%B7%D8%B1-%D9%86%D9%88%D8%B4%D8%AA%D8%A7%D8%B1%DB%8C-07-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1-%D8%A8%D8%B3%D8%AA%D9%87-12%D8%B9%D8%AF%D8%AF%DB%8C)  
36. اتود کرند مدل armic قطر نوشتاری 0.5 میلی متری تک عددی \- Digikala, [https://www.digikala.com/product/dkp-1018450/%D8%A7%D8%AA%D9%88%D8%AF-%DA%A9%D8%B1%D9%86%D8%AF-%D9%85%D8%AF%D9%84-armic-%D9%82%D8%B7%D8%B1-%D9%86%D9%88%D8%B4%D8%AA%D8%A7%D8%B1%DB%8C-05-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1%DB%8C-%D8%AA%DA%A9-%D8%B9%D8%AF%D8%AF%DB%8C](https://www.digikala.com/product/dkp-1018450/%D8%A7%D8%AA%D9%88%D8%AF-%DA%A9%D8%B1%D9%86%D8%AF-%D9%85%D8%AF%D9%84-armic-%D9%82%D8%B7%D8%B1-%D9%86%D9%88%D8%B4%D8%AA%D8%A7%D8%B1%DB%8C-05-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1%DB%8C-%D8%AA%DA%A9-%D8%B9%D8%AF%D8%AF%DB%8C)  
37. قیمت و خرید مداد نوکی کوییلو طرح مدرسه \- کد 634065 با قطر نوشتاری, [https://www.digikala.com/product/dkp-51153/%D9%85%D8%AF%D8%A7%D8%AF-%D9%86%D9%88%DA%A9%DB%8C-%DA%A9%D9%88%DB%8C%DB%8C%D9%84%D9%88-%D8%B7%D8%B1%D8%AD-%D9%85%D8%AF%D8%B1%D8%B3%D9%87-%DA%A9%D8%AF-634065-%D8%A8%D8%A7-%D9%82%D8%B7%D8%B1-%D9%86%D9%88%D8%B4%D8%AA%D8%A7%D8%B1%DB%8C-05-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D8%A8%D8%A7-%D9%86%D9%88%DA%A9-05-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1-hb](https://www.digikala.com/product/dkp-51153/%D9%85%D8%AF%D8%A7%D8%AF-%D9%86%D9%88%DA%A9%DB%8C-%DA%A9%D9%88%DB%8C%DB%8C%D9%84%D9%88-%D8%B7%D8%B1%D8%AD-%D9%85%D8%AF%D8%B1%D8%B3%D9%87-%DA%A9%D8%AF-634065-%D8%A8%D8%A7-%D9%82%D8%B7%D8%B1-%D9%86%D9%88%D8%B4%D8%AA%D8%A7%D8%B1%DB%8C-05-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D8%A8%D8%A7-%D9%86%D9%88%DA%A9-05-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1-hb)  
38. اتود طراحی 5.6 میلی متری ترویکا مدل zimmerman \- Digikala, [https://www.digikala.com/product/dkp-2278645/%D8%A7%D8%AA%D9%88%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-56-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1%DB%8C-%D8%AA%D8%B1%D9%88%DB%8C%DA%A9%D8%A7-%D9%85%D8%AF%D9%84-zimmerman](https://www.digikala.com/product/dkp-2278645/%D8%A7%D8%AA%D9%88%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-56-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1%DB%8C-%D8%AA%D8%B1%D9%88%DB%8C%DA%A9%D8%A7-%D9%85%D8%AF%D9%84-zimmerman)  
39. اتود طراحی 5 میلی متری کوه نور مدل 5347 \- Digikala, [https://www.digikala.com/product/dkp-2293634/%D8%A7%D8%AA%D9%88%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-5-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1%DB%8C-%DA%A9%D9%88%D9%87-%D9%86%D9%88%D8%B1-%D9%85%D8%AF%D9%84-5347](https://www.digikala.com/product/dkp-2293634/%D8%A7%D8%AA%D9%88%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-5-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1%DB%8C-%DA%A9%D9%88%D9%87-%D9%86%D9%88%D8%B1-%D9%85%D8%AF%D9%84-5347)  
40. بهترین مداد نوکی؛ کدام مدل‌ ایرانی، خارجی یا فانتزی بهتر است؟ \- Digikala, [https://www.digikala.com/mag/the-best-mechanical-pencil/](https://www.digikala.com/mag/the-best-mechanical-pencil/)  
41. نوک \- خرید و قیمت انواع نوک مداد نوکی (رنگی و سیاه) \- Digikala, [https://www.digikala.com/search/category-tip/](https://www.digikala.com/search/category-tip/)  
42. مداد نوکی 0.5 میلی متری زبرا مدل Delguard-lx \- Digikala, [https://www.digikala.com/product/dkp-222771/%D9%85%D8%AF%D8%A7%D8%AF-%D9%86%D9%88%DA%A9%DB%8C-05-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1%DB%8C-%D8%B2%D8%A8%D8%B1%D8%A7-%D9%85%D8%AF%D9%84-delguard-lx](https://www.digikala.com/product/dkp-222771/%D9%85%D8%AF%D8%A7%D8%AF-%D9%86%D9%88%DA%A9%DB%8C-05-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1%DB%8C-%D8%B2%D8%A8%D8%B1%D8%A7-%D9%85%D8%AF%D9%84-delguard-lx)  
43. خرید انواع مداد نوکی Panter با بهترین قیمت \- Digikala, [https://www.digikala.com/search/category-mechanical-pencils/panter/](https://www.digikala.com/search/category-mechanical-pencils/panter/)  
44. خرید و مقایسه‌ی مداد نوکی پارسیکار مدل JM802-N2، مداد نوکی پنتر مدل M and G و مداد نوکی زبرا مدل Drafix \- Digikala, [https://www.digikala.com/mag/video/parsikar-0-7-mm-pencil-vs-panter-m-and-g-2mm-mechanical-pencil-vs-zebra-drafix-0-5mm-mechanical-pencil-unboxing-review/](https://www.digikala.com/mag/video/parsikar-0-7-mm-pencil-vs-panter-m-and-g-2mm-mechanical-pencil-vs-zebra-drafix-0-5mm-mechanical-pencil-unboxing-review/)  
45. قیمت و خرید چسب ماتیکی بیسیک مدل 36 بسته 6 عددی \- Digikala, [https://www.digikala.com/product/dkp-5334857/%DA%86%D8%B3%D8%A8-%D9%85%D8%A7%D8%AA%DB%8C%DA%A9%DB%8C-%D8%A8%DB%8C%D8%B3%DB%8C%DA%A9-%D9%85%D8%AF%D9%84-36-%D8%A8%D8%B3%D8%AA%D9%87-6-%D8%B9%D8%AF%D8%AF%DB%8C](https://www.digikala.com/product/dkp-5334857/%DA%86%D8%B3%D8%A8-%D9%85%D8%A7%D8%AA%DB%8C%DA%A9%DB%8C-%D8%A8%DB%8C%D8%B3%DB%8C%DA%A9-%D9%85%D8%AF%D9%84-36-%D8%A8%D8%B3%D8%AA%D9%87-6-%D8%B9%D8%AF%D8%AF%DB%8C)  
46. ماژیک نقاشی 24 رنگ مدل B24 \- Digikala, [https://www.digikala.com/product/dkp-1646542/%D9%85%D8%A7%DA%98%DB%8C%DA%A9-%D9%86%D9%82%D8%A7%D8%B4%DB%8C-24-%D8%B1%D9%86%DA%AF-%D9%85%D8%AF%D9%84-b24](https://www.digikala.com/product/dkp-1646542/%D9%85%D8%A7%DA%98%DB%8C%DA%A9-%D9%86%D9%82%D8%A7%D8%B4%DB%8C-24-%D8%B1%D9%86%DA%AF-%D9%85%D8%AF%D9%84-b24)  
47. ماژیک رنگ آمیزی 12 رنگ استدلر مدل Noris Club \- Digikala, [https://www.digikala.com/product/dkp-95101/%D9%85%D8%A7%DA%98%DB%8C%DA%A9-%D8%B1%D9%86%DA%AF-%D8%A2%D9%85%DB%8C%D8%B2%DB%8C-12-%D8%B1%D9%86%DA%AF-%D8%A7%D8%B3%D8%AA%D8%AF%D9%84%D8%B1-%D9%85%D8%AF%D9%84-noris-club](https://www.digikala.com/product/dkp-95101/%D9%85%D8%A7%DA%98%DB%8C%DA%A9-%D8%B1%D9%86%DA%AF-%D8%A2%D9%85%DB%8C%D8%B2%DB%8C-12-%D8%B1%D9%86%DA%AF-%D8%A7%D8%B3%D8%AA%D8%AF%D9%84%D8%B1-%D9%85%D8%AF%D9%84-noris-club)  
48. 9 Filtering Design Best Practices to Improve E-Commerce UX, [https://uxplanet.org/9-filtering-design-best-practices-to-improve-e-commerce-ux-edac50560f94](https://uxplanet.org/9-filtering-design-best-practices-to-improve-e-commerce-ux-edac50560f94)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAWCAYAAADeiIy1AAABg0lEQVR4Xu2UvytGURjHv0JRryRK8payKWVikEGRLG8ZJMUgi83Of2BQktFiM9hkkeEdlVmKFKVMUgYlhe+35+Q995xz77vIdL/1Gc7znHOfH+c5Fyj1jxohc6RKpskimSQtpI8skAnn174Z0q6DQ+SW7JFOskVunD1PF+SLzIYOp0OyERpPyTMZdutB8kAOYFmmpP1PsKxD9ZArMhU63sgjGXDrCqnDgiloSqrmjHSEDlhrX2BtzOgb6UDvZNzZQunMdmh0WoH5o24ou1Qgba45my9VUXQ/+7CzkdRvP5BKvkZ+IN2LfEWoG5E0ba9k1K3nYRnnBVIlze5HiSbVCvuAytYA1GFDMubtkfRxBWnWtmi0JQXp8tb95J5ckm7PLukJqNVFY/2JxGhLu7Aslt1amz7I6u+OhlSJ2ppqm6pXF9S2aLSlI1igJbfWqz+HTZ8vjesOciaKWoP5Tkhb1mXShd/B3sUmOUa2Zf4U+qyjcWehLy8Z9MIC6gcZPbRSpf5UP9UZXrE6u0l6AAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAWCAYAAADafVyIAAABgklEQVR4Xu2UvytGURjHv5JBfiVKMogRMcigjAaGtxRJ8RcYbBS7UUkySEkWWZlkeMsiZilSSCkGpSjKj++3c+77nnvuOTbb/dan7vPjnOec5zxdINc/aIxMRFCsqpxq1E6uyCqpJovk0vpjWiM/ZNoPUG/kmXQnjgPySDqt3UZuyTqpsD5XNeSYvJI+LyadwBQvJA4l3pFWa9eSIkwRFfOlg+hA56TRi0mKfZDBxKFqoQLvZMD6XI3CrFGbfOnGim3CeYtvhAukruloGeH+15MNMg/voXUlt0AzuUC8gPqv2BO5t+j7i+w7eSVpel5Ij7VHYG4VKxDrvyZwi8wiMByVZBimr3rYIuJTEmpPInVBY9rvOrV5nWO3kBtyShocv6QRjRWWhsgD6XCdKzCnmrK2kjRmM6WMsjSiofZIOozeZwFei3ZgCkxaW0lHMNPka5xsI72BvnvJGcw+mV+FHvKaLJE5sod0a9TCXZjFMT7JIemyazJqgimkH1ZmAnLl+lO/60Vb6BjrFi8AAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAXCAYAAADz/ZRUAAABrklEQVR4Xu2UvytGURjHH4WSDEpJJkpCoYTIQCZJCZvFpoyKDDYZrAaDlCSDH4M/wGYwmJXFQErIQJEfA9/ve87jPZ73XKVXGdxvfXrve77nPPfe53vOFUn1x6oGY2AIdPjrflAESsEg6AVVHl5zLFQFGBa31sLxOnH1cjQAVsEpuAcbYA6UgFbvHYF38Ap2wVJmZVbdkq3Befzlf7INnsTV5r2iWgOTdtBrWlzRZWsY0ee8cTPeCR7BLWgynjSAO3Hts+LYiTif85JUC67AMShP8F5Al/EyT8onLrAG1APewCEoM14otjTWHdZc8B5jyMle2xUTo4gVtVqUeMtXwDOYkciN+TZ8Ky78jhFdEBFPxYG4eTfgwsPrHXFtj0rzZq5Wv5E3NzJPyZREYtW8t6whP8+bN7LSB7sG9cb7zDt2zPLNm+KH6VzcUWsLDbaIreJHoD00oEKwJ8lFVZr3A2gxHqXduwQ1oRHmbc94JTiT/PKmdCPOisl8whvM226GPnFPnFRUNSquxrp8rcHrZu/Nizlm9igRSveAZR8U+znUZmSOhbu8URekSvX/9AFPl4bjOhwR3QAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAYCAYAAADKx8xXAAAA7ElEQVR4Xu2SsQtBURSHj0EpCyUlm81kkI1NRoOsZruNXTIoKwt2ZbL5DwwWRmVikGwWhd/pHLnvvvdkpHz19e67557bOec9op8lAhMfGHomMPzShGt4VydwCBdwr3s3WNQcB2l4gks7AAokF2TtAFMmuXlkB0AUTknKddEmSazbAZLEgT4dhEn6ucCc7uVhV9dx2CFrOEwKHuAGxmAA9mHFPOQFT4undiTpcQXPMGMe8qJF0t8YVkk+B0/X1ZNJEu5UXjNcQU3XvvAQrnBOHs2/o0FSJpf7MUE4IxlMyYr5sqXXv2naMw/9+Woem68vsbW9FgQAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAZCAYAAACFHfjcAAACFklEQVR4Xu2Wvyt+URzH35KiiHxFymizKIPJaDB8FwaLzWK0SNkUpSwGgygyyPDty0LWJwaL0R9AmZgpyo/Pu3NPjs9z7rnnPInlvOrdfe655zl9zuv5PPdeIJPJZL6HOcmNHlT0Sq714C/AWvv1oGJDUpO0q/EgQ5IHya2+4NAEs/i7vvDD2FqrRLwiUUSb5L/kBWER45J7/K4It9aQCHbuGxJFsM1WJecoF8GFjyXziBfRIunRg4o+SbMeDODWWiaCnbsOs5caIkWwzf5JBmC+5BNhF56W/EW8CBZAeZP6QsGU5ASRhaK+1jIR7NwtJIjgL7YrGYOZXINfBK9zHueniCDdkjOYTbvw/FTSqcbL8NXqE/FHciQZRIKIGckyzC9eJsJdmKSKID4ZKRKIr1Ytgtc4h3NJlAhujBvkRolPhF6YNCKCuDIYnsdSVqsW4XYuqRTBiZswX7T4RIxKdvC5MGlUBOFGLovEEqrVFcHuOsRn55JKEcOSbZUDyXORBUlXcdTzrmBE8DPXiYGdxRut/Tsw+p5RRqhWHlljq2TCM4+PT75v7ElmEQnt0qC+R2gWkdYRWoKF57EyNLZW/dfQPKKiI3zwkXRXJMQS4kVYCXyE6hsjzxuVYWvlMcST5ELSoS/4sHa5OZsa6i3aTnDD+0UIvoStoV6CheMrqH7pssTWOgLTDe68/S8zMplMJpPJZBL4AKzVjx0Z7ikUAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,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>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAaCAYAAABGiCfwAAABrElEQVR4Xu2UPShGYRTHj1BEJMqilEGZDEoxSRKLwcdkMLKw+SiGdzEYFGWSMjJYlWSQwcBkkBIlhVISRSgf/7/zPO+997jvtUr3V7/e957zfNz7nHOvSMp/IB+ewRt4BedgWWSEUgKn4QZ8d/L/csgPuA7L3ZwIeTADi911M7yHJ7DGxSwN8A4ewgqTW4WfcEF07QjV8By2uesiuCk6YdjFLN2i+RWbAL2iuV1YGk2JVMIj2OGuw5tN+kGGWdH8oE1IkFuDBSb3De/APzKflEf4CluyIwJYtx3RY+RxWq5Fy8ByJMINJ0SLzN8fZw7qRBvJ1otj2+EBrA/FY2EH3Yre8YDEb0R8vd7gZUhe8yYKg6G54eKsH5viAY5L/MSkerXCfcndxT/gpkuiC9qj9PV6hI2heBjOm7dBT4/oyxluU9++tgmSWp6w+5jPmHgWTuQAdqGHLc/YMawKxZOOkPTBU1hrE54u+CLBcfFLsiW66Igf5NiDT7DJxHm8U6JNEvc6ZGETzMBFOAS3RTcfE/1mEr4zz6I3kMsLOOrG/0on7He/sR/RlJSUv8kXljlijRveMHQAAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAaCAYAAABVX2cEAAABGUlEQVR4XmNgGAXUArOA+AwQ/wfin0BsiSrNoADE7xkg8jeAeAIQSyIrQAfTgfgiA0TDFCBmRJVmCALiVUDMiiaOAQSBeCMQBzBAXPAEiBVRVDAwtAJxNJoYVqAPxIuBmAeIlzNAXNeArAAIVjNA1BEEIBuroGwPIP4HxNeBWByuAuJykA8IAlB4uUDZ/EB8ggHiugi4CkgkEQXWAbEMEj+HAWLYDiDmhIoRFV4gMB+IOZD4oMAHRQIsmXADsSaSPF4ACy8YACULUPKAJRMVBiLDC6QI2YswAEpPoHQFMvALmhxOYMyA6kVkAIvZt+gS2AAoLNoZEIGMDmAxexhdAhmAXLKVAeIFGE5CUYEAoJidhC44CkbBkAQAgEMwHNeHByEAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,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>