import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

class Config:
    # إعدادات قاعدة البيانات
    DB_PATH = os.getenv("DB_PATH", "data/finance_tracker.db")
    
    # إعدادات API لبيانات الأسهم
    ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
    
    # إعدادات Telegram للتنبيهات
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    # إعدادات أخرى
    CACHE_EXPIRATION = int(os.getenv("CACHE_EXPIRATION", 3600))  # ثانية (ساعة واحدة)
    TIMEZONE = os.getenv("TIMEZONE", "Asia/Riyadh")
    
    # مسارات الملفات
    LOG_DIR = "logs"
    DATA_DIR = "data"
    
    @classmethod
    def validate(cls):
        """التحقق من صحة الإعدادات الأساسية"""
        required_keys = [
            'ALPHA_VANTAGE_API_KEY',
            'FINNHUB_API_KEY'
        ]
        
        missing = [key for key in required_keys if not getattr(cls, key)]
        if missing:
            raise ValueError(f"مفاتيح API مفقودة في ملف البيئة: {', '.join(missing)}")

# إنشاء المجلدات إذا لم تكن موجودة
os.makedirs(Config.LOG_DIR, exist_ok=True)
os.makedirs(Config.DATA_DIR, exist_ok=True)

# التحقق من الإعدادات عند استيراد الملف
try:
    Config.validate()
except ValueError as e:
    print(f"تحذير: {e}")
