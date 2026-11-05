"""
A1 DAN C2 GACHA NEMIS TILI LUG'AT BAZASI (VOCABULARY)
Har bir so'z artikli, ko'pligi, o'zbekcha tarjimasi, mavzusi va jonli misoli bilan.
"""
import random

VOCABULARY_DATA = {
    "A1": [
        {
            "word": "der Apfel",
            "plural": "die Äpfel",
            "translation": "olma",
            "category": "Oziq-ovqat",
            "example": "Ich esse jeden Tag einen Apfel.",
            "example_uz": "Men har kuni bitta olma yeyman."
        },
        {
            "word": "das Buch",
            "plural": "die Bücher",
            "translation": "kitob",
            "category": "O'qish & Ta'lim",
            "example": "Das Buch ist sehr interessant.",
            "example_uz": "Kitob juda qiziqarli."
        },
        {
            "word": "die Familie",
            "plural": "die Familien",
            "translation": "oila",
            "category": "Oila",
            "example": "Meine Familie wohnt in Taschkent.",
            "example_uz": "Mening oilam Toshkentda yashaydi."
        },
        {
            "word": "der Freund",
            "plural": "die Freunde",
            "translation": "do'st (o'rtoq)",
            "category": "Munosabatlar",
            "example": "Mein Freund hilft mir immer.",
            "example_uz": "Do'stim menga doimo yordam beradi."
        },
        {
            "word": "die Wohnung",
            "plural": "die Wohnungen",
            "translation": "kvartira (xonadon)",
            "category": "Uy-joy",
            "example": "Die Wohnung hat drei Zimmer.",
            "example_uz": "Kvartirada uchta xona bor."
        },
        {
            "word": "das Auto",
            "plural": "die Autos",
            "translation": "mashina (avtomobil)",
            "category": "Transport",
            "example": "Er fährt ein schnelles Auto.",
            "example_uz": "U tez yurar mashina haydaydi."
        },
        {
            "word": "die Arbeit",
            "plural": "die Arbeiten",
            "translation": "ish (mehnat)",
            "category": "Kasb & Ish",
            "example": "Ich gehe um 8 Uhr zur Arbeit.",
            "example_uz": "Men soat 8 da ishga boraman."
        },
        {
            "word": "die Zeit",
            "plural": "die Zeiten",
            "translation": "vaqt",
            "category": "Vaqt",
            "example": "Heute habe ich leider keine Zeit.",
            "example_uz": "Bugun menda afsuski vaqt yo'q."
        }
    ],

    "A2": [
        {
            "word": "die Erfahrung",
            "plural": "die Erfahrungen",
            "translation": "tajriba",
            "category": "Hayot & Ish",
            "example": "Er hat viel Erfahrung in diesem Beruf.",
            "example_uz": "Uning bu kasbda tajribasi ko'p."
        },
        {
            "word": "die Reise",
            "plural": "die Reisen",
            "translation": "sayohat",
            "category": "Sayohat",
            "example": "Die Reise nach Berlin war wunderbar.",
            "example_uz": "Berlinga sayohat ajoyib bo'ldi."
        },
        {
            "word": "der Urlaub",
            "plural": "die Urlaube",
            "translation": "ta'til (mehnat ta'tili)",
            "category": "Dam olish",
            "example": "Im Sommer fahre ich in den Urlaub.",
            "example_uz": "Yozda men ta'tilga ketaman."
        },
        {
            "word": "die Gesundheit",
            "plural": "-",
            "translation": "salomatlik",
            "category": "Tibbiyot",
            "example": "Gesundheit ist das Wichtigste im Leben.",
            "example_uz": "Salomatlik hayotdagi eng muhim narsadir."
        },
        {
            "word": "das Angebot",
            "plural": "die Angebote",
            "translation": "taklif (aksiya, narx taklifi)",
            "category": "Savdo & Xarid",
            "example": "Das ist ein sehr günstiges Angebot.",
            "example_uz": "Bu juda qulay taklif."
        },
        {
            "word": "die Umwelt",
            "plural": "-",
            "translation": "atrof-muhit",
            "category": "Tabiat",
            "example": "Wir müssen die Umwelt schützen.",
            "example_uz": "Biz atrof-muhitni asrashimiz kerak."
        }
    ],

    "B1": [
        {
            "word": "die Entscheidung",
            "plural": "die Entscheidungen",
            "translation": "qaror",
            "category": "Jamiyat & Shaxs",
            "example": "Ich muss eine wichtige Entscheidung treffen.",
            "example_uz": "Men muhim bir qaror qabul qilishim kerak."
        },
        {
            "word": "die Ausbildung",
            "plural": "die Ausbildungen",
            "translation": "kasbiy ta'lim (o'qish)",
            "category": "Ta'lim",
            "example": "Er macht eine Ausbildung zum Mechatroniker.",
            "example_uz": "U mexatronik bo'yicha kasbiy ta'lim olmoqda."
        },
        {
            "word": "die Beziehung",
            "plural": "die Beziehungen",
            "translation": "munosabat (aloqa)",
            "category": "Munosabatlar",
            "example": "Vertrauen ist die Basis jeder Beziehung.",
            "example_uz": "Ishonch har qanday munosabatning asosidir."
        },
        {
            "word": "die Bewerbung",
            "plural": "die Bewerbungen",
            "translation": "ishga ariza (rezyume)",
            "category": "Ish qidirish",
            "example": "Ich habe gestern meine Bewerbung abgeschickt.",
            "example_uz": "Men kecha arizamni jo'natdim."
        },
        {
            "word": "die Herausforderung",
            "plural": "die Herausforderungen",
            "translation": "qiyin vazifa (chaqiriq, sinov)",
            "category": "Rivojlanish",
            "example": "Das neue Projekt ist eine große Herausforderung.",
            "example_uz": "Yangi loyiha katta bir sinovdir."
        },
        {
            "word": "die Gesellschaft",
            "plural": "die Gesellschaften",
            "translation": "jamiyat",
            "category": "Ijtimoiy hayot",
            "example": "Jeder Bürger spielt eine Rolle in der Gesellschaft.",
            "example_uz": "Har bir fuqaro jamiyatda o'z roliga ega."
        }
    ],

    "B2": [
        {
            "word": "die Voraussetzung",
            "plural": "die Voraussetzungen",
            "translation": "shart (talab, dastlabki mezon)",
            "category": "Talablar",
            "example": "Gute Deutschkenntnisse sind eine feste Voraussetzung.",
            "example_uz": "Yaxshi nemis tili bilimi qat'iy talabdir."
        },
        {
            "word": "die Maßnahme",
            "plural": "die Maßnahmen",
            "translation": "chora-tadbir",
            "category": "Boshqaruv",
            "example": "Die Regierung ergreift strenge Maßnahmen.",
            "example_uz": "Hukumat qat'iy choralar ko'rmoqda."
        },
        {
            "word": "der Fortschritt",
            "plural": "die Fortschritte",
            "translation": "taraqqiyot (oldinga siljish)",
            "category": "Ilm & Texnika",
            "example": "Der technologische Fortschritt verändert die Welt.",
            "example_uz": "Texnologik taraqqiyot dunyoni o'zgartirmoqda."
        },
        {
            "word": "die Verhandlung",
            "plural": "die Verhandlungen",
            "translation": "muzokara (muhokama)",
            "category": "Biznes & Siyosat",
            "example": "Die Verhandlungen dauerten mehrere Stunden.",
            "example_uz": "Muzokaralar bir necha soat davom etdi."
        },
        {
            "word": "die Nachhaltigkeit",
            "plural": "-",
            "translation": "barqarorlik (ekologik uzoq muddatlilik)",
            "category": "Ekologiya & Iqtisod",
            "example": "Nachhaltigkeit steht im Mittelpunkt unserer Strategie.",
            "example_uz": "Barqarorlik bizning strategiyamiz markazida turadi."
        }
    ],

    "C1": [
        {
            "word": "die Plausibilität",
            "plural": "-",
            "translation": "ishonarlilik (mantiqiy asoslilik)",
            "category": "Akademik mantiq",
            "example": "Die Plausibilität der Argumente wurde überprüft.",
            "example_uz": "Dalillarning mantiqiy ishonarliligi tekshirildi."
        },
        {
            "word": "die Divergenz",
            "plural": "die Divergenzen",
            "translation": "tafovut (qarashlar ixtilofi, farqlanish)",
            "category": "Ilmiy tahlil",
            "example": "Es besteht eine erhebliche Divergenz zwischen Theorie und Praxis.",
            "example_uz": "Nazariya va amaliyot o'rtasida jiddiy tafovut mavjud."
        },
        {
            "word": "die Implikation",
            "plural": "die Implikationen",
            "translation": "kelib chiqadigan oqibat (yashirin ma'no)",
            "category": "Falsafa & Fan",
            "example": "Diese Entdeckung hat weitreichende ethische Implikationen.",
            "example_uz": "Ushbu kashfiyot keng qamrovli axloqiy oqibatlarga ega."
        },
        {
            "word": "die Eloquenz",
            "plural": "-",
            "translation": "notiqilik (so'zga chechanlik, fasohat)",
            "category": "Ritorika",
            "example": "Seine Eloquenz überzeugte das gesamte Auditorium.",
            "example_uz": "Uning notiqligi butun auditoriyani ishontirdi."
        },
        {
            "word": "die Kontroverse",
            "plural": "die Kontroversen",
            "translation": "bahs-munozara (ziddiyatli ixtilof)",
            "category": "Siyosat & Jamiyat",
            "example": "Das neue Gesetz löste eine heftige Kontroverse aus.",
            "example_uz": "Yangi qonun shiddatli bahs-munozaralarga sabab bo'ldi."
        }
    ],

    "C2": [
        {
            "word": "die Ambivalenz",
            "plural": "die Ambivalenzen",
            "translation": "ikkiyoqlamalik (qarama-qarshi hislar uyg'unligi)",
            "category": "Oliy adabiyot & Psixologiya",
            "example": "Er betrachtete die Situation mit einer gewissen Ambivalenz.",
            "example_uz": "U vaziyatga ma'lum bir ikkilanish bilan qaradi."
        },
        {
            "word": "das Refugium",
            "plural": "die Refugien",
            "translation": "panohgoh (oromgoh, sokin boshpana)",
            "category": "Mumtoz adabiyot",
            "example": "Die alte Bibliothek war sein persönliches Refugium.",
            "example_uz": "Qadimiy kutubxona uning shaxsiy oromgohi edi."
        },
        {
            "word": "die Quintessenz",
            "plural": "-",
            "translation": "mohiyat (eng sarasi, asl tub ma'no)",
            "category": "Falsafa",
            "example": "Die Quintessenz seiner Rede war der Aufruf zum Frieden.",
            "example_uz": "Uning nutqining asl mohiyati tinchlikka chaqiriq edi."
        },
        {
            "word": "das Renommee",
            "plural": "-",
            "translation": "yuksak obro'-e'tibor (nufuz)",
            "category": "Diplomatiya & Elita",
            "example": "Die Universität genießt weltweit ein exzellentes Renommee.",
            "example_uz": "Universitet dunyo bo'ylab yuksak obro'-e'tiborga ega."
        },
        {
            "word": "die Akribie",
            "plural": "-",
            "translation": "o'ta nozik sinchkovlik (mukammallikka intilish)",
            "category": "Akademik uslub",
            "example": "Er widmete sich der Manuskriptanalyse mit wissenschaftlicher Akribie.",
            "example_uz": "U qo'lyozma tahliliga ilmiy sinchkovlik bilan kirishdi."
        }
    ]
}


def get_words_by_level(level: str):
    """Tanlangan darajadagi so'zlar ro'yxatini qaytaradi"""
    return VOCABULARY_DATA.get(level.upper(), [])


def get_random_word(level: str = None):
    """Tasodifiy bitta so'z kartochkasini qaytaradi"""
    if level and level.upper() in VOCABULARY_DATA:
        words = VOCABULARY_DATA[level.upper()]
    else:
        words = []
        for l_words in VOCABULARY_DATA.values():
            words.extend(l_words)
    return random.choice(words) if words else None


def generate_vocab_quiz(level: str = "A1"):
    """So'z bo'yicha interaktiv test savoli hosil qiladi"""
    level_words = get_words_by_level(level)
    if not level_words or len(level_words) < 4:
        level_words = []
        for l_words in VOCABULARY_DATA.values():
            level_words.extend(l_words)

    target = random.choice(level_words)
    other_words = [w for w in level_words if w["word"] != target["word"]]
    distractors = random.sample(other_words, min(3, len(other_words)))

    options = [target["translation"]] + [d["translation"] for d in distractors]
    random.shuffle(options)
    correct_idx = options.index(target["translation"])

    question_text = (
        f"📖 <b>Nemischa so'z tarjimasini toping:</b>\n\n"
        f"So'z: <b>{target['word']}</b> ({target.get('plural', '')})\n"
        f"💡 Misol: <i>\"{target['example']}\"</i>"
    )

    proof = (
        f"✅ <b>TO'G'RI JAVOB: {target['translation']}</b>\n\n"
        f"📌 <b>So'z:</b> {target['word']} ({target.get('plural', '')})\n"
        f"🇺🇿 <b>Tarjimasi:</b> {target['translation']}\n"
        f"📝 <b>Misol:</b> <i>{target['example']}</i>\n"
        f"🔍 <b>Tarjimasi:</b> {target['example_uz']}"
    )

    wrong_explanations = {}
    for i, opt in enumerate(options):
        if i != correct_idx:
            wrong_explanations[i] = f"❌ '{opt}' boshqa so'zning tarjimasi. '{target['word']}' so'zining to'g'ri ma'nosi — '{target['translation']}'."

    return {
        "id": f"vocab_{target['word']}",
        "question": question_text,
        "options": options,
        "correct_index": correct_idx,
        "proof": proof,
        "wrong_explanations": wrong_explanations
    }
