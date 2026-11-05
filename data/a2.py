"""
A2 DARAJASI GRAMMATIKA MAVZULARI (RASMIY DUDEN & CEFR / GeR STANDARTI)
"""

A2_TOPICS = [
    {
        "id": "a2_perfekt",
        "level": "A2",
        "title": "1. Perfekt Zamoni (haben yoki sein? & Partizip II)",
        "keywords": ["perfekt", "haben sein", "partizip 2", "o'tgan zamon", "ge-", "vergangenheit"],
        "summary": "O'tgan zamonda so'zlashuvning yuragi: haben yoki sein tanlashning temir formulasi.",
        "content": (
            "📖 <b>1-MAVZU: Perfekt Zamoni (O'tgan Zamon)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR A2 Standarti:</b>\n"
            "Formulasi: [haben / sein (2-o'rinda)] + ... + [Partizip II (Gap oxirida)]\n"
            "🔹 <b>SEIN oluvchi fe'llar:</b>\n"
            "1. Makonda joy o'zgarishi: gehen, fahren, fliegen, kommen, laufen\n"
            "2. Holat o'zgarishi: aufwachen, einschlafen, sterben, wachsen\n"
            "3. Istisnolar: sein (bin gewesen), bleiben (bin geblieben), passieren\n"
            "🔹 <b>HABEN oluvchi fe'llar:</b> Qolgan barcha fe'llar (~90%).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Tanam bir joydan ikkinchi joyga siljidimi yoki holatim o'zgardimi? Ha bo'lsa ➔ <b>SEIN</b>, bo'lmasa ➔ <b>HABEN</b>!"
        ),
        "quizzes": [
            {
                "id": "a2_perf_q1",
                "question": "'Er ___ gestern nach Deutschland geflogen.' (fliegen = uchmoq)",
                "options": ["ist", "hat", "wird", "sein"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ist</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'fliegen' fe'li joy o'zgarishini bildiradi. Perfektda <b>sein</b> (er ist) bilan yasaladi."
                ),
                "wrong_explanations": {
                    1: "❌ Harakat fe'llari haben olmaydi.",
                    2: "❌ Futur I shakli.",
                    3: "❌ Tuslanmagan shakl."
                }
            },
            {
                "id": "a2_perf_q2",
                "question": "'Ich ___ am Wochenende lange geschlafen.' (schlafen = uxlamoq)",
                "options": ["habe", "bin", "ist", "hat"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: habe</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Uxlaganda joy o'zgarmaydi. Shuning uchun <b>haben</b> yordamchi fe'li ishlatiladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'einschlafen' (uxlab qolish) sein oladi, lekin oddiy 'schlafen' haben oladi!",
                    2: "❌ ist 3-shaxs.",
                    3: "❌ hat 3-shaxs."
                }
            }
        ]
    },
    {
        "id": "a2_praeteritum_sein_haben",
        "level": "A2",
        "title": "2. Präteritum: sein, haben va Modal Fe'llar (war, hatte, konnte)",
        "keywords": ["präteritum a2", "war", "hatte", "konnte", "musste", "o'tgan zamon hikoya"],
        "summary": "Kundalik nutqda sein, haben va modal fe'llarning o'tgan zamonda qo'llanishi.",
        "content": (
            "📖 <b>2-MAVZU: Präteritum (sein, haben va Modal Fe'llar)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR A2 Standarti:</b>\n"
            "Nemislar og'zaki nutqda ham <b>sein</b>, <b>haben</b> va <b>modal fe'llar</b> uchun Perfekt o'rniga Präteritumni afzal ko'rishadi:\n\n"
            "• <b>sein:</b> ich <b>war</b>, du <b>warst</b>, er/sie/es <b>war</b>, wir <b>waren</b>\n"
            "  <i>Ich <b>war</b> gestern krank. (Ich bin gewesen o'rniga)</i>\n"
            "• <b>haben:</b> ich <b>hatte</b>, du <b>hattest</b>, er/sie/es <b>hatte</b>, wir <b>hatten</b>\n"
            "  <i>Ich <b>hatte</b> keine Zeit. (Ich habe gehabt o'rniga)</i>\n"
            "• <b>Modal fe'llar (Umlaut YO'QOLADI!):</b>\n"
            "  - können ➔ ich <b>konnte</b>\n"
            "  - müssen ➔ ich <b>musste</b>\n"
            "  - dürfen ➔ ich <b>durfte</b>\n"
            "  - wollen ➔ ich <b>wollte</b>\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Präteritumda 'Men' (ich) va 'U' (er/sie/es) egizaklardek bir xil bo'ladi: ich war = er war; ich hatte = er hatte!"
        ),
        "quizzes": [
            {
                "id": "a2_praet_q1",
                "question": "'Gestern ___ ich keine Zeit, deshalb ___ ich nicht kommen.'",
                "options": ["hatte / konnte", "habe / kann", "war / musste", "hatte / wollte"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: hatte / konnte</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'Gestern' o'tgan zamon bo'lgani uchun haben ➔ <b>hatte</b> va können ➔ <b>konnte</b> Präteritum shaklida ishlatiladi."
                ),
                "wrong_explanations": {
                    1: "❌ Hozirgi zamon shakllari.",
                    2: "❌ 'Vaqt bo'ldim' mantiqsiz.",
                    3: "❌ 'kela olmadim' ma'nosiga konnte to'g'ri keladi."
                }
            }
        ]
    },
    {
        "id": "a2_wechselpraep",
        "level": "A2",
        "title": "3. Ikki Tomonlama Ko'makchilar (Wechselpräpositionen: Wo? vs Wohin?)",
        "keywords": ["wechselpräpositionen", "an auf in", "wo dativ", "wohin akkusativ", "ko'makchilar"],
        "summary": "Wo? (Tinchlik) ➔ Dativ, Wohin? (Harakat/Yo'nalish) ➔ Akkusativ!",
        "content": (
            "📖 <b>3-MAVZU: Ikki Tomonlama Ko'makchilar (Wechselpräpositionen)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "an, auf, hinter, in, neben, über, unter, vor, zwischen.\n"
            "1. <b>WO? (Qayerda? Tinchlik):</b> ➔ <b>DATIV</b> (Das Buch liegt auf <b>dem</b> Tisch).\n"
            "2. <b>WOHIN? (Qayerga? Yo'nalish):</b> ➔ <b>AKKUSATIV</b> (Ich lege das Buch auf <b>den</b> Tisch).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> Tinch tursa Dativ, yo'naltirilsa Akkusativ!"
        ),
        "quizzes": [
            {
                "id": "a2_wech_q1",
                "question": "'Ich hänge das Bild an ___ Wand.' (die Wand = devor, ilish harakati)",
                "options": ["die Wand (Akkusativ - Wohin?)", "der Wand (Dativ - Wo?)", "dem Wand", "den Wand"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: die Wand</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Rasm devorga qaratib ilinmoqda (Wohin? - Qayerga? ➔ Akkusativ: die Wand)."
                ),
                "wrong_explanations": {
                    1: "❌ 'der Wand' osilib turgan holat (Wo?).",
                    2: "❌ Wand ayol jinsi.",
                    3: "❌ den Wand xato."
                }
            }
        ]
    },
    {
        "id": "a2_praepositionen",
        "level": "A2",
        "title": "4. Sof Dativ va Sof Akkusativ Ko'makchilari (DOGFU & Aus-bei-mit)",
        "keywords": ["dativ ko'makchilari", "akkusativ ko'makchilari", "aus bei mit nach", "durch für gegen ohne um"],
        "summary": "Savoliga qaramasdan har doim bitta kelishik talab qiluvchi temir ko'makchilar.",
        "content": (
            "📖 <b>4-MAVZU: Sof Dativ va Sof Akkusativ Ko'makchilari</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• <b>FAQAT AKKUSATIV (DOGFU):</b> Durch, Ohne, Gegen, Für, Um\n"
            "• <b>FAQAT DATIV:</b> aus, bei, mit, nach, seit, von, zu, gegenüber\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> aus - bei - mit - nach - seit - von - zu ko'rdingizmi ➔ 100% <b>DATIV</b>!"
        ),
        "quizzes": [
            {
                "id": "a2_prp_q1",
                "question": "'Ich fahre jeden Tag mit ___ Bus zur Arbeit.' (der Bus)",
                "options": ["dem", "den", "der", "das"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: dem</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'mit' qat'iy ravishda <b>DATIV</b> talab qiladi. der Bus ➔ mit <b>dem</b> Bus."
                ),
                "wrong_explanations": {
                    1: "❌ 'den' Akkusativ.",
                    2: "❌ 'der' ayol jinsi Dativi.",
                    3: "❌ 'das' Bus erkak jinsida."
                }
            }
        ]
    },
    {
        "id": "a2_adjektivdeklination",
        "level": "A2",
        "title": "5. Sifat Turlanishi (Adjektivdeklination: Sehrli Formula)",
        "keywords": ["sifat turlanishi", "adjektivdeklination", "sifat qo'shimchalari", "der alte mann", "ein alter mann"],
        "summary": "Sifat qo'shimchalari jadvalini oson tushunish va eslab qolish siri.",
        "content": (
            "📖 <b>5-MAVZU: Sifat Turlanishi (Adjektivdeklination)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• Aniq artikldan keyin: Nominativda sifat <b>-e</b> oladi. Dativ, Genitiv va ko'plikda: <b>-en</b>!\n"
            "• Noaniq artikldan keyin (ein): ein alter Mann (-er), ein neues Auto (-es), eine schöne Frau (-e).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> Dativ yoki ko'plik bo'ldimi ➔ har doim <b>-EN</b>!"
        ),
        "quizzes": [
            {
                "id": "a2_adj_q1",
                "question": "'Ich habe ein ___ Auto gekauft.' (das Auto, neu)",
                "options": ["neues", "neue", "neuen", "neuem"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: neues</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Auto o'rta jins (das Auto). Sifat 'das' ning belgisini o'ziga oladi: ein neu<b>es</b> Auto."
                ),
                "wrong_explanations": {
                    1: "❌ 'neue' ayol jinsi uchun.",
                    2: "❌ 'neuen' erkak jinsi Akkusativida.",
                    3: "❌ 'neuem' Dativ shakli."
                }
            }
        ]
    },
    {
        "id": "a2_komparativ_superlativ",
        "level": "A2",
        "title": "6. Sifat Darajalari (Komparativ & Superlativ: als vs wie)",
        "keywords": ["komparativ", "superlativ", "sifat darajalari", "besser", "am besten", "als wie"],
        "summary": "Taqqoslaganda 'als' va tenglikda 'wie' qo'llash formulasi.",
        "content": (
            "📖 <b>6-MAVZU: Sifat Darajalari (Komparativ & Superlativ)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "1. <b>Positiv (Tenglik): so ... wie</b> (xuddi ...dek):\n"
            "• Ali ist <b>so groß wie</b> Vali. (Ali Vali kabi baland bo'yli).\n\n"
            "2. <b>Komparativ (Qiyosiy daraja): -er + als</b> (ko'ra, nisbatan):\n"
            "• Ali ist <b>größer als</b> Vali. (Ali Validan balandroq).\n\n"
            "3. <b>Superlativ (Orttirma daraja): am ...-sten</b>:\n"
            "• Er ist <b>am größten</b>. (U eng baland bo'ylisi).\n\n"
            "⚡ <b>Noqoidali sifatlar:</b>\n"
            "• gut ➔ <b>besser</b> ➔ <b>am besten</b>\n"
            "• viel ➔ <b>mehr</b> ➔ <b>am meisten</b>\n"
            "• gern ➔ <b>lieber</b> ➔ <b>am liebsten</b>\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Teng bo'lsa ➔ <b>wie</b>, farq bo'lsa ➔ <b>als</b>! Boshqa holat yo'q!"
        ),
        "quizzes": [
            {
                "id": "a2_komp_q1",
                "question": "'Mein Bruder ist älter ___ ich.'",
                "options": ["als", "wie", "denn", "so"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: als</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Komparativ darajada (-er: älter) taqqoslash vositasi doimo <b>als</b> bo'ladi: älter <b>als</b> ich."
                ),
                "wrong_explanations": {
                    1: "❌ 'wie' faqat tenglikda (so alt wie) ishlatiladi.",
                    2: "❌ 'denn' sabab bog'lovchisi.",
                    3: "❌ 'so' tenglik qismining boshida keladi."
                }
            }
        ]
    },
    {
        "id": "a2_nebensaetze_weil_dass_wenn",
        "level": "A2",
        "title": "7. Ergash Gaplar: weil, dass, wenn (Fe'l oxiriga ketishi)",
        "keywords": ["weil", "dass", "wenn", "nebensatz", "ergash gap", "fe'l oxirida", "verb am ende"],
        "summary": "Nega bu bog'lovchilar tuslangan fe'lni gapning eng oxiriga surgun qiladi?",
        "content": (
            "📖 <b>7-MAVZU: Ergash Gaplar (Nebensätze: weil, dass, wenn)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "weil, dass, wenn kelganda, <b>TUSLANGAN FE'L GAPNING ENG OXIRIGA SURILADI</b>!\n"
            "• Ich bleibe zu Hause, <b>weil</b> ich krank <b>bin</b>.\n"
            "• Ich weiß, <b>dass</b> du fleißig <b>bist</b>.\n"
            "• <b>Wenn</b> es regnet, <b>bleibe</b> ich hier."
        ),
        "quizzes": [
            {
                "id": "a2_ns_q1",
                "question": "Quyidagi gaplarning qaysi biri to'g'ri?",
                "options": [
                    "Ich lerne Deutsch, weil ich in Deutschland studieren will.",
                    "Ich lerne Deutsch, weil ich will in Deutschland studieren.",
                    "Ich lerne Deutsch, weil will ich in Deutschland studieren.",
                    "Ich lerne Deutsch, weil ich in Deutschland will studieren."
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ...weil ich in Deutschland studieren will.</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'weil' ergash gapida tuslangan modal fe'l <b>will</b> gapning ENG OXIRIGA borib turadi."
                ),
                "wrong_explanations": {
                    1: "❌ 'weil ich will...' xato tartib.",
                    2: "❌ fe'l darhol kelmaydi.",
                    3: "❌ tuslangan fe'l oxirgi bo'lishi shart."
                }
            }
        ]
    },
    {
        "id": "a2_aduso",
        "level": "A2",
        "title": "8. Nol O'rindagi Bog'lovchilar (ADUSO: Tartibni o'zgartirmaydiganlar)",
        "keywords": ["aduso", "aber denn und sondern oder", "nol o'rin", "konjunktionen"],
        "summary": "aber, denn, und, sondern, oder — gap tartibiga mutlaqo teginmaydigan do'stlar.",
        "content": (
            "📖 <b>8-MAVZU: Nol O'rindagi Bog'lovchilar (ADUSO)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "<b>A</b>ber, <b>D</b>enn, <b>U</b>nd, <b>S</b>ondern, <b>O</b>der gap tartibini aslo o'zgartirmaydi (Position 0). "
            "Ulardan keyin darhol [Ega] + [Fe'l 2-o'rinda] keladi!\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> ADUSO — ko'rinmas nol raqamli o'yinchilar!"
        ),
        "quizzes": [
            {
                "id": "a2_adu_q1",
                "question": "'Ich trinke keinen Kaffee, ___ ich mag nur Tee.' (denn vs weil)",
                "options": ["denn", "weil", "obwohl", "dass"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: denn</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'ich mag nur Tee' gapida ega 1-o'rinda, fe'l (mag) 2-o'rinda. Bu 0-o'rindagi <b>denn</b> bog'lovchisidir."
                ),
                "wrong_explanations": {
                    1: "❌ 'weil' fe'lni gap oxiriga suradi.",
                    2: "❌ 'obwohl' fe'lni oxirga suradi.",
                    3: "❌ 'dass' to'ldiruvchi gap."
                }
            }
        ]
    },
    {
        "id": "a2_reflexiv",
        "level": "A2",
        "title": "9. O'zlik Fe'llari (Reflexive Verben: sich freuen, sich waschen)",
        "keywords": ["o'zlik fe'llari", "reflexiv", "sich", "mich mir", "dich dir"],
        "summary": "O'zini yuvmoq, xursand bo'lmoq: sich, mich va mir ni to'g'ri qo'llash.",
        "content": (
            "📖 <b>9-MAVZU: O'zlik Fe'llari (Reflexive Verben)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• Boshqa to'ldiruvchi yo'q ➔ Akkusativ: Ich wasche <b>mich</b>.\n"
            "• Aniq tana a'zosi ko'rsatilsa ➔ Dativ: Ich wasche <b>mir die Hände</b>.\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> Tana a'zosi aytildimi — darhol <b>mir / dir</b>!"
        ),
        "quizzes": [
            {
                "id": "a2_refl_q1",
                "question": "'Ich putze ___ die Zähne.' (die Zähne = tishlar)",
                "options": ["mir", "mich", "sich", "uns"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: mir</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'die Zähne' Akkusativ to'ldiruvchi bo'lib kelgani uchun o'zlik olmoshi Dativ (mir) bo'ladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'mich' ob'ekt bo'lmaganda (Ich putze mich) ishlatilardi.",
                    2: "❌ 'sich' faqat 3-shaxs.",
                    3: "❌ 'uns' biz."
                }
            }
        ]
    },
    {
        "id": "a2_passiv_praesens",
        "level": "A2",
        "title": "10. Majhul Nisbatga Kirish (Vorgangspassiv Präsens: werden + Partizip II)",
        "keywords": ["passiv", "majhul nisbat", "werden", "von durch", "vorgangspassiv"],
        "summary": "Ish kim tomonidan qilingani emas, ishning o'zi muhim bo'lganda qo'llanadigan formulalar.",
        "content": (
            "📖 <b>10-MAVZU: Majhul Nisbatga Kirish (Vorgangspassiv Präsens)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Formulasi: [<b>werden</b> (tuslangan)] + ... + [<b>Partizip II</b>]\n"
            "• Das Auto <b>wird repariert</b>. (Mashina ta'mirlanmoqda)."
        ),
        "quizzes": [
            {
                "id": "a2_pas_q1",
                "question": "'Das Haus ___ im Jahr 2026 gebaut.'",
                "options": ["wird", "ist", "hat", "werdet"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: wird</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Jarayon majhulligi: <b>werden + Partizip II</b>. 'Das Haus' (3-shaxs) uchun: <b>wird</b> gebaut."
                ),
                "wrong_explanations": {
                    1: "❌ 'ist' holat majhulligi (Zustandspassiv).",
                    2: "❌ 'hat' Passiv hech qachon haben olmaydi.",
                    3: "❌ 'werdet' ihr uchun."
                }
            }
        ]
    }
]
