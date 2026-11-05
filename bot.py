"""
Nemis Tili Duden Grammatika, Goethe-Institut (A1-C2), Lug'at va Worthub Sayti Boti
Muallif: Antigravity AI
...
"""
import asyncio
import logging
import sys
import os
import threading
from flask import Flask

# Windows konsolida UTF-8 simvollarini to'g'ri ko'rsatish
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import config
# ... (qolgan importlar va bot = Bot(...) / dp = Dispatcher() qismlari)
