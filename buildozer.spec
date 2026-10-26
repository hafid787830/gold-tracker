[app]

# عنوان التطبيق
title = Gold Price Tracker

# اسم الحزمة (Package name)
package.name = goldtracker

# نطاق الحزمة (Package domain)
package.domain = org.goldtracker

# الملفات المشمولة في التطبيق (تأكد من شمل ملف JSON الخاص بالبيانات)
source.include_exts = py,png,jpg,kv,atlas,json

# نقطة بداية التطبيق (ملف البايثون الرئيسي)
source.main = main.py

# الإصدار
version = 0.1

# المتطلبات البرمجية للتطبيق (مكتبة بايثون الأساسية، وkivy، ومكتبات قراءة البيانات)
requirements = python3,kivy,pyjnius

# إذن الوصول للإنترنت (مهم في حال كان التطبيق يجلب أسعار الذهب عبر الإنترنت)
android.permissions = INTERNET

# اتجاه الشاشة (عمودي)
orientation = portrait

# إعدادات أندرويد (تحديث SDK والـ API لتجنب التحذيرات القديمة)
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]

# مستوى تسجيل الأخطاء (0 = صامت، 2 = تفصيلي للتصحيح)
log_level = 2

# وضع التحذير عند استخدام الجذر
warn_on_root = 1
