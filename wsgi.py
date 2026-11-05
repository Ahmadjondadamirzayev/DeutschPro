import threading
import asyncio
from flask import Flask
import bot as telegram_bot_module

app = Flask(__name__)

@app.route('/')
def home():
    return "DeutschPro Bot is active!"

def start_bot():
    try:
        asyncio.run(telegram_bot_module.main())
    except Exception as e:
        print(f"Bot xatoligi: {e}")

# Gunicorn ishga tushishi bilan botni fonda yurgizamiz
bot_thread = threading.Thread(target=start_bot, daemon=True)
bot_thread.start()
