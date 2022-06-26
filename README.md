# Book-Review

پیاده سازی سیستم نظر دهی کتاب :

قصدمون پیاده سازی یک سیستم ساده برای ثبت کتاب و ثبت نظر درمورد کتاب هاست

من میخوام داخل سیستمم یه سری کتاب ثبت کنم و کاربر ها وارد بشن و برای کتاب ها نظر بذارن

  ● می تونیم اینجا تعیین کنیم که کتاب ها و کاربر ها چه اطالعاتی ازشون توی سیستم ثبت میشه ولی قصدمون اینه که توانایی
  شما در تشخیص نیازمندی سنجیده بشه

  ● ترجیح ما اینه که حتما از REST استفاده بشه

کاربرد های زیر مد نظره :

  ● کاربر ادمین بتونه کتاب ثبت کنه (از طریق ادمین جنگو مد نظر نیست و اضافه بر اون باید قابلیتش موجود باشه)

  ● ثبت نام و لاگین (وجود قابلیت هایی مثه لاگین با گوگل اجباری نیست ولی اگر باشه خوبه)

  ● فقط ادمین بتونه کتاب هارو حذف کنه یا تغییر بده

  ● هر کاربر بتونه لیست کتاب هارو ببینه . کتاب های دسته بندی مختلف دارن
  باید بتونه بر اساس دسته یا نویسنده ببینه

  ● قابلیت سرچ کتاب

  ● بتونه برای هر کتاب کامنت بذاره . قابلیت مرتب کردن کامنت ها بر اساس زمان ثبت هم نیازه

  ● داخل کامنت باید قابلیت این باشه که کاربر ثبت کنه از چه تاریخی تا چه تاریخی داشته کتاب رو میخونده . مدت زمان هم
  نمایش داده بشه خوبه

  ● برای هر کامنت نشون داده بشه که چند ساعت پیش ثبت شده

  ● هر کاربر بتونه کتاب هارو لایک کنه و بتونه لیست کتاب هایی که لایک کرده ببینه

  ● بتونیم برای هر کتاب لیست کسایی که کتاب رو لایک کردن بببنیم (و همینطور تعدادشون)

  ● هر کاربر باید یک wishlist از کتاب ها داشته باشه و فقط خودش یا ادمین بتونه این لیست رو ببینه یا تغییر بده

  ● نکات امنیتی در نظر گرفته بشه مثال کاربر عادی نتونه لیست همه ی کاربرا رو ببینه و از این قبیل نکات

  ● استفاده از کش امتیاز مثبت داره (نیاز به وقت گذاشتن زیاد روی این بخش نیست در ساده ترین حالت ممکن کافیه)

دقت کنین که نیاز به طراحی هیچ UI برای این پروژه نیست . صرفا میخوایم دیتایی که رد و بدل میشه رو بررسی کنیم
از دیتابیس sqlite استفاده بشه مشکلی نداره که این دیتابیس رو به صورت