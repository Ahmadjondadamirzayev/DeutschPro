import threading
import asyncio
import os
from flask import Flask

# Flask veb-serverini yaratamiz (Render port talabini qondirish uchun)
app = Flask(__name__)

@app.route('/')
def home():
    return "DeutschPro Bot is running and active!"

# Telegram botni alohida fon oqimida (background thread) ishga tushiramiz
def run_telegram_bot():
    import bot
    try:
        asyncio.run(bot.main())
    except Exception as e:
        print(f"Bot xatoligi: {e}")

# Gunicorn ishga tushishi bilan veb-server yonadi va botni fonda yoqadi
threading.Thread(target=run_telegram_bot, daemon=True).start()
