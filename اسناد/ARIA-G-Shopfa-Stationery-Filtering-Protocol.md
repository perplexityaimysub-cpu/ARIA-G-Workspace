# **گزارش جامع مهندسی ناوبری چندوجهی (Faceted Navigation) و پروتکل طراحی فیلترهای نوشت‌افزار در پلتفرم شاپفا**

صنعت تجارت الکترونیک در سال‌های اخیر دستخوش تحولات ساختاری گسترده‌ای شده است؛ به طوری که بر اساس داده‌های آماری، کاربران بخش جستجو تنها ۲۶ درصد از کل ترافیک یک فروشگاه اینترنتی را تشکیل می‌دهند، اما سهمی معادل ۴۹ درصد از کل درآمدهای پلتفرم را به خود اختصاص می‌دهند1. این موضوع نشان‌دهنده نرخ تبدیل (Conversion Rate) بسیار بالای کاربران هدفمندی است که مستقیماً از سیستم‌های ناوبری چندوجهی استفاده می‌کنند1. با این حال، مواجهه کاربر با کاتالوگ‌های انبوه در فروشگاه‌های بزرگ بدون بهره‌گیری از یک فیلترینگ کارآمد، منجر به بروز پدیده «فلج انتخاب» (Choice Overload) و خروج فوری کاربر از سایت (Bounce Rate) به دلیل خستگی ناشی از پیمایش بیهوده (Scroll Fatigue) می‌شود3.  
این گزارش استراتژیک، با تمرکز بر پیاده‌سازی بهینه ناوبری چندوجهی در پلتفرم فروشگاه‌ساز شاپفا5، به تحلیل عمیق چالش‌های تجربه کاربری و مهندسی معکوس ساختارهای فیلترینگ پرداخته و نقشه راه فنی دقیقی را برای صنف نوشت‌افزار ارائه می‌کند.

## **۱. تبیین استراتژیک چالش‌های رابط و تجربه کاربری در فیلترینگ مقیاس‌بزرگ**

معماری اطلاعات (Information Architecture) در فروشگاه‌های نوشت‌افزار به دلیل تنوع بسیار بالای متغیرهای فنی از حساسیت بالایی برخوردار است7. برای مثال، یک محصول فانتزی مانند روان‌نویس کریتورز کلاس مدل Monet با قطر نوشتاری ![][image1] میلی‌متر7 نیازمند متغیرهایی کاملاً متفاوت با یک ابزار صنعتی مانند چسب پاتکس مدل پرمیوم10 یا یک ابزار ترسیم تخصصی مانند اتود طراحی ۵ میلی‌متری کوه نور11 است. به منظور مدیریت بهینه این تنوع کاتالوگی، رعایت اصول پنج‌گانه UI/UX فیلترینگ در پلتفرم شاپفا الزامی است5.

### **اصول پنج‌گانه طراحی فیلترهای تخصصی نوشت‌افزار:**

#### **اصل اول: اولویت‌بندی سلسله‌مراتبی (Hierarchical Priority)**

چیدمان فیلترها در ستون کناری باید دقیقاً منطبق بر مدل ذهنی خریدار و ترجیحات شناختی او در زمان خرید باشد3. در این صنف، سلسله‌مراتب تصمیم‌گیری خریدار و تقدم ویژگی‌ها بدین صورت تعریف می‌شود:  
![][image2]  
نمایش اطلاعات غیرضروری مانند «ابعاد بسته پستی» یا «طول بدنه» در ستون فیلترها یک خطای فاحش در طراحی تجربه کاربری است؛ زیرا این داده‌ها صرفاً باید در برگه مشخصات فنی کالا درج شوند و تاثیری در فیلترینگ اولیه ندارند13.

#### **اصل دوم: ادغام هوشمند فیلترها (Filter Consolidation)**

تعدد بی‌ضابطه مقادیر فیلتر، سیستم را به سمت نابودی کارایی هدایت می‌کند1. در سیستم مدیریت مشخصات شاپفا، از تعریف مقادیر هم‌پوشان و مترادف (نظیر «آبی آسمانی»، «آبی لایت»، «آبی روشن» برای خودکارها) باید به شدت اجتناب کرد1. تمامی این متغیرها باید تحت یک مقدار استاندارد واحد تحت عنوان «رنگ جوهر: آبی» نرمال‌سازی و ادغام شوند تا از قطعه‌قطعه شدن نتایج جلوگیری به عمل آید1.

#### **اصل سوم: بهره‌گیری از فیلترهای بصری (Visual Swatches)**

برای متغیرهای کیفی بصری مانند رنگ جوهر خودکار یا رنگ بدنه اتود، چک‌باکس‌های متنی خام کارایی بسیار پایینی دارند7. پلتفرم شاپفا از قابلیت تنوع کالای تصویری و استایل‌دار پشتیبانی می‌کند15؛ بنابراین باید ویژگی‌های رنگی به صورت دایره‌های رنگی بصری (Color Swatches) طراحی شوند تا کاربر بدون نیاز به خواندن متن، رنگ مورد نظر را انتخاب کند7.

#### **اصل دوم: سیستم آکاردئونی و بخش‌های تاشو (Collapsible Sections)**

مواجهه اولیه کاربر با صدها چک‌باکس فعال، منجر به تصمیم‌گریزی می‌شود3. هر گروه از فیلترها باید در قالب کادرهای آکاردئونی تاشو طراحی شوند3. سیستم به طور پیش‌فرض باید تنها عنوان فیلترها را نمایش داده و با کلیک کاربر، گزینه‌های داخلی آن را باز کند3.

#### **اصل پنجم: حذف گزینه‌های با نتیجه صفر (Zero-Result Prevention)**

به منظور ممانعت از بن‌بست‌های اطلاعاتی که عامل ترک ۶۹ درصد از کاربران وب‌سایت‌های فروشگاهی است16، سیستم باید تعداد دقیق موجودی هر متغیر را به صورت داینامیک محاسبه کرده و در صورت نبود کالا، آن گزینه را غیرفعال (Greyed-out) یا پنهان کند1.

## **۲. تحلیل تطبیقی و مهندسی معکوس ساختار فیلترینگ رقبا**

پایش عمیق ساختار ناوبری چندوجهی در سه بستر بزرگ تجارت الکترونیک کشور یعنی دیجی‌کالا، ترب و برایتو، الگوهای رفتاری و استانداردهای طراحی زیر را نمایان می‌سازد7.

### **تحلیل ستون کناری و ترتیب چیدمان فیلترها**

در پلتفرم‌های دیجی‌کالا و برایتو، فیلترها بر اساس منطق کاهش پله‌پهنه گزینه‌ها چیده شده‌اند7. در دسته‌بندی خودکار و روان‌نویس، ترتیب چیدمان از بالا به پایین شامل دسته‌بندی فرعی، برند، رنگ جوهر، قطر ساچمه نوک، جنس بدنه، نحوه استفاده (کلیکی/درب‌دار)، نوع نوک (ساچمه‌ای/نمدی/ژله‌ای)، قابلیت‌ها (مانند پاک‌شونده بودن) و رده سنی است7.  
رقبا به طور گسترده از فیلترهای آکاردئونی تاشو استفاده می‌کنند7. تعداد گزینه‌های پیش‌فرض به نمایش درآمده قبل از دکمه تعاملی «مشاهده بیشتر» (Show More) به صورت استاندارد **۵ گزینه پربازدید** است3. این امر بار شناختی صفحه را کنترل کرده و از طولانی شدن بیش از حد ستون کناری جلوگیری می‌کند3.

### **تحلیل فیلترهای بصری و تعاملی**

در زمینه فیلترینگ رنگ، دیجی‌کالا از دایره‌های رنگی تعاملی استفاده می‌کند که به طور مجزا برای رنگ جوهر و رنگ بدنه تعریف می‌شوند7. برای مشخصات فنی بازه‌ای (نظیر وزن چسب یا قیمت)، پلتفرم ترب از اسلایدرهای دوطرفه تعاملی استفاده می‌کند17.  
اما در صنف نوشت‌افزار، استفاده از اسلایدر عددی برای وزن یا حجم محصولاتی چون چسب ماتیکی ناکارآمد است؛ زیرا خریداران ترجیح می‌دهند چسب را بر اساس دسته‌بندی‌های استاندارد وزنی بازار (مانند ۸ گرم، ۲۱ گرم، ۳۶ گرم) فیلتر کنند3. از این رو، بازه‌های از پیش‌تعریف‌شده (چک‌باکس‌های بازه‌ای) برای وزن و حجم کارایی بهتری نسبت به اسلایدرهای پیوسته دارند3.

### **فیلترهای تخصصی صنف لوازم تحریر**

* **سایز مغزی اتود:** در دسته‌بندی اتودها، فیلتر «سایز مغزی» (نظیر ![][image3]، ![][image1]، ![][image4]، ![][image5]، ![][image6]، ![][image7] و ![][image8] میلی‌متر) حیاتی‌ترین فیلتر هدایت‌گر است؛ چرا که نوع مغزی مورد استفاده کاربر تعیین‌کننده کاربرد تحصیلی، اداری یا طراحی محصول است11.  
* **اتودهای تخصصی ۲ میلی‌متر به بالا:** برای اتودهای ضخیم طراحی (نظیر مدل‌های کوه نور یا استدلر تیکنیکو)11، علاوه بر سایز نوک، ویژگی‌های زیر اهمیت فیلترینگ دارند:  
  * درجه سختی نوک (طیف ![][image9] تا ![][image10] و قرارگیری ![][image11] و ![][image12] در مرکز تقاضا)11.  
  * وجود تراش درپوش (برای تیز کردن مغزی‌های ضخیم)24.  
  * فرم سطح مقطع بدنه (شش‌ضلعی برای جلوگیری از غلتیدن روی میز یا مثلثی ارگونومیک)8.  
  * کاربرد تخصصی (طراحی، مهندسی، خوش‌نویسی)9.  
* **چسب‌ها:** خریداران در درجه نخست چسب‌ها را بر اساس **«نوع چسب»** (ماتیکی، مایع، نواری، ۱۲۳، آکواریوم، آناروبیک) فیلتر می‌کنند10؛ زیرا ماهیت شیمیایی چسب مشخص‌کننده متریال هدف اتصال است10. فیلتر **«وزن یا حجم»** به عنوان فیلتر ثانویه برای انتخاب ابعاد فیزیکی بسته مصرفی به کار می‌رود3.

## **۳. پروتکل بصری‌سازی و استقرار تعاملی فیلترها در شاپفا**

شاپفا با برخورداری از سیستم مدیریت ویژگی‌های پیشرفته، امکان تعریف ساختارهای بصری متنوع را فراهم می‌سازد5. نقشه پیاده‌سازی فیلترها در شاپفا باید مشخصات تعاملی جدول زیر را به طور دقیق رعایت کند15:

| عنوان فیلتر (ویژگی) | فرم بصری در لایه فرانت‌اند (UI) | نوع تعامل کاربر (Interaction) | مکانیزم کنترل داده در شاپفا |
| ----: | ----: | ----: | ----: |
| **رنگ جوهر (خودکار/روان‌نویس)** | دایره‌های رنگی توپر (Color Swatches)7 | تک‌انتخابی یا چندانتخابی (Multi-select OR) | متصل به تنوع کالای استایل‌دار شاپفا15 |
| **رنگ بدنه (نوشت‌افزار فانتزی)** | دایره‌های رنگی حاشیه‌دار دوگانه | چندانتخابی با آیکون تیک داخلی | متصل به گالری تصاویر محصول شاپفا12 |
| **ضخامت نوک / نوشتار** | دکمه‌های حبابی مستطیلی افقی (Pills) | چندانتخابی ضربه‌ای | متغیرهای سیستمی فیلتر شاپفا5 |
| **محدوده قیمت** | اسلایدر دوطرفه قیمت تعاملی17 | کشیدن دستگیره‌ها (Drag & Drop) | فیلتر محصولات پیشرفته شاپفا5 |
| **بازه وزنی چسب‌ها** | چک‌باکس‌های بازه‌ای از پیش‌تعریف‌شده10 | تیک زدن ساده گزینه‌ها | متغیرهای ثابت محصول (Specifications)12 |
| **برند نوشت‌افزار** | لیست چک‌باکسی همراه با فیلد جستجوی زنده | تیک زدن \+ تایپ نام برند | متصل به ماژول برندهای شاپفا15 |

## **۴. لیست طلایی فیلترهای ستون کناری برای محصولات برند سی‌کلاس (C-Class)**

این بخش با تمرکز بر تنوع سبد محصولات سی‌کلاس و کریتورز کلاس (زیربرند فانتزی سی‌کلاس)7، به ارائه ساختار دقیق فیلترهای کناری به صورت مجزا می‌پردازد.

### **دسته‌بندی ۱: خودکار و روان‌نویس (نظیر مدل‌های کاندید، مورنو و موج سی‌کلاس)**

7

\[V\] نوع نوشت‌افزار (چک‌باکس متنی)  
    \[ \] خودکار معمولی  
    \[ \] روان‌نویس فانتزی  
    \[ \] روان‌نویس نوک‌نمدی (Fineliner) \[cite: 29, 30\]  
    \[ \] ژل‌پن رنگی \[cite: 7, 31\]

\[V\] رنگ جوهر (نمونه‌های بصری دایره‌ای)  
    (آبی)  (مشکی)  (قرمز)  (سبز)  (صورتی)  (بنفش) \[cite: 7, 32\]

\[V\] ضخامت نوشتار (دکمه‌های مستطیلی Pills)  
    ( 0.4 mm ) \[cite: 19\]   ( 0.5 mm ) \[cite: 7, 31\]   ( 0.7 mm ) \[cite: 7, 9\]   ( 1.0 mm ) \[cite: 33\]   ( 1.2 mm ) \[cite: 33\]

\[V\] نحوه استفاده (چک‌باکس)  
    \[ \] کلیکی (شستی‌دار)  
    \[ \] درب‌دار معمولی \[cite: 14\]

\[V\] ساختار و جنس بدنه (چک‌باکس)  
    \[ \] پلاستیک فشرده سبک \[cite: 19, 31\]  
    \[ \] دارای گریپ لاستیکی (نرم‌کننده محل قرارگیری انگشت) \[cite: 9, 34\]  
    \[ \] بدنه شفاف (نمایش‌دهنده میزان جوهر) \[cite: 14, 34\]

### **دسته‌بندی ۲: اتود و مداد مکانیکی (نظیر مدل‌های اکسپرت و مارشمالو سی‌کلاس)**

23

\[V\] سایز مغزی اتود (دکمه‌های مستطیلی Pills) \[cite: 8, 23\]  
    ( 0.3 mm ) \[cite: 21\]   ( 0.5 mm ) \[cite: 23, 35\]   ( 0.7 mm ) \[cite: 8, 23\]   ( 0.9 mm ) \[cite: 21, 35\]   ( 2.0 mm ) \[cite: 11, 25\]

\[V\] ساختار بدنه و ارگونومی (چک‌باکس) \[cite: 8, 35\]  
    \[ \] فلزی سنگین (طراحی و مهندسی) \[cite: 23, 24\]  
    \[ \] پلاستیکی فانتزی (دانش‌آموزی) \[cite: 23, 24\]  
    \[ \] بدنه دارای گریپ سیلیکونی \[cite: 25, 36\]

\[V\] فرم سطح مقطع بدنه (چک‌باکس) \[cite: 8, 35\]  
    \[ \] دایره‌ای کلاسیک \[cite: 24\]  
    \[ \] شش‌ضلعی ضدغلتش \[cite: 13\]  
    \[ \] مثلثی ارگونومیک \[cite: 21, 30\]

\[V\] ویژگی‌های حفاظتی و خاص (چک‌باکس) \[cite: 8\]  
    \[ \] نوک متحرک لرزش‌گیر (ضد شکستن نوک)  
    \[ \] نشانگر تنظیم درجه سختی نوک روی بدنه \[cite: 24\]  
    \[ \] پاک‌کن پیچی طویل در انتهای اتود \[cite: 24\]

### **دسته‌بندی ۳: انواع چسب‌ها (چسب‌های حرارتی، مایع و نواری سی‌کلاس)**

28

\[V\] نوع شیمیایی و ساختار چسب (چک‌باکس متنی) \[cite: 10, 28\]  
    \[ \] چسب ماتیکی (کاربرگ کاغذ)  
    \[ \] چسب مایع و ژله‌ای  
    \[ \] چسب نواری پهن و شیشه‌ای  
    \[ \] چسب حرارتی تفنگی

\[V\] بازه وزنی و ابعادی (چک‌باکس بازه‌ای) \[cite: 10, 28\]  
    \[ \] فوق‌العاده سبک (کمتر از ۱۰ گرم)  
    \[ \] اداری و مدرسه‌ای استاندارد (۱۰ تا ۴۰ گرم)  
    \[ \] صنعتی و بسته‌بندی بزرگ (بالای ۴۰ گرم)

\[V\] کاربری و سطوح هدف (چک‌باکس)  
    \[ \] کاغذ، مقوا و روزنامه  
    \[ \] پارچه، چرم و کفش  
    \[ \] سطوح سخت، فلز و سنگ

### **دسته‌بندی ۴: پاک‌کن و غلط‌گیر (نظیر غلط‌گیرهای نواری و پاک‌کن‌های سی‌کلاس)**

20

\[V\] نوع محصول (چک‌باکس متنی) \[cite: 20, 38\]  
    \[ \] لاک غلط‌گیر مایع (قلمی/پمپی) \[cite: 20, 38, 39\]  
    \[ \] لاک غلط‌گیر نواری (خشک) \[cite: 20, 38\]  
    \[ \] پاک‌کن جامد تحریر \[cite: 20, 40\]

\[V\] مدل عملکردی و ساختار محصول (چک‌باکس) \[cite: 38, 40\]  
    \[ \] غلط‌گیر دو سر تعاملی \[cite: 38\]  
    \[ \] پاک‌کن اتودی کاتری \[cite: 38, 40\]  
    \[ \] پاک‌کن برقی مخزن‌دار \[cite: 38, 40\]

\[V\] استانداردهای سلامت و زیست‌محیطی (چک‌باکس) \[cite: 20\]  
    \[ \] فاقد مواد سمی و PVC  
    \[ \] بدون غبار (Dust-Free با فیبرهای متراکم) \[cite: 20\]

## **۵. معماری فنی دیتابیس و مدل هم‌پوشانی ویژگی‌ها در شاپفا**

برای استقرار بدون نقص ناوبری چندوجهی بدون کاهش سرعت لود صفحات، ساختار جداول پایگاه داده شاپفا باید از الگوی توسعه‌یافته کاتالوگ محصول پیروی کند41.

                                  \+-----------------------+  
                                  |     Product (جدول)    |  
                                  \+-----------------------+  
                                  | \- id (PK)             |  
                                  | \- title               |  
                                  | \- category\_id (FK)    |  
                                  \+-----------------------+  
                                              | 1  
                                              |  
                                              | N  
\+-------------------------+      \+------------------------+      \+-------------------------+  
|     Attribute (جدول)    | 1    |  ProductAttributeValue | N    |   AttributeValue (جدول) |  
\+-------------------------+------|------------------------+------|-------------------------+  
| \- id (PK)               |      | \- product\_id (FK, PK)  |      | \- id (PK)               |  
| \- name (مثلا: رنگ جوهر)  |      | \- attribute\_id (FK, PK)|      | \- attribute\_id (FK)     |  
| \- display\_type (UI)     |      | \- value\_id (FK)        |      | \- value (مثلا: آبی)      |  
\+-------------------------+      \+------------------------+      \+-------------------------+

### **مکانیزم اعمال منطق بولی (AND / OR) در دیتابیس شاپفا**

وقتی کاربر چندین رنگ (آبی و مشکی) را از فیلتر رنگ انتخاب می‌کند، سیستم باید بین مقادیر یک ویژگی منطق OR را برقرار کند، اما با افزودن فیلتر ضخامت نوک (![][image1] میلی‌متر)، دیتابیس باید نتایج حاصله را با منطق AND تلاقی دهد3. عبارت پرس‌وجوی ساختاریافته (SQL Query) در موتور جستجوی شاپفا به صورت بهینه زیر پیاده‌سازی می‌شود:

SQL  
SELECT p.id, p.title  
FROM Product p  
\-- بررسی شرط اول: تطابق رنگ جوهر با مقادیر انتخابی (OR داخلی)  
WHERE p.id IN (  
    SELECT pav.product\_id   
    FROM ProductAttributeValue pav  
    JOIN AttributeValue av ON pav.value\_id \= av.id  
    WHERE av.attribute\_id \= 1 AND av.value IN ('آبی', 'مشکی')  
)  
\-- اعمال شرط دوم با عطف منطقی (AND بین متغیرهای مختلف)  
AND p.id IN (  
    SELECT pav.product\_id   
    FROM ProductAttributeValue pav  
    JOIN AttributeValue av ON pav.value\_id \= av.id  
    WHERE av.attribute\_id \= 2 AND av.value \= '0.5'  
);

این متدولوژی پرس‌وجو تضمین می‌کند که فرآیند فیلترینگ با سرعت بسیار بالا پردازش شده و به دلیل ساختار شاخص‌گذاری شده (Indexing) فیلدها در جداول واسط، بار سرور به حداقل برسد41.

## **۶. نتیجه‌گیری و توصیه‌های عملیاتی CRO برای شاپفا**

طراحی هوشمندانه ناوبری چندوجهی صرفاً یک ویژگی ظاهری برای وب‌سایت شاپفا نیست، بلکه یک موتور تولید درآمد است که با کاهش اصطکاک در فرآیند خرید، به طور مستقیم بر نرخ خروج و نرخ ثبت سفارش نهایی اثر می‌گذارد2. پیاده‌سازی استراتژیک این پلتفرم نیازمند اجرای گام‌به‌گام اقدامات زیر است43:

1. **مدیریت داینامیک عدم موجودی (Dynamic Out-of-Stock Styling):** در سیستم شاپفا، محصولاتی که فاقد موجودی در انبار هستند، نباید ویژگی‌های آن‌ها در فیلترینگ حذف شود؛ بلکه باید با کاهش شفافیت بصری (Opacity: 0.4) و نمایش غیرفعال به کاربر نشان داده شوند تا کاربر همچنان از وجود کالا مطلع باشد اما به صفحه نتایج خالی هدایت نشود1.  
2. **یکپارچه‌سازی کامل با سیستم چندقیمتی شاپفا:** متغیرهایی که تعیین‌کننده قیمت هستند (مانند رنگ‌های گران‌بها در ست‌های روان‌نویس فانتزی یا سایز مغزی اتود) باید مستقیماً با ماژول محصول متغیر شاپفا همگام‌سازی شوند تا تغییر فیلتر، قیمت واقعی آن تنوع کالا را در لحظه به خریدار نمایش دهد12.  
3. **پشتیبانی از جستجوی معنایی هوشمند و برچسب‌های محتوایی:** تلفیق فیلترهای ناوبری با سیستم جستجوی زنده (Autocomplete) به کاربر کمک می‌کند تا با تایپ عباراتی چون «خودکار کاندید آبی»، سیستم به طور خودکار فیلتر برند روی «سی‌کلاس»23، دسته‌بندی روی «خودکار»7 و فیلتر رنگ روی «آبی» را فعال کرده و کاربر را مستقیماً به نتایج هدف هدایت کند2.

#### **Cytowane prace**

1. Ecommerce Search Relevance: Fix Zero-Results & Boost Conversions \- RBMSoft, [https://rbmsoft.com/blogs/search-relevance-tuning-for-ecommerce/](https://rbmsoft.com/blogs/search-relevance-tuning-for-ecommerce/)  
2. Faceted Search: What Is It and Why Your E-Shop Needs It \- Luigi's Box, [https://www.luigisbox.com/blog/faceted-search/](https://www.luigisbox.com/blog/faceted-search/)  
3. Fixing E-Commerce Product Filters: 2026 UX Best Practices \- WISEPIM, [https://wisepim.com/blog/ecommerce-product-filters-ux-best-practices](https://wisepim.com/blog/ecommerce-product-filters-ux-best-practices)  
4. Advanced Search Filters for E-commerce Sites \- ConversionBox, [https://www.conversionbox.ai/blog/advanced-search-filters-ecommerce-navigation/](https://www.conversionbox.ai/blog/advanced-search-filters-ecommerce-navigation/)  
5. قیمت طراحی سایت فروشگاهی و هزینه ساخت فروشگاه اینترنتی \- فروشگاه ساز شاپفا, [https://shopfa.com/plans](https://shopfa.com/plans)  
6. صفر تا صد راه اندازی وب سایت فروشگاهی ✔️ \- آژانس ارتباطات خلاق رویانو, [https://royanow.ir/starting-a-shopping-site-from-scratch/](https://royanow.ir/starting-a-shopping-site-from-scratch/)  
7. خرید و قیمت خودکار و روان نویس کریتورز کلاس \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-pen/creators-class/](https://www.digikala.com/search/category-pen/creators-class/)  
8. خرید و قیمت مداد نوکی کرند \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-mechanical-pencils/crend/](https://www.digikala.com/search/category-mechanical-pencils/crend/)  
9. بهترین خودکار در بازار ایران کدام است؟ \- Digikala, [https://www.digikala.com/mag/the-best-pen-in-iran-market/](https://www.digikala.com/mag/the-best-pen-in-iran-market/)  
10. فروشگاه اینترنتی دیجی‌کالا, [https://www.digikala.com/product/dkp-10917607/](https://www.digikala.com/product/dkp-10917607/)  
11. خرید و قیمت نوک کوه نور \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-tip/koh-i-noor/](https://www.digikala.com/search/category-tip/koh-i-noor/)  
12. امکانات سایت فروشگاهی \[200 افزونه و ابزار کاربردی\] \- فروشگاه ساز شاپفا, [https://shopfa.com/features](https://shopfa.com/features)  
13. فروشگاه اینترنتی دیجی‌کالا, [https://www.digikala.com/product/dkp-82599/%D9%85%D8%AF%D8%A7%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%D9%81%D8%A7%D8%A8%D8%B1-%DA%A9%D8%A7%D8%B3%D8%AA%D9%84-%D9%85%D8%AF%D9%84-9000-%D8%A8%D8%A7-%D8%AF%D8%B1%D8%AC%D9%87-%D8%B3%D8%AE%D8%AA%DB%8C-%D9%86%D9%88%DA%A9-hb](https://www.digikala.com/product/dkp-82599/%D9%85%D8%AF%D8%A7%D8%AF-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%D9%81%D8%A7%D8%A8%D8%B1-%DA%A9%D8%A7%D8%B3%D8%AA%D9%84-%D9%85%D8%AF%D9%84-9000-%D8%A8%D8%A7-%D8%AF%D8%B1%D8%AC%D9%87-%D8%B3%D8%AE%D8%AA%DB%8C-%D9%86%D9%88%DA%A9-hb)  
14. خودکار بیک مدل کریستال لارج بسته 3 عددی \- Digikala, [https://www.digikala.com/product/dkp-1700953/%D8%AE%D9%88%D8%AF%DA%A9%D8%A7%D8%B1-%D8%A8%DB%8C%DA%A9-%D9%85%D8%AF%D9%84-%DA%A9%D8%B1%DB%8C%D8%B3%D8%AA%D8%A7%D9%84-%D9%84%D8%A7%D8%B1%D8%AC-%D8%A8%D8%B3%D8%AA%D9%87-3-%D8%B9%D8%AF%D8%AF%DB%8C](https://www.digikala.com/product/dkp-1700953/%D8%AE%D9%88%D8%AF%DA%A9%D8%A7%D8%B1-%D8%A8%DB%8C%DA%A9-%D9%85%D8%AF%D9%84-%DA%A9%D8%B1%DB%8C%D8%B3%D8%AA%D8%A7%D9%84-%D9%84%D8%A7%D8%B1%D8%AC-%D8%A8%D8%B3%D8%AA%D9%87-3-%D8%B9%D8%AF%D8%AF%DB%8C)  
15. شاپفا | shopfa.com \- آپارات, [https://www.aparat.com/shopfa.com](https://www.aparat.com/shopfa.com)  
16. The Ultimate Guide to Search UX Design: 9 Best Practices for Maximum User Success, [https://whatifdesign.co/feeds/blog/best-search-ux-design](https://whatifdesign.co/feeds/blog/best-search-ux-design)  
17. لیست قیمت مداد نوکی و اتود، ۱۹ تیر \- ترب, [https://torob.com/browse/3461/%D9%85%D8%AF%D8%A7%D8%AF-%D9%86%D9%88%DA%A9%DB%8C-%D9%88-%D8%A7%D8%AA%D9%88%D8%AF/](https://torob.com/browse/3461/%D9%85%D8%AF%D8%A7%D8%AF-%D9%86%D9%88%DA%A9%DB%8C-%D9%88-%D8%A7%D8%AA%D9%88%D8%AF/)  
18. رویه ثبت شفارش – تحریر استور | فروشگاه اینترنتی لوازم تحریر, [https://tahrir-store.ir/%D8%B1%D9%88%DB%8C%D9%87-%D8%AB%D8%A8%D8%AA-%D8%B4%D9%81%D8%A7%D8%B1%D8%B4/](https://tahrir-store.ir/%D8%B1%D9%88%DB%8C%D9%87-%D8%AB%D8%A8%D8%AA-%D8%B4%D9%81%D8%A7%D8%B1%D8%B4/)  
19. خودکار مدل پاک کن دار طرح حرارتی به همراه غلط گیر بسته 7 عددی \- Digikala, [https://www.digikala.com/product/dkp-18622948/%D8%AE%D9%88%D8%AF%DA%A9%D8%A7%D8%B1-%D9%85%D8%AF%D9%84-%D9%BE%D8%A7%DA%A9-%DA%A9%D9%86-%D8%AF%D8%A7%D8%B1-%D8%B7%D8%B1%D8%AD-%D8%AD%D8%B1%D8%A7%D8%B1%D8%AA%DB%8C-%D8%A8%D9%87-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D8%BA%D9%84%D8%B7-%DA%AF%DB%8C%D8%B1-%D8%A8%D8%B3%D8%AA%D9%87-7-%D8%B9%D8%AF%D8%AF%DB%8C](https://www.digikala.com/product/dkp-18622948/%D8%AE%D9%88%D8%AF%DA%A9%D8%A7%D8%B1-%D9%85%D8%AF%D9%84-%D9%BE%D8%A7%DA%A9-%DA%A9%D9%86-%D8%AF%D8%A7%D8%B1-%D8%B7%D8%B1%D8%AD-%D8%AD%D8%B1%D8%A7%D8%B1%D8%AA%DB%8C-%D8%A8%D9%87-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D8%BA%D9%84%D8%B7-%DA%AF%DB%8C%D8%B1-%D8%A8%D8%B3%D8%AA%D9%87-7-%D8%B9%D8%AF%D8%AF%DB%8C)  
20. خرید و قیمت پاک کن و غلط گیر پلیکان \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-cleaners/pelikan/](https://www.digikala.com/search/category-cleaners/pelikan/)  
21. مداد نوکی استدلر \- خرید مداد نوکی Staedtler با بهترین قیمت \- Digikala, [https://www.digikala.com/search/category-mechanical-pencils/staedtler/](https://www.digikala.com/search/category-mechanical-pencils/staedtler/)  
22. لیست قیمت چسب 123، ۱۷ تیر \- ترب, [https://torob.com/browse/4433/%DA%86%D8%B3%D8%A8-123/b/8415/derby-%D8%AF%D8%B1%D8%A8%DB%8C/](https://torob.com/browse/4433/%DA%86%D8%B3%D8%A8-123/b/8415/derby-%D8%AF%D8%B1%D8%A8%DB%8C/)  
23. مداد نوکی-خرید بهترین انواع مداد نوکی فلزی و فانتزی \- Digikala, [https://www.digikala.com/search/category-mechanical-pencils/](https://www.digikala.com/search/category-mechanical-pencils/)  
24. بهترین مداد نوکی؛ کدام مدل‌ ایرانی، خارجی یا فانتزی بهتر است؟ \- Digikala, [https://www.digikala.com/mag/the-best-mechanical-pencil/](https://www.digikala.com/mag/the-best-mechanical-pencil/)  
25. خرید و قیمت مداد نوکی پارسیکار \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-mechanical-pencils/parsikar/](https://www.digikala.com/search/category-mechanical-pencils/parsikar/)  
26. لیست قیمت چسب آناروبیک، ۱۸ تیر \- ترب, [https://torob.com/browse/4392/%DA%86%D8%B3%D8%A8-%D8%A7%D9%86%D8%A7%D8%B1%D9%88%D8%A8%DB%8C%DA%A9/](https://torob.com/browse/4392/%DA%86%D8%B3%D8%A8-%D8%A7%D9%86%D8%A7%D8%B1%D9%88%D8%A8%DB%8C%DA%A9/)  
27. لیست قیمت چسب آکواریوم، ۱۹ تیر \- ترب, [https://torob.com/browse/3722/%DA%86%D8%B3%D8%A8-%D8%A7%DA%A9%D9%88%D8%A7%D8%B1%DB%8C%D9%88%D9%85/](https://torob.com/browse/3722/%DA%86%D8%B3%D8%A8-%D8%A7%DA%A9%D9%88%D8%A7%D8%B1%DB%8C%D9%88%D9%85/)  
28. قیمت چسب و لوازم جانبی Not Detected شناسایی نشده امروز ۱۵ فروردین، صفحه ۴۷ | ترب, [https://torob.com/browse/448/%DA%86%D8%B3%D8%A8-%D9%88-%D9%84%D9%88%D8%A7%D8%B2%D9%85-%D8%AC%D8%A7%D9%86%D8%A8%DB%8C-glue/b/-1/not-detected-%D8%B4%D9%86%D8%A7%D8%B3%D8%A7%DB%8C%DB%8C-%D9%86%D8%B4%D8%AF%D9%87/?page=47](https://torob.com/browse/448/%DA%86%D8%B3%D8%A8-%D9%88-%D9%84%D9%88%D8%A7%D8%B2%D9%85-%D8%AC%D8%A7%D9%86%D8%A8%DB%8C-glue/b/-1/not-detected-%D8%B4%D9%86%D8%A7%D8%B3%D8%A7%DB%8C%DB%8C-%D9%86%D8%B4%D8%AF%D9%87/?page=47)  
29. خرید و قیمت پاک کن و غلط گیر سی بی اس \- فروشگاه اینترنتی دیجی کالا, [https://www.digikala.com/search/category-cleaners/cbs/](https://www.digikala.com/search/category-cleaners/cbs/)  
30. فروشگاه ساز شاپفا | رایگان و حرفه ای فروشگاه اینترنتی بسازید., [https://shopfa.com/](https://shopfa.com/)  
31. 5 سیستم فروشگاهی حرفه ای رایگان \- زرین پال, [https://www.zarinpal.com/blog/5-professional-free-shop-systems/](https://www.zarinpal.com/blog/5-professional-free-shop-systems/)  
32. آسان ترین آموزش ساخت فروشگاه اینترنتی و راه اندازی فروشگاه آنلاین در ۱۰ دقیقه, [https://janebi.com/mag/how-to-build-ecommerce-site](https://janebi.com/mag/how-to-build-ecommerce-site)  
33. یک سایت ساز خوب باید این 9 ویژگی را داشته باشد \- فروشگاه ساز شاپفا, [https://shopfa.com/read/guide-choosing-the-best-site-builder](https://shopfa.com/read/guide-choosing-the-best-site-builder)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABk0lEQVR4Xu2UPSiGURTHjzBREolSPrIoJbEomQwWJvmITVIyE7vBoGQxsFAWFjJIGZSBMilSFh+LQVKKEf//c+/13Pe4t9Q70fOvX+/7nHvOPee59zxHJNNf1Ai4A4/gAUyDYt8hojZwCubBABgHh2DMd3IqANegyT5XgzOwCoqcU0Tt4A18eixKpMgGMKts/eAddCq7FhPdgE2wIWmxQU2CPmVzlS4ouxb9dkGpXgiJlXQpm0t0BErUmq9fJ+Im3IwBvhrFNMY5KFdrvhi3DwbBCVgClTkeVqzkWH4mqgH3Fv6PiXFPYE5M0eti7qzOd6LyTVQPJiTtzhbwArZFdV6+ibRc3DNoVmtJZ8W6bkvMdxYSN+KGH6DH2lwixuriE6fRgI0b+HZeeK+kiWvFTBM2k3tr10RXEmgKHp9/ptxoGVyCKuck5qt/Ba32mfeyAoa+PURmxBQYHEHUBdgDw2BNTFUdOR4it+AAlHk2jivOth0xc47TZErix528TbeYwcjf4KyKqFDMfTC2Qq1lyvRf9QXOTk4ZV7dwaAAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABmklEQVR4Xu2UPShGURjHH0URJQYfpXxkshhYlAwyMDBJZDRYLCarxUiSMrAYLAYSsiivTZmUsigfkcGgFFl8/P8957zvOcc9L8O70P3Vr3vPc5/7nHPPfe4VSfmLjMFr+ABv4RQscRPy0AaP4T3cM+NEiuAFbDXjOngCV2CxTYrQDY9goxkfwnc4lM1waIYzQYyJr7AriIeswU84b8aTZrwPS22ShRcHg1gHfIFzQTyEE7DwkhnbiTKwwsSyrItugYudiFtRHlxz4XusMUeyLDrRrE2wsAiLsbBLi2hjnMKq4Fo+nkTrVYYX+HgZ+T5RPbwx8vwnpuEVXJDIDhRqIsJal3BLtHM9CjkR6YcfEtk+dlas6zZEv7MkGkS/v0fY7sTuRBuCHejRB8cTYlyZGx8RXbGdeEC0IOU5sQvkvazhwe3blFyLstAiPBdtXQsLPktu9bWiT8TPwzYAf13M24VlJuZxBnfgKFwVbe1OL0O76kD8ve8Vzd2GE/BNdNHVTo4Hn6YHDpvjb3+ohLlcFO9tkvg7TUn5T3wBByJSj/LOvfgAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABYklEQVR4Xu2UzytEURTHj2IhJCU/yoZsrCyIlKwoFqw0iL2NsvQXKGUjJULJQsrOSkmxVFZqapaDjTXFEt/vnLnmzpl3573FbOR96tPMfN/pnvfuO3dEUv4iS/AJvsIXuAYb/IIAq/ANnsJD45ZXV6AO5mB/8XcXvIf7sN4VBdiE3wGvvboCvXDDZHPwE46Z3Ic3eAK34bznOszDkVKpwsefNdkQ/BC94xAtolvW6WXc7gO44mW/sHjcZK7RDWwy1xyNcFTKt3cB7knE++UiXIwL+/SJDsYDbDPXqnELe2xImuGdVDbqhs9F+T0JfApOayS1bDQFB2zoqFUjvqdzidlmTlZo6s5ExziOGdGzU5VJuByRfZk8A6clujHPYWwjbt+FlEaSC+3ALOxwRaILvcNBL3McS4JG5BFewkV4JDraw2UVetqvYKvJya4kbMSnmRD9C+FnxYGLoV30PaWk/Bd+AAWIREKFdX7FAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABnUlEQVR4Xu2UPyiGURTGjzAISeRPlMioDBiUTN9gYZKI3SKr2I3KoAwmg5JNBiWDScqkSJH8WWyUoix4Hudezr3f9WX4Fnqf+vX2nnvfc+597rmvSKa/qAlwA+7BHZgB5XZCATWBNfAAtkBrOPytEnAOOt07PzwCq6DMT/pBbeACLIMKMC+ai/E8tYO5KDYCXkB/FLdi4h1RFzpcrEXUmRXRDQSaBsNRrAc8g8UobtUNnsAtaHaxKnAgWoxFA62DgSjmC+2DymjMi4t7l3QhutHnYp9iEiZjYitaQUuOQW005pUDb5IuxAUELvmBuBA/ZAKbJJZfjJ1TD86kyIV42Oy2R9DlYkOiuyxqIaoG7IJD0ebgPTqVRCGKnRUHfTNsSKJNjUpBtXlvBFei95CLCMRDnUzEaIGNj4laYwsvia5+3L2ze1/B1NcMI9rHLftfjveeFjT4SaIJeW9okRevBuNcBMUO3hPNmdQJ2BZdGf9b7KbeYIbIteh5WEto+SVYALNgMxrPE3czCEbd87c/VKpOtCC/LXSemTL9J30A4QdXNPWP94IAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABRklEQVR4Xu2UvytGURiAX0kRRQYMwmwxsJBJBgYm+QcMFovN6B9gkEkWmwwMyKLwL1gsykIGg1Ik5cfzdt7jO/fcm9v9roXuU0/f95737bzn1/eJVPxVWnAFt+JEDoN4gXd4ZHEmHXiJb/iJO8n0j4zjGfZbfIrvOPtdEaA76cNRfJZijbbFLW7N4kWLj7HZF8UMS/FG2kAn3rDYNzrHNhtLUU+jJuyyT2VTXKNVX5BFPY1iHsXdU3ucCCnTaBlvcB1bo1yKMo0UvZNr3MeeKJegbCNlCj8k5/iKNurFK3zAoWDsVtyD0BeYSV6jeXErbrB4WtyEqn5X/By6q0kbSzGGL7iLjVFO0QmfpLb6bnE70oX5B7BkdYfi/ggS6CX6lcXOBHX6qk4kefYTeI8HuICvuIedQc2voT/WEZzDAakdbUXFf+YLuJFLMsjfigEAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABhElEQVR4Xu2UPyhHURTHj1BESQwKKclikEQpNgMDmaSMUhaLgZh+i90gSkomKWXyZzD8drMUAwtCUoqBge/Xeff9znvvPsOvDPI+9el1zz3vnXffPe+KZPxFVuA7/IQ3cBZWRjLSaYK78BEewfbodIEaOA3LYR1cEy14CKtNno8WeA4XYSmcgvewyyY5ONlrxnx4XrTYhIn7yMFr2BiM3b07sCyIhWzCE1hlYkuihbZNLE49PBN9sF0577mDrSb2zQhclegbLIgW2ovFLd3wVZI5LMR7h03MSwncEk3ORaci8EG+VS8H8clYPEEbvIUXopudBr+Er5D7Grymws7bgM8SbRAfRRfiJ5uHD7AvNuejqEKD8Fj053N0ijYJX8AHu4rdlZdk173BHhML2YcNsRg3k23uGIdDUihcAQ/gKaz9IRbCDedSfdrO4fhFdKWOUdH9HAjGHaInw0yYYeAPGy9AP2C/ybsSPct4ZDl47HBfn+AcvITrok31KzTDseCakfEf+AJrRFkwTcaq4QAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABo0lEQVR4Xu2UvSvFURjHH6EIyUtKKTEoJS/ZxGZgUAZZyEJe/gFiMxgMSpIMShYsRimLW0pisLCIXKUMQhmUFL5f55x7n9/v3vNTNrrf+tTvPOc5L8/L74hk9Be1DQZAn2Ue7IJS7RShcrAMHsABqApOJ/UZ4go0Bzz8ol8czIICsAO2QI7ySWgfbIIVMRHlB6e9qgDnYB3kgh4xF42BwqRbUnT4jabAB+i0Y0Y0DXpBlnPS+s1BJeAU3IPa0JxXw2ABXIND0CWeGyk1gRdwC0bAMXgEExKx9gw0inFoA09g0o59YrqYNtZkTUyNOsArGFd+AdWrb27OVn0Ts9AnV/h30G5tRWIycgdqrC1SLDI3WQpPKLmImLpKa2OnxcSs7ba2hLgZf848ZXMHbShbWPxJL8R/UEqDzYDRkG1OjPOYsvVLsElcinXXuYPYFLoc32oBxWpcDS7BCShTdh7MLmO3ObVa26AdN4BnsChpGokGpoCREabiSFLfqxuwJ8FLce2QmAhYgjhYlYiXhTdnTvn88JbZwekf5dbXSZpIMsroH+oLvXZTOAcwcbkAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB0AAAAaCAYAAABLlle3AAABk0lEQVR4Xu2UvSuGURjGL0UxGHykTBIpGQw+JoPBwIDCZjQomchuUcomk0UGg1L+A4vBYFKMBotFDIpFPq7L/Zz3vd/TeR729/nVb3jv+5z3fNznfoCSeuGKPtFnukVbatMVdukZ/aTf9JIe0jHaDJv7luVus9zc78yIRTpPG2g7vYANbvKDHMP0ld7Rzign7mGbH4wTgSHYCRtdTDvTSaZdzLMMO8kJbKMxH/SatsWJwAbsDzwjsCs6QvpP92FzVuNEhnIak8sx8hdVvVqjnHavU7zD6hijG9P/LcQJT9i1Jyz6QLujnOqkeuXVU7HCeopQH88U/UJ6UZ1A44tM3VANXbCnHVpENTyATU4t+lc9FS+sZ2CU7tE+uk5PYTVLLfpXPdXDhfUMqKk9M7DTbEdxoXheq0zA2iW3VQId9Ib2utgOfaT9LhYoutpU+yXR9ekae7Lf4/SFblZGVNEG865WX69z/HNR1UEPZwX2APTc11B7feE1+xeqr9gAqi3kc/qaTWpiEVpgic7CTlNSUlKH/AA+d2U2y3A3EgAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAaCAYAAABGiCfwAAABoElEQVR4Xu2UvStHYRTHv4oiJJRSSl5SMhjIYJSBAYXNaBMLKWWxmKQkk5RMKH+CJIpiUiYTBgahFIPy8j333Jdzn3vvb6f7qU/97jnPc5/nOc+5PyDnv3BOn+gznadl8bRHOV2kB/TLV35vGr/pHq3y5yQYoyO0iNbQI+jEEjvI0A7d1CWtdnLb9IeuQd8XowN6omITG4buesDELIPQF265CTIKzR3TingKmIUmLV30HbrLxO7IMnTOhJtAlNtF/AAeO8he7JRWOjm5t0NoGaWcLg/0lfa4CWEd2Yvd0Xon10wfkbwvqUAfvaBtJh5DSuEu1g/tqrTFgvv6pPdGeZZNZDWVRx29RtTqssMN6AvTFit0X730jDa4CUs3XaEtdJru0w8kFwvu6412mrhFNrLqBi2lznNQqqWMeFrLC9J9afNCaukVbTIxKZV0VauJBfGsEgry53BDG91EgJRJyhUMkJZ9oXPhiIgTaJdKt1qkvAvQJkn7HELk6NIQk9DPQL6fKcQ/ZtmA3KGcKstbOuOPL4i8eJwOQcuak5Pzh/gFO5ZjaRrcBzcAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAaCAYAAAA9rOU8AAABlElEQVR4Xu2VvyuFURjHH6EsfotFyaJMlGwGA4PFgDIoq10h/4HZSBZlkdVfQFFKKTYWiUEUYfHz+/W8p3vuc957brpMzqc+4f2ec+5zzvucSySR+B2a4Arcge/wE+7BNTgIF+AmfM6y0ywb52SPKbgBb0THHYiOc3Ltc9jvJsTog4/wDLaZrANewDvYazKfOrgLX+GQyabhh+hm2k0WMCO6oy1YZTIuzA84gs0m83FFU/7u0wmvRE94wGQBq6LFzNlA9BkzjonhiuYrrymRsaBukxXB3XLXL6J94sNFuTiLmTCZZV5Kb2hbNFuU8OSLYB+wH/L6hX/zebl+cUXn9Qtf0YNo30QLIdwxq47JG1bvJuTg+oVjr+Fl5j18g62FoXH+ul9aRE9mzDwPiPUL+Wm/8GceLPREypxQ7EqTSq+0g59xCBtt4BN7RaTSV0S6RL+BJ23gwyM7ltKvqFa0GJ5ejGXRcUvmeTUcFf03MCv5J//NiIQ35hb2SOGq+xl3NsyJHg1wX8J1fJ/gupuQSCQS/5Ivnr6Av4TpjuoAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAaCAYAAABGiCfwAAABdklEQVR4Xu2UvytGYRTHv4pBfiWDRSmDMlHKIINsBguZ/A0Wgx9ZLAaDMgolE4M/QZLBwGQ1ycAgiWIgP75f597u85z33pv57X7q0/ve59znec8959wXqKgHmukz/Uk+N2h7dIfRQlfpMf1K1PedwG96RDuSPRFNdBt2kFyBHXJNe4L7QgboE72inS62D0t6iza4GMbpHbJAI92DbVhL1jyTsLju80zDYme0NQ4BC7Bgd7BWuoGsw+JzPoAsdghLPGKQPiI+dAq2Ia9MKvUJrIwqp+ce1vcRHyhiCcXZ9dEH1CaiNkzQS9ofrJfSBdtQlF3arw9Yr1N1rSQ0cP9C2S3STzrjYill/RqlFyie4gj9wAudRc7YIuvXK6zXeSiRTb/oOaVDwbWm84C2BWtlIy/U37JX5o9e1E7WGN1F/IRlJRSqzA3svFz0t6LS6BCvDg85p2902K2rvMuwIfFJR6QvdZ7pE2gq33Piobd0Prm/oqKiXvkFoKtjjPhIe2wAAAAASUVORK5CYII=>