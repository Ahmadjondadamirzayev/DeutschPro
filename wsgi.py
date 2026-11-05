import threading
import asyncio
from flask import Flask
import bot as telegram_bot_module

app = Flask(__name__)

@app.route('/')
def home():
    return "DeutschPro Bot is active!"

# Botni fonda xatosiz ishga tushirish
def start_bot():
    try:
        asyncio.run(telegram_bot_module.main())
    except Exception as e:
        print(f"Bot xatoligi: {e}")

# Gunicorn yonishi bilan bot fonda ishlay boshlaydi
threading.Thread(target=start_bot, daemon=True).start()
