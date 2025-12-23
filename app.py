# app.py
from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

# Route اصلی - صفحه HTML
@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✅ سرور فعال در کلود</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }
        h1 {
            color: #4CAF50;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
        }
        .info-box {
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
            border-right: 5px solid #4CAF50;
        }
        .url-box {
            background: rgba(0, 0, 0, 0.3);
            padding: 12px;
            font-family: monospace;
            word-break: break-all;
            border-radius: 5px;
            margin: 10px 0;
        }
        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }
        button:hover {
            background: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 سرور شما با موفقیت راه‌اندازی شد!</h1>
        
        <div class="info-box">
            <h3>📡 وضعیت سرور:</h3>
            <p><strong>✅ آنلاین و فعال</strong></p>
            <p>زمان راه‌اندازی: ''' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '''</p>
            <p>پورت: <strong>3000</strong></p>
        </div>
        
        <div class="info-box">
            <h3>🌍 دسترسی عمومی:</h3>
            <p>این سرور اکنون یک <strong>IP عمومی واقعی</strong> دارد:</p>
            <div class="url-box" id="currentUrl">در حال دریافت...</div>
            <p>✅ این آدرس از هر نقطه از جهان (حتی موبایل با اینترنت سیمکارت) قابل دسترسی است.</p>
            <button onclick="copyUrl()">📋 کپی آدرس</button>
        </div>
        
        <div class="info-box">
            <h3>🛠️ امکانات سرور:</h3>
            <ul>
                <li><a href="/api/status" style="color:#4CAF50;">/api/status</a> - وضعیت JSON سرور</li>
                <li><a href="/api/time" style="color:#4CAF50;">/api/time</a> - زمان سرور</li>
                <li>پورت 3000 برای دسترسی عمومی باز است</li>
                <li>قابل توسعه برای API، وبسایت، ربات و...</li>
            </ul>
        </div>
        
        <div class="info-box">
            <h3>📝 راهنمای تست:</h3>
            <ol>
                <li>این آدرس را در مرورگر دیگری باز کنید</li>
                <li>با موبایل (اینترنت سیمکارت) تست کنید</li>
                <li>برای دوستان خود بفرستید تا تأیید کنند</li>
            </ol>
        </div>
    </div>
    
    <script>
        // نمایش آدرس فعلی
        document.getElementById('currentUrl').textContent = window.location.origin;
        
        // تابع کپی کردن آدرس
        function copyUrl() {
            const url = window.location.origin;
            navigator.clipboard.writeText(url).then(() => {
                alert('آدرس کپی شد: ' + url);
            });
        }
        
        // تست دسترسی به API
        fetch('/api/status')
            .then(response => response.json())
            .then(data => console.log('API Status:', data));
    </script>
</body>
</html>
'''

# Route برای API وضعیت
@app.route('/api/status')
def api_status():
    return jsonify({
        "status": "online",
        "service": "Cloud Server",
        "platform": "Gitpod/Ona",
        "timestamp": datetime.datetime.now().isoformat(),
        "endpoints": ["/", "/api/status", "/api/time"]
    })

# Route برای دریافت زمان سرور
@app.route('/api/time')
def api_time():
    return jsonify({
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "UTC"
    })

# Route تستی برای نمایش پارامتر
@app.route('/api/hello/<name>')
def hello_name(name):
    return jsonify({
        "message": f"سلام {name}!",
        "received_at": datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    # اجرای سرور روی همه آدرس‌ها و پورت 3000
    print("=" * 60)
    print("🚀 سرور در حال راه‌اندازی...")
    print("📡 در حال گوش دادن روی: 0.0.0.0:3000")
    print("🌍 دسترسی عمومی: پورت 3000 را Public کنید")
    print("=" * 60)
    
    app.run(
        host='0.0.0.0',  # گوش دادن به همه آدرس‌ها
        port=3000,        # پورت اصلی
        debug=True,       # حالت دیباگ (در تولید False کنید)
        threaded=True     # پشتیبانی از چندین درخواست
    )
