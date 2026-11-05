"""
Nemis Tili Duden Grammatika, Goethe-Institut (A1-C2), Lug'at va Worthub Sayti Boti
Muallif: Antigravity AI
Tavsif: Duden qoidalari asosida A1 dan C1 gacha darslar,
Goethe-Institut A1 dan C2 gacha imtihon testlari,
A1 dan C2 gacha Lug'at (Vocabulary) va worthub.vercel.app rasmiy veb-sayti integratsiyasi.
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
from data.manager import (
    get_topics_by_level,
    get_topic_by_id,
    search_topics,
    ALL_TOPICS
)
from data.vocabulary import (
    get_words_by_level,
    get_random_word
)
from quiz_manager import (
    start_topic_quiz,
    start_random_quiz,
    start_goethe_quiz,
    start_goethe_einstufung,
    start_vocab_quiz,
    start_fixing_mistakes,
    get_current_session,
    record_answer,
    advance_question
)
from keyboards import (
    get_main_reply_keyboard,
    get_levels_inline_keyboard,
    get_goethe_levels_inline_keyboard,
    get_vocab_levels_inline_keyboard,
    get_worthub_inline_keyboard,
    get_topics_keyboard,
    get_topic_detail_keyboard,
    get_active_quiz_keyboard,
    get_answer_result_keyboard,
    get_quiz_summary_keyboard,
    get_search_results_keyboard
)

# Log sozlamalari
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("GermanDudenBot")

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


# ==========================================
# RENDER UCHUN FLASK WEB SERVER (PORT OCHISH)
# ==========================================
app = Flask(__name__)

@app.route('/')
def home():
    return "DeutschPro Bot is running and active!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


# ==========================================
# ASOSIY BUYRUQLAR VA MENYU
# ==========================================

@dp.message(CommandStart())
async def cmd_start(message: Message):
    """Start buyrug'i"""
    first_name = message.from_user.first_name if message.from_user else "O'quvchi"
    text = (
        f"🇩🇪 <b>Salom, {first_name}! Nemis tili Duden, Goethe & Worthub Botiga xush kelibsiz!</b>\n\n"
        "🤔 <b>Qaysi grammatika yoki mavzuda qiynalyapsiz?</b>\n"
        "Menga shunchaki mavzu nomini yozing (masalan: <i>akkusativ, weil, perfekt, passiv, genitiv, modal fe'l</i>) "
        "yoki quyidagi bo'limlardan birini tanlang:\n\n"
        "📚 <b>Duden Grammatikasi (A1 - C1):</b> Nazariya, misollar va eslab qolish sirlari\n"
        "🎓 <b>Gyote Testlari (A1 - C2):</b> Xalqaro Goethe-Zertifikat imtihonlari va darajani aniqlash testi\n"
        "📖 <b>Lug'at & So'zlar (A1 - C2):</b> Artiklli so'zlar, tarjimalar, misollar va so'z testlari\n"
        f"🌐 <b>Bizning Saytimiz:</b> <a href='{config.WEBSITE_URL}'>worthub.vercel.app</a>\n"
        "🛠 <b>Xatolarni To'g'rilash:</b> Har bir test yakunida faqat adashgan savollaringiz ustida ishlash imkoniyati!"
    )
    await message.answer(
        text,
        reply_markup=get_main_reply_keyboard(),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )
    await message.answer(
        "👇 <b>Kerakli bo'limni tanlang:</b>",
        reply_markup=get_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )


@dp.message(F.text == "📚 Grammatika Darajalari (A1-C1)")
@dp.message(Command("levels"))
async def show_levels_menu(message: Message):
    await message.answer(
        "📚 <b>Duden qoidalari bo'yicha grammatika darajangizni tanlang:</b>\n\n"
        "🟢 <b>A1</b> — Boshlang'ich (Artikllar, Jins & Ko'plik, Präsens, Wortstellung)\n"
        "🔵 <b>A2</b> — Elementar (Perfekt haben/sein, Wechselpräpositionen, ADUSO)\n"
        "🟡 <b>B1</b> — O'rta (Konjunktiv II, Relativsätze, Genitiv, um...zu)\n"
        "🟠 <b>B2</b> — O'rtadan yuqori (Passiv o'rinbosarlari, N-Deklination, FVG)\n"
        "🔴 <b>C1</b> — Mukammal (Konjunktiv I, Gerundivum, Nominalisierung)",
        reply_markup=get_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )


@dp.message(F.text == "🎓 Gyote Testlari (A1-C2)")
@dp.message(Command("goethe"))
async def show_goethe_menu(message: Message):
    """Goethe imtihonlari bosh menyusi"""
    text = (
        "🏛 <b>GOETHE-INSTITUT (GYOTE INSTITUTI) IMTIHON TESTLARI (A1 - C2)</b>\n\n"
        "Gyote instituti xalqaro sertifikat imtihonlarining haqiqiy <i>Sprachbausteine</i>, "
        "<i>Lesen</i> va <i>Grammatik im Kontext</i> formatidagi topshiriqlari!\n\n"
        "🟢 <b>Goethe A1</b> — Start Deutsch 1\n"
        "🔵 <b>Goethe A2</b> — Fit in Deutsch / A2\n"
        "🟡 <b>Goethe B1</b> — Goethe-Zertifikat B1\n"
        "🟠 <b>Goethe B2</b> — Goethe-Zertifikat B2\n"
        "🔴 <b>Goethe C1</b> — Goethe-Zertifikat C1\n"
        "🟣 <b>Goethe C2</b> — Großes Deutsches Sprachdiplom (GDS Diplom)\n"
        "🏆 <b>Daraja Aniqlovchi Test</b> — A1 dan C2 gacha aralash sinov\n\n"
        "👇 <b>Kerakli imtihon darajasini tanlang:</b>"
    )
    await message.answer(
        text,
        reply_markup=get_goethe_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )


@dp.message(F.text == "📖 Lug'at & So'zlar (A1-C2)")
@dp.message(Command("vocab"))
async def show_vocab_menu(message: Message):
    """Lug'at bo'limi bosh menyusi"""
    text = (
        "📖 <b>NEMIS TILI LUG'AT & SO'ZLAR BO'LIMI (A1 - C2)</b>\n\n"
        "Har bir so'z artikli, ko'plik shakli, o'zbekcha tarjimasi va jonli misollar bilan berilgan.\n\n"
        "🟢 <b>A1</b> — Asosiy kundalik so'zlar (Oila, Uy, Oziq-ovqat, Transport)\n"
        "🔵 <b>A2</b> — Sayohat, Shahar, Ta'til va Salomatlik\n"
        "🟡 <b>B1</b> — Munosabatlar, Ishga ariza, Ta'lim va Jamiyat\n"
        "🟠 <b>B2</b> — Biznes, Texnika, Barqarorlik va Huquq\n"
        "🔴 <b>C1</b> — Ilmiy tadqiqot, Notiqlik, Falsafa va Mantiq\n"
        "🟣 <b>C2</b> — Mumtoz adabiyot, Elita, Idiomalar va Oliy uslub\n\n"
        "👇 <b>Kerakli darajani tanlang yoki so'z testi ishlang:</b>"
    )
    await message.answer(
        text,
        reply_markup=get_vocab_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )


@dp.message(F.text == "🌐 Worthub Saytimiz")
@dp.message(Command("site"))
@dp.message(Command("worthub"))
async def show_worthub_info(message: Message):
    """Worthub.vercel.app sayti haqida ma'lumot va ulanish"""
    text = (
        "🌐 <b>BIZNING RASMIY SAYTIMIZ: WORTHUB</b>\n\n"
        f"🔗 <b>Sayt manzili:</b> <a href='{config.WEBSITE_URL}'>{config.WEBSITE_URL}</a>\n\n"
        "Platformamiz orqali nemis tili, foydali materiallar, loyihalar va ta'lim vositalaridan "
        "to'liq va qulay foydalanishingiz mumkin.\n\n"
        "<i>Quyidagi tugmalar orqali saytni to'g'ridan-to'g'ri Telegram ichida (Web App) yoki "
        "brauzeringizda ochishingiz mumkin:</i>"
    )
    await message.answer(
        text,
        reply_markup=get_worthub_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )


@dp.message(F.text == "🔍 Mavzu Qidirish")
@dp.message(Command("search"))
async def prompt_search(message: Message):
    await message.answer(
        "🔍 <b>Mavzu qidirish:</b>\n\n"
        "O'zingiz tushunmayotgan yoki qiynalayotgan har qanday mavzu nomini yozing.\n"
        "<i>Masalan: akkusativ, weil, modal fe'llar, konjunktiv, passiv, genitiv</i>\n\n"
        "Men darhol kerakli darslikni topib beraman!",
        parse_mode=ParseMode.HTML
    )


@dp.message(F.text == "ℹ️ Duden Standarti Haqida")
@dp.message(Command("help"))
async def show_help(message: Message):
    text = (
        "🇩🇪 <b>DUDEN, GOETHE & WORTHUB PLATFORMASI HAQIDA</b>\n\n"
        "🎯 <b>Duden nima?</b>\n"
        "Duden — Germaniyaning eng oliy davlat grammatik me'yoridir.\n\n"
        "🏛 <b>Goethe-Institut nima?</b>\n"
        "Xalqaro miqyosda tan olingan A1-C2 sertifikat imtihonlari standarti.\n\n"
        "📖 <b>Lug'at bo'limi:</b>\n"
        "Har bir so'z artikl, ko'plik va misollar bilan mnemotexnik yodlatiladi.\n\n"
        f"🌐 <b>Rasmiy Veb-Sayt:</b> <a href='{config.WEBSITE_URL}'>worthub.vercel.app</a>"
    )
    await message.answer(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@dp.message(F.text == "🎲 Tasodifiy Test")
async def send_random_test_cmd(message: Message):
    """Tasodifiy aralash test boshlash"""
    user_id = message.from_user.id
    session = start_random_quiz(user_id, count=5)
    if not session or not session.get("questions"):
        await message.answer("Savollar topilmadi.")
        return

    q = session["questions"][0]
    topic_title = q.get("topic_title", "Aralash Test")
    text = (
        f"🎲 <b>Aralash Duden Mashqi (1/{len(session['questions'])})</b>\n"
        f"📌 <i>Mavzu: {topic_title}</i>\n\n"
        f"❓ <b>Savol:</b>\n{q['question']}\n\n"
        "<i>To'g'ri variantni tanlang:</i>"
    )
    await message.answer(
        text,
        reply_markup=get_active_quiz_keyboard(q["options"], "random"),
        parse_mode=ParseMode.HTML
    )


# ==========================================
# CALLBACK QUERY (TUGMALAR) HANDLERLARI
# ==========================================

@dp.callback_query(F.data == "menu:main")
async def cb_main_menu(call: CallbackQuery):
    await call.message.edit_text(
        "📚 <b>Grammatika darajalaridan birini tanlang yoki qidirmoqchi bo'lgan mavzuni yozing:</b>",
        reply_markup=get_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await call.answer()


@dp.callback_query(F.data == "levels:menu")
async def cb_levels_menu(call: CallbackQuery):
    await call.message.edit_text(
        "📚 <b>Duden qoidalari bo'yicha darajani tanlang:</b>",
        reply_markup=get_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await call.answer()


@dp.callback_query(F.data == "goethe:menu")
async def cb_goethe_menu(call: CallbackQuery):
    """Gyote testlari darajalar menyusi"""
    text = (
        "🏛 <b>GOETHE-INSTITUT (GYOTE INSTITUTI) IMTIHON TESTLARI (A1 - C2)</b>\n\n"
        "Kerakli imtihon darajasini tanlang va xalqaro Goethe-Zertifikat "
        "formatidagi topshiriqlarni yeching:"
    )
    await call.message.edit_text(
        text,
        reply_markup=get_goethe_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await call.answer()


@dp.callback_query(F.data == "vocab:menu")
async def cb_vocab_menu(call: CallbackQuery):
    """Lug'at bo'limi menyusi"""
    text = (
        "📖 <b>NEMIS TILI LUG'AT & SO'ZLAR BO'LIMI (A1 - C2)</b>\n\n"
        "Darajani tanlang va nemischa so'zlarni artikli, ko'pligi va jonli misollari bilan o'rganing:"
    )
    await call.message.edit_text(
        text,
        reply_markup=get_vocab_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await call.answer()


@dp.callback_query(F.data.startswith("vocab:list:"))
async def cb_vocab_list(call: CallbackQuery):
    """Muayyan darajadagi so'zlar ro'yxatini ko'rsatish"""
    level = call.data.split(":")[2]
    words = get_words_by_level(level)

    if not words:
        await call.answer("So'zlar topilmadi.", show_alert=True)
        return

    text_parts = [f"📖 <b>{level} DARAJASI ASOSIY SO'ZLARI:</b>\n"]
    for i, w in enumerate(words, 1):
        plural_info = f" ({w.get('plural')})" if w.get("plural") and w.get("plural") != "-" else ""
        text_parts.append(
            f"<b>{i}. {w['word']}{plural_info}</b> — {w['translation']}\n"
            f"   💡 <i>\"{w['example']}\"</i>\n"
            f"   🇺🇿 <i>{w['example_uz']}</i>\n"
        )

    text = "\n".join(text_parts)
    await call.message.edit_text(
        text,
        reply_markup=get_vocab_levels_inline_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await call.answer()


@dp.callback_query(F.data == "vocab:card:random")
async def cb_vocab_card_random(call: CallbackQuery):
    """Tasodifiy bitta so'z kartochkasini chiqarish"""
    w = get_random_word()
    if not w:
        await call.answer("So'z topilmadi.")
        return

    plural_info = f" ({w
