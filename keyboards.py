"""
Telegram Inline va Reply Klaviaturasi
Duden grammatikasi, Goethe-Institut testlari, Lug'at (Vocabulary) va Worthub.vercel.app veb-sayti bilan.
"""
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
from typing import List, Dict
import config


def get_main_reply_keyboard() -> ReplyKeyboardMarkup:
    """Foydalanuvchi ekrani pastida doimiy turuvchi asosiy tugmalar"""
    kb = [
        [
            KeyboardButton(text="📚 Grammatika Darajalari (A1-C1)"),
            KeyboardButton(text="🎓 Gyote Testlari (A1-C2)")
        ],
        [
            KeyboardButton(text="📖 Lug'at & So'zlar (A1-C2)"),
            KeyboardButton(
                text="🌐 Worthub Saytimiz",
                web_app=WebAppInfo(url=config.WEBSITE_URL)
            )
        ],
        [
            KeyboardButton(text="🔍 Mavzu Qidirish"),
            KeyboardButton(text="🎲 Tasodifiy Test")
        ],
        [
            KeyboardButton(text="ℹ️ Duden Standarti Haqida")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def get_worthub_inline_keyboard() -> InlineKeyboardMarkup:
    """Worthub.vercel.app saytiga ulovchi inline tugmalar"""
    buttons = [
        [
            InlineKeyboardButton(
                text="🌐 Worthub Saytini Ochish (Web App)",
                web_app=WebAppInfo(url=config.WEBSITE_URL)
            )
        ],
        [
            InlineKeyboardButton(
                text="🔗 Brauzerda Ochish (worthub.vercel.app)",
                url=config.WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(text="🏠 Bosh Menyu", callback_data="menu:main")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_levels_inline_keyboard() -> InlineKeyboardMarkup:
    """A1 dan C1 gacha bo'lgan grammatika darajalari"""
    buttons = [
        [
            InlineKeyboardButton(text="🟢 A1 — Boshlang'ich", callback_data="level:A1"),
            InlineKeyboardButton(text="🔵 A2 — Elementar", callback_data="level:A2")
        ],
        [
            InlineKeyboardButton(text="🟡 B1 — O'rta", callback_data="level:B1"),
            InlineKeyboardButton(text="🟠 B2 — O'rtadan Yuqori", callback_data="level:B2")
        ],
        [
            InlineKeyboardButton(text="🔴 C1 — Mukammal / Akademik", callback_data="level:C1")
        ],
        [
            InlineKeyboardButton(text="🎓 Gyote Imtihon Testlari (A1 - C2)", callback_data="goethe:menu")
        ],
        [
            InlineKeyboardButton(text="📖 Lug'at & So'z Boyligi", callback_data="vocab:menu"),
            InlineKeyboardButton(text="🌐 Worthub Sayti", web_app=WebAppInfo(url=config.WEBSITE_URL))
        ],
        [
            InlineKeyboardButton(text="🎲 Aralash Duden Testi (5 ta savol)", callback_data="quiz:random")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_goethe_levels_inline_keyboard() -> InlineKeyboardMarkup:
    """Goethe-Institut rasmiy imtihon darajalari tanlovi (A1 - C2)"""
    buttons = [
        [
            InlineKeyboardButton(text="🟢 Goethe A1 (Start Deutsch 1)", callback_data="goethe:level:A1"),
            InlineKeyboardButton(text="🔵 Goethe A2 (Fit in Deutsch / A2)", callback_data="goethe:level:A2")
        ],
        [
            InlineKeyboardButton(text="🟡 Goethe B1 (Zertifikat B1)", callback_data="goethe:level:B1"),
            InlineKeyboardButton(text="🟠 Goethe B2 (Zertifikat B2)", callback_data="goethe:level:B2")
        ],
        [
            InlineKeyboardButton(text="🔴 Goethe C1 (Zertifikat C1)", callback_data="goethe:level:C1"),
            InlineKeyboardButton(text="🟣 Goethe C2 (GDS Diplom)", callback_data="goethe:level:C2")
        ],
        [
            InlineKeyboardButton(text="🏆 Gyote Daraja Aniqlovchi Test (A1-C2)", callback_data="goethe:einstufung")
        ],
        [
            InlineKeyboardButton(text="📚 Duden Grammatikasiga Qaytish", callback_data="levels:menu"),
            InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_vocab_levels_inline_keyboard() -> InlineKeyboardMarkup:
    """Lug'at bo'limi darajalar va test menyusi"""
    buttons = [
        [
            InlineKeyboardButton(text="🟢 A1 So'zlar", callback_data="vocab:list:A1"),
            InlineKeyboardButton(text="🔵 A2 So'zlar", callback_data="vocab:list:A2")
        ],
        [
            InlineKeyboardButton(text="🟡 B1 So'zlar", callback_data="vocab:list:B1"),
            InlineKeyboardButton(text="🟠 B2 So'zlar", callback_data="vocab:list:B2")
        ],
        [
            InlineKeyboardButton(text="🔴 C1 So'zlar", callback_data="vocab:list:C1"),
            InlineKeyboardButton(text="🟣 C2 So'zlar", callback_data="vocab:list:C2")
        ],
        [
            InlineKeyboardButton(text="🎲 Tasodifiy So'z Kartochkasi", callback_data="vocab:card:random")
        ],
        [
            InlineKeyboardButton(text="📝 So'z Boyligi Testi (A1)", callback_data="vocab:quiz:A1"),
            InlineKeyboardButton(text="📝 So'z Testi (B1/B2)", callback_data="vocab:quiz:B1")
        ],
        [
            InlineKeyboardButton(text="🌐 Worthub Saytimiz", web_app=WebAppInfo(url=config.WEBSITE_URL)),
            InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_topics_keyboard(level: str, topics: List[Dict]) -> InlineKeyboardMarkup:
    buttons = []
    for topic in topics:
        buttons.append([
            InlineKeyboardButton(
                text=topic["title"],
                callback_data=f"topic:{topic['id']}"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text="⬅️ Darajalarga qaytish", callback_data="levels:menu"),
        InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_topic_detail_keyboard(topic_id: str, level: str, has_quizzes: bool = True) -> InlineKeyboardMarkup:
    buttons = []
    if has_quizzes:
        buttons.append([
            InlineKeyboardButton(
                text="📝 Mashqni Boshlash (Har gal yangi savollar)",
                callback_data=f"quiz:start:{topic_id}:fresh"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text=f"⬅️ {level} mavzulariga qaytish", callback_data=f"level:{level}"),
        InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_active_quiz_keyboard(options: List[str], topic_id: str) -> InlineKeyboardMarkup:
    buttons = []
    letters = ["A", "B", "C", "D", "E"]
    for i, opt in enumerate(options):
        letter = letters[i] if i < len(letters) else f"{i+1}"
        buttons.append([
            InlineKeyboardButton(
                text=f"{letter}) {opt}",
                callback_data=f"quiz:ans:{i}"
            )
        ])
    buttons.append([
        InlineKeyboardButton(
            text="❌ Testni to'xtatish",
            callback_data="menu:main" if (topic_id.startswith("vocab_") or topic_id.startswith("goethe")) else f"topic:{topic_id}"
        )
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_answer_result_keyboard(is_last: bool, topic_id: str) -> InlineKeyboardMarkup:
    buttons = []
    if not is_last:
        buttons.append([
            InlineKeyboardButton(text="Keyingi savol ➡️", callback_data="quiz:next")
        ])
    else:
        buttons.append([
            InlineKeyboardButton(text="🏁 Natijani Ko'rish", callback_data="quiz:summary")
        ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_quiz_summary_keyboard(
    topic_id: str,
    level: str,
    mistakes_count: int,
    is_fixing_mistakes: bool = False
) -> InlineKeyboardMarkup:
    buttons = []

    # XATOLARNI TO'G'RILASH TUGMASI!
    if mistakes_count > 0:
        buttons.append([
            InlineKeyboardButton(
                text=f"🛠 Xatolarni To'g'rilash ({mistakes_count} ta xato)",
                callback_data="quiz:fix_mistakes"
            )
        ])

    # Lug'at (Vocabulary) testlari uchun
    if topic_id.startswith("vocab_"):
        vocab_lvl = topic_id.replace("vocab_", "")
        buttons.append([
            InlineKeyboardButton(
                text=f"🔄 Yangi {vocab_lvl} So'z Testini Ishlash",
                callback_data=f"vocab:quiz:{vocab_lvl}"
            )
        ])
        buttons.append([
            InlineKeyboardButton(text="📖 Lug'at Menyusiga Qaytish", callback_data="vocab:menu"),
            InlineKeyboardButton(text="🌐 Worthub Sayti", web_app=WebAppInfo(url=config.WEBSITE_URL))
        ])
        buttons.append([
            InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
        ])

    # Goethe imtihonlari uchun
    elif topic_id.startswith("goethe_"):
        if topic_id == "goethe_einstufung":
            buttons.append([
                InlineKeyboardButton(
                    text="🔄 Qaytadan Darajani Aniqlash",
                    callback_data="goethe:einstufung"
                )
            ])
        else:
            goethe_lvl = topic_id.replace("goethe_", "")
            buttons.append([
                InlineKeyboardButton(
                    text=f"🔄 Yangi {goethe_lvl} Gyote Testini Ishlash",
                    callback_data=f"goethe:level:{goethe_lvl}"
                )
            ])
        buttons.append([
            InlineKeyboardButton(text="🎓 Gyote Darajalar Menyusi", callback_data="goethe:menu"),
            InlineKeyboardButton(text="🌐 Worthub Sayti", web_app=WebAppInfo(url=config.WEBSITE_URL))
        ])
        buttons.append([
            InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
        ])

    elif topic_id != "random":
        buttons.append([
            InlineKeyboardButton(
                text="🎲 Boshqa yangi savollar bilan qayta ishlash",
                callback_data=f"quiz:start:{topic_id}:fresh"
            )
        ])
        buttons.append([
            InlineKeyboardButton(text="📖 Mavzuni qayta o'qish", callback_data=f"topic:{topic_id}"),
            InlineKeyboardButton(text=f"📚 {level} darslariga qaytish", callback_data=f"level:{level}")
        ])
        buttons.append([
            InlineKeyboardButton(text="🌐 Worthub Saytimiz", web_app=WebAppInfo(url=config.WEBSITE_URL)),
            InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
        ])
    else:
        buttons.append([
            InlineKeyboardButton(
                text="🎲 Boshqa yangi aralash test boshlash",
                callback_data="quiz:random"
            )
        ])
        buttons.append([
            InlineKeyboardButton(text="📚 Darajalar menyusi", callback_data="levels:menu"),
            InlineKeyboardButton(text="🌐 Worthub Sayti", web_app=WebAppInfo(url=config.WEBSITE_URL))
        ])
        buttons.append([
            InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
        ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_search_results_keyboard(topics: List[Dict]) -> InlineKeyboardMarkup:
    buttons = []
    for topic in topics:
        buttons.append([
            InlineKeyboardButton(
                text=f"[{topic['level']}] {topic['title']}",
                callback_data=f"topic:{topic['id']}"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text="📚 Barcha Darajalar", callback_data="levels:menu"),
        InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu:main")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
