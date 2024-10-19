# 🍪 Cookie Clicker Automation 🎮  
**Automate your Cookie Clicker game with Selenium! This script clicks the cookie, saves your progress, and loads previous game sessions. It also lets you set a custom execution time for the script.**

**این اسکریپت بازی Cookie Clicker شما را با استفاده از Selenium اتوماتیک می‌کند! این برنامه کوکی‌ها را کلیک می‌کند، پیشرفت شما را ذخیره می‌کند و جلسه‌های قبلی بازی را بارگذاری می‌کند. همچنین می‌توانید زمان اجرای دلخواه برای این اسکریپت تنظیم کنید.**

---

## 🌟 Features | ویژگی‌ها

- **Auto-clicking the big cookie** 🔄  
  The script clicks the main cookie repeatedly until the specified time is reached.  
  **کلیک خودکار بر روی کوکی اصلی** 🔄  
  اسکریپت به‌طور مکرر کوکی اصلی را تا زمان تعیین‌شده کلیک می‌کند.

- **Save and load game progress** 💾  
  It allows you to save your game progress and load it from a file.  
  **ذخیره و بارگذاری پیشرفت بازی** 💾  
  امکان ذخیره پیشرفت بازی و بارگذاری آن از یک فایل را فراهم می‌کند.

- **Set custom execution time** ⏱️  
  You can define how long the script should run by specifying the duration in minutes.  
  **تنظیم زمان اجرای دلخواه** ⏱️  
  شما می‌توانید مدت زمان اجرای اسکریپت را با وارد کردن زمان به دقیقه تعیین کنید.

---

## 🛠️ Installation | نصب

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/cookie-clicker-automation.git
   ```

2. **Install dependencies**  
   In the project directory, run:  
   ```bash
   pip install -r requirements.txt
   
   ``` 
---

## 🚀 How to Run | نحوه اجرا

1. **Run the script**  
   Execute the Python script to start automating Cookie Clicker:  
   ```bash
   python cookie_clicker.py
   ```
   
2. **Set execution time**  
   A prompt will appear asking you how long you'd like the script to run. Input the time in minutes (default is 1 minute).
   
   **تنظیم زمان اجرا**  
   یک پیغام ظاهر می‌شود که از شما می‌خواهد مدت زمان اجرای اسکریپت را وارد کنید. زمان را به دقیقه وارد کنید (پیش‌فرض 1 دقیقه است).

4. **Save or load game**  
   The script will attempt to load a saved game if a `recovery.txt` file exists. Otherwise, it will create a new game and save the recovery code.
   
   **ذخیره یا بارگذاری بازی**  
   اسکریپت تلاش می‌کند تا اگر فایل `recovery.txt` وجود دارد بازی ذخیره‌شده را بارگذاری کند. در غیر این صورت، بازی جدید ایجاد می‌شود و کد بازیابی ذخیره می‌شود.

---

## 🔧 Project Structure | ساختار پروژه

```bash
cookie-clicker-automation/
├── cookieclicker_Selenium.py        # Main Python script to run the automation
├── requirements.txt         # Required dependencies
├── recovery.txt             # Stores the game recovery code
└── README.md                # Project documentation
```
---

## 📄 License | لایسنس

This project is licensed under the MIT License.  
**این پروژه تحت لایسنس MIT منتشر شده است.**

---
