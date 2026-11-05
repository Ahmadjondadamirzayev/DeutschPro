"""
A1 DARAJASI GRAMMATIKA MAVZULARI (RASMIY DUDEN & CEFR / GeR STANDARTI)
Har bir mavzu CEFR A1 talablariga 100% mos va turfa xil test savollari bilan boyitilgan.
"""

A1_TOPICS = [
    {
        "id": "a1_artikel",
        "level": "A1",
        "title": "1. Aniq va Noaniq Artikellar (der, die, das / ein, eine / Nullartikel)",
        "keywords": ["artikl", "artikel", "der", "die", "das", "ein", "eine", "aniq artikl", "noaniq artikl", "nol artikl"],
        "summary": "Nemis tilida har bir otning pasporti - artikllar va ularning qo'llanish sirlari.",
        "content": (
            "📖 <b>1-MAVZU: Aniq va Noaniq Artikellar (Bestimmter & Unbestimmter Artikel)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR A1 Me'yori:</b>\n"
            "Nemis tilida barcha otlar bosh harf bilan yoziladi va o'zining jinsini (Maskulin, Feminin, Neutrum) ko'rsatuvchi artiklga ega bo'ladi.\n\n"
            "🔹 <b>Aniq artikl (Bestimmter Artikel):</b> Aniq ma'lum, avval tilga olingan yoki yagona bo'lgan narsalar uchun:\n"
            "• <b>der</b> — Erkak jinsi (Maskulin): <i>der Tisch</i> (stol)\n"
            "• <b>die</b> — Ayol jinsi (Feminin): <i>die Sonne</i> (quyosh)\n"
            "• <b>das</b> — O'rta jins (Neutrum): <i>das Buch</i> (kitob)\n"
            "• <b>die</b> — Ko'plik (Plural - barcha jinslar uchun): <i>die Bücher</i> (kitoblar)\n\n"
            "🔹 <b>Noaniq artikl (Unbestimmter Artikel):</b> Noma'lum, ixtiyoriy bitta narsa uchun:\n"
            "• Erkak: <b>ein</b> Mann | Ayol: <b>eine</b> Frau | O'rta: <b>ein</b> Kind\n"
            "⚠️ <i>DUDEN TEMIR QOIDASI: Noaniq artiklning KO'PLIK shakli YO'Q (Nol artikl)!</i>\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Do'konga kirdingiz: 'Ich möchte <b>ein</b> Buch kaufen' (Ixtiyoriy bitta kitob = ein). "
            "Sotuvchi uzatgan aniq kitob haqida gapirsangiz: '<b>Das</b> Buch gefällt mir!' (O'sha kitob = das)!"
        ),
        "quizzes": [
            {
                "id": "a1_art_q1",
                "question": "Gapni to'ldiring: 'Dort steht ___ Mann. ___ Mann ist mein Lehrer.'",
                "options": ["ein / Der", "der / Ein", "eine / Die", "ein / Ein"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ein / Der</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "1. 'Mann' — erkak jinsidagi ot (der Mann).\n"
                    "2. Birinchi gapda u noma'lum shaxs sifatida ilk bor tilga olinyapti ➔ <b>ein</b>.\n"
                    "3. Ikkinchi gapda esa u shaxs allaqachon ma'lum ➔ <b>Der</b>."
                ),
                "wrong_explanations": {
                    1: "❌ Noma'lum narsa birinchi bor tilga olinganda aniq artikl (der) emas, noaniq (ein) bo'ladi.",
                    2: "❌ Mann erkak jinsi, ayol jinsi (eine/die) emas.",
                    3: "❌ Ikkinchi gapda ma'lum bo'lib qoldi, noaniq ein qo'yilmaydi."
                }
            },
            {
                "id": "a1_art_q2",
                "question": "Quyidagi otlardan qaysi biri ko'plikda NOANIQ artikl bilan ishlatiladi?",
                "options": ["Hech qaysi biri (Ko'plikda noaniq artikl bo'lmaydi)", "eine Bücher", "ein Autos", "einen Kinder"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Hech qaysi biri!</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Dudenda 'ein' bu 'bir' so'zidan olingan. Ko'plikda esa 'bir kitoblar' deb bo'lmaydi. Shuning uchun ko'plikda noaniq artikl mutlaqo ISHLATILMAYDI (Nullartikel)!"
                ),
                "wrong_explanations": {
                    1: "❌ 'eine Bücher' qo'pol xato.",
                    2: "❌ 'ein Autos' ko'plik bilan qo'shilmaydi.",
                    3: "❌ 'einen Kinder' xato."
                }
            },
            {
                "id": "a1_art_q3",
                "question": "'Das ist ___ Lampe. ___ Lampe ist neu.' (die Lampe = chiroq)",
                "options": ["eine / Die", "ein / Der", "die / Eine", "eine / Das"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: eine / Die</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Lampe — ayol jinsi (die Lampe). Noaniq shakli <b>eine</b>, aniq shakli esa <b>Die</b> bo'ladi."
                ),
                "wrong_explanations": {
                    1: "❌ Lampe erkak jinsi emas.",
                    2: "❌ Tartib teskari.",
                    3: "❌ Lampe o'rta jins emas."
                }
            }
        ]
    },
    {
        "id": "a1_genus_plural",
        "level": "A1",
        "title": "2. Otlarning Jinsi va Ko'plik Yasalishi (Genus & Plural)",
        "keywords": ["genus", "jins", "maskulin", "feminin", "neutrum", "plural", "ko'plik", "suffiks"],
        "summary": "Otlarning jinsini suffikslar orqali aniqlash va ko'plik yasashning 5 xil usuli.",
        "content": (
            "📖 <b>2-MAVZU: Otlarning Jinsi va Ko'plik Yasalishi (Genus & Plural)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "1. <b>DIE (Ayol jinsi):</b> -ung, -heit, -keit, -schaft, -tät, -ion bilan tugasa 100% DIE!\n"
            "2. <b>DER (Erkak jinsi):</b> fasllar, oylar, hafta kunlari, -or, -er (kasblar: der Lehrer, der Fahrer).\n"
            "3. <b>DAS (O'rta jins):</b> -chen, -lein (das Mädchen, das Brötchen), -ment (das Dokument), -um (das Zentrum).\n\n"
            "🔹 <b>KO'PLIK (PLURAL) YASALISHINING 5 TA ASOSIY TURI:</b>\n"
            "1. <b>-(e)n:</b> die Frau ➔ die Frau<b>en</b>, die Zeitung ➔ die Zeitung<b>en</b> (Ayol jinsi 95% -en oladi!)\n"
            "2. <b>-e (ko'pincha umlaut bilan):</b> der Tisch ➔ die Tisch<b>e</b>, der Stuhl ➔ die Stühl<b>e</b>\n"
            "3. <b>-er (ko'pincha umlaut bilan):</b> das Kind ➔ die Kind<b>er</b>, das Buch ➔ die Büch<b>er</b>\n"
            "4. <b>-s:</b> das Auto ➔ die Auto<b>s</b>, das Hotel ➔ die Hotel<b>s</b>\n"
            "5. <b>O'zgarishsiz (faqat artikl o'zgaradi):</b> der Lehrer ➔ die Lehrer, das Fenster ➔ die Fenster\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Barcha ko'plikdagi otlarning aniq artikli har doim <b>DIE</b> bo'ladi! "
            "Ayol jinsidagi otlar ko'plikda deyarli har doim <b>-(e)n</b> oladi!"
        ),
        "quizzes": [
            {
                "id": "a1_gen_q1",
                "question": "'Wohnung' (kvartira) so'zining jinsi va ko'pligi qaysi?",
                "options": ["die Wohnung / die Wohnungen", "der Wohnung / die Wohnungen", "das Wohnung / die Wohnungs", "die Wohnung / die Wöhninger"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: die Wohnung / die Wohnungen</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "1. -ung suffiksi bilan tugagan barcha otlar 100% <b>DIE</b> (feminin) dir.\n"
                    "2. -ung bilan tugagan otlar ko'plikda doimo <b>-en</b> oladi: die Wohnungen."
                ),
                "wrong_explanations": {
                    1: "❌ Wohnung erkak jinsi emas.",
                    2: "❌ das emas.",
                    3: "❌ Ko'plik shakli xato yasalgan."
                }
            },
            {
                "id": "a1_gen_q2",
                "question": "'das Kind' (bola) so'zining ko'plik shakli qanday?",
                "options": ["die Kinder", "die Kinden", "die Kindes", "die Kinde"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: die Kinder</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Ko'plab o'rta jinsdagi (das) bir bo'g'inli otlar ko'plikda <b>-er</b> qo'shimchasini oladi: das Kind ➔ die Kinder, das Bild ➔ die Bilder."
                ),
                "wrong_explanations": {
                    1: "❌ Kinden bunday so'z faqat Dativ ko'plikda (den Kindern) bo'ladi.",
                    2: "❌ Kindes bu Genitiv shakli.",
                    3: "❌ Kinde emas."
                }
            }
        ]
    },
    {
        "id": "a1_personalpronomen",
        "level": "A1",
        "title": "3. Kishilik Olmoshlari (Nominativ, Akkusativ va Dativ: mich/mir, dich/dir)",
        "keywords": ["personalpronomen", "kishilik olmoshlari", "mich", "mir", "dich", "dir", "ihn", "ihm"],
        "summary": "Men, meni, menga; sen, seni, senga — kishilik olmoshlarining A1 jadvali.",
        "content": (
            "📖 <b>3-MAVZU: Kishilik Olmoshlari (Personalpronomen)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR A1 Talabi:</b>\n"
            "A1 darajasida kishilik olmoshlarini har uchala asosiy kelishikda bilish shart:\n\n"
            "📊 <b>Olmoshlar Jadvali:</b>\n"
            "• <b>ich</b> (men) ➔ Akkusativ: <b>mich</b> (meni) | Dativ: <b>mir</b> (menga)\n"
            "• <b>du</b> (sen) ➔ Akkusativ: <b>dich</b> (seni) | Dativ: <b>dir</b> (senga)\n"
            "• <b>er</b> (u - erkak) ➔ Akkusativ: <b>ihn</b> (uni) | Dativ: <b>ihm</b> (unga)\n"
            "• <b>sie</b> (u - ayol) ➔ Akkusativ: <b>sie</b> (uni) | Dativ: <b>ihr</b> (unga)\n"
            "• <b>es</b> (u - o'rta) ➔ Akkusativ: <b>es</b> (uni) | Dativ: <b>ihm</b> (unga)\n"
            "• <b>wir</b> (biz) ➔ Akkusativ: <b>uns</b> (bizni) | Dativ: <b>uns</b> (bizga)\n"
            "• <b>ihr</b> (sizlar) ➔ Akkusativ: <b>euch</b> (sizlarni) | Dativ: <b>euch</b> (sizlarga)\n"
            "• <b>Sie / sie</b> (Siz / ular) ➔ Akkusativ: <b>Sie / sie</b> | Dativ: <b>Ihnen / ihnen</b>\n\n"
            "💡 <b>Jonli Misollar:</b>\n"
            "• Liebst du <b>mich</b>? (Meni sevasanmi? - Akkusativ)\n"
            "• Wie geht es <b>dir</b>? (Senga qanday ketyapti? Ahvoling qalay? - Dativ)\n"
            "• Ich danke <b>Ihnen</b>! (Sizga rahmat aytaman! - Dativ)\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Akkusativ = <b>-CH / -N</b> (mi<b>ch</b>, di<b>ch</b>, ih<b>n</b>).\n"
            "Dativ = <b>-R / -M</b> (mi<b>r</b>, di<b>r</b>, ih<b>m</b>)!"
        ),
        "quizzes": [
            {
                "id": "a1_per_q1",
                "question": "'Kannst du ___ bitte helfen?' (Sen menga yordam bera olasanmi?)",
                "options": ["mir", "mich", "ich", "meiner"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: mir</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'helfen' fe'li har doim Dativ (Wem? - Kimga?) talab qiladi. "
                    "'ich' olmoshining Dativ shakli <b>mir</b> bo'ladi: Hilf <b>mir</b>!"
                ),
                "wrong_explanations": {
                    1: "❌ 'mich' Akkusativ shakli (Wen? - Kimni?). Helfen fe'li Akkusativ olmaydi.",
                    2: "❌ 'ich' Nominativ (ega).",
                    3: "❌ 'meiner' Genitiv."
                }
            },
            {
                "id": "a1_per_q2",
                "question": "'Ich liebe ___ von ganzem Herzen!' (Men seni butun qalbim bilan sevaman)",
                "options": ["dich", "dir", "du", "dein"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: dich</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'lieben' (sevmoq) fe'li to'g'ridan-to'g'ri Akkusativ (Wen? - Kimni?) talab qiladi. "
                    "'du' olmoshining Akkusativ shakli <b>dich</b> dir: Ich liebe <b>dich</b>."
                ),
                "wrong_explanations": {
                    1: "❌ 'dir' Dativ (senga) shakli.",
                    2: "❌ 'du' Nominativ (sen).",
                    3: "❌ 'dein' egalik olmoshi."
                }
            }
        ]
    },
    {
        "id": "a1_possessiv",
        "level": "A1",
        "title": "4. Egalik Olmoshlari (Possessivpronomen: mein, dein, sein, ihr...)",
        "keywords": ["possessivpronomen", "egalik olmoshlari", "mein", "dein", "sein", "ihr", "unser", "euer"],
        "summary": "Mening, sening, uning — buyumlarning kimga tegishli ekanligini ifodalash.",
        "content": (
            "📖 <b>4-MAVZU: Egalik Olmoshlari (Possessivpronomen)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR A1 Talabi:</b>\n"
            "Har bir kishilik olmoshiga mos keluvchi egalik olmoshi mavjud:\n"
            "• ich ➔ <b>mein</b> (mening)\n"
            "• du ➔ <b>dein</b> (sening)\n"
            "• er (u - erkak) ➔ <b>sein</b> (uning)\n"
            "• es (u - o'rta) ➔ <b>sein</b> (uning)\n"
            "• sie (u - ayol) ➔ <b>ihr</b> (uning)\n"
            "• wir ➔ <b>unser</b> (bizning)\n"
            "• ihr (sizlar) ➔ <b>euer</b> (sizlarning)\n"
            "• Sie / sie ➔ <b>Ihr / ihr</b> (Sizning / ularning)\n\n"
            "🔹 <b>Qo'shimchalar qoidasi:</b>\n"
            "Egalik olmoshi xuddi 'ein' kabi o'zidan keyingi otning jinsiga qarab qo'shimcha oladi:\n"
            "• Erkak: Das ist <b>mein</b> Vater (Nominativ) | Ich sehe <b>meinen</b> Vater (Akkusativ -en oladi!).\n"
            "• Ayol: Das ist <b>meine</b> Mutter (-e oladi).\n"
            "• O'rta: Das ist <b>mein</b> Kind (qo'shimcha yo'q).\n"
            "• Ko'plik: Das sind <b>meine</b> Freunde (-e oladi).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Egalik olmoshi o'zidan keyingi otga xizmat qiladi! Ayol va ko'plik bo'lsa ➔ <b>-e</b> qo'shing (meine, deine)! "
            "Erkak jinsi Akkusativda bo'lsa ➔ <b>-en</b> qo'shing (meinen, deinen)!"
        ),
        "quizzes": [
            {
                "id": "a1_pos_q1",
                "question": "'Wo ist ___ Tasche?' (die Tasche = sumka, seniki)",
                "options": ["deine", "dein", "deinen", "deinem"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: deine</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'Tasche' — ayol jinsi (die Tasche). Ayol jinsidagi otlar oldida egalik olmoshi <b>-e</b> oladi: <b>deine</b> Tasche."
                ),
                "wrong_explanations": {
                    1: "❌ 'dein' erkak yoki o'rta jins uchun.",
                    2: "❌ 'deinen' erkak jinsi Akkusativida.",
                    3: "❌ 'deinem' Dativ shakli."
                }
            },
            {
                "id": "a1_pos_q2",
                "question": "'Er sucht ___ Schlüssel.' (der Schlüssel = kalit, uning kaliti - Akkusativ)",
                "options": ["seinen", "sein", "seine", "ihren"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: seinen</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "1. 'er' ning egalik olmoshi <b>sein</b> bo'ladi.\n"
                    "2. 'Schlüssel' erkak jinsi (der Schlüssel) va bu yerda Akkusativda kelmoqda (Wen? Was? sucht er?).\n"
                    "3. Erkak jinsi Akkusativda <b>-en</b> oladi: er sucht <b>seinen</b> Schlüssel."
                ),
                "wrong_explanations": {
                    1: "❌ 'sein' Nominativ shakli.",
                    2: "❌ 'seine' ayol jinsi yoki ko'plik.",
                    3: "❌ 'ihren' bu ayol kishining kaliti bo'lardi."
                }
            }
        ]
    },
    {
        "id": "a1_praesens",
        "level": "A1",
        "title": "5. Fe'llarning Hozirgi Zamonda Tuslanishi (Präsens)",
        "keywords": ["fe'l", "tuslanish", "präsens", "konjugation", "ich du er sie es", "unregelmäßige verben"],
        "summary": "Muntazam va o'zak tovushi o'zgaruvchi fe'llarni xatosiz tuslash formulasi.",
        "content": (
            "📖 <b>5-MAVZU: Fe'llarning Hozirgi Zamonda Tuslanishi (Präsens)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• Muntazam qo'shimchalar: ich <b>-e</b>, du <b>-st</b>, er/sie/es <b>-t</b>, wir <b>-en</b>, ihr <b>-t</b>, sie/Sie <b>-en</b>.\n"
            "• Noqoidali fe'llarda faqat <b>du</b> va <b>er/sie/es</b> da o'zak unlisi o'zgaradi:\n"
            "  - e ➔ i: sprechen (du sprichst, er spricht), helfen (du hilfst)\n"
            "  - e ➔ ie: sehen (du siehst, er sieht), lesen (du liest)\n"
            "  - a ➔ ä: fahren (du fährst, er fährt), schlafen (du schläfst)\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Unli o'zgarishi 'Men'da ham, ko'plikda ham aslo bo'lmaydi! Faqat 'Sen' (du) va 'U' (er/sie/es) da bo'ladi!"
        ),
        "quizzes": [
            {
                "id": "a1_prs_q1",
                "question": "'Du ___ sehr gut Deutsch.' (sprechen)",
                "options": ["sprichst", "sprechst", "spricht", "spreche"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: sprichst</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "sprechen fe'lida du shaxsida 'e' harfi 'i' ga aylanadi va -st qo'shimchasi qo'shiladi: du <b>sprichst</b>."
                ),
                "wrong_explanations": {
                    1: "❌ 'sprechst' da unli o'zgarmagan.",
                    2: "❌ 'spricht' 3-shaxs (er/sie) uchun.",
                    3: "❌ 'spreche' ich uchun."
                }
            },
            {
                "id": "a1_prs_q2",
                "question": "'Er ___ nach Berlin.' (fahren)",
                "options": ["fährt", "fahrt", "fahre", "fahren"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: fährt</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "fahren fe'lida er shaxsida a ➔ ä umlaut oladi va -t qo'shiladi: er <b>fährt</b>."
                ),
                "wrong_explanations": {
                    1: "❌ 'fahrt' umlautsiz ihr (sizlar) uchun.",
                    2: "❌ 'fahre' ich uchun.",
                    3: "❌ 'fahren' infinitiv."
                }
            }
        ]
    },
    {
        "id": "a1_satzbau",
        "level": "A1",
        "title": "6. Nemis Tilida Gap Tuzilishi (Wortstellung: Temir Qonun)",
        "keywords": ["gap tuzilishi", "wortstellung", "fe'l o'rni", "verbposition", "ikkinchi o'rin"],
        "summary": "Nemis tilining bosh qonuni: Oddiy gapda tuslangan fe'l HAR DOIM 2-o'rinda turadi!",
        "content": (
            "📖 <b>6-MAVZU: Gap Tuzilishi (Wortstellung im Hauptsatz)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Bosh gapda (Hauptsatz) <b>TUSLANGAN FE'L HAR DOIM 2-O'RINDA</b> turadi!\n"
            "• To'g'ri tartib: <i>Ich</i> <b>lerne</b> heute Deutsch.\n"
            "• Teskari tartib: <i>Heute</i> <b>lerne</b> ich Deutsch. (Vaqt oldinga chiqsa ham fe'l 2-o'rinda qoladi!)\n\n"
            "🔹 <b>So'roq gaplar:</b>\n"
            "• W-Fragen (So'roq so'zli): Wo <b>wohnst</b> du? (Fe'l 2-o'rinda)\n"
            "• Ja/Nein-Fragen (So'roq so'zsiz): <b>Lernst</b> du Deutsch? (Fe'l 1-o'rinda)\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Fe'l — har doim 2-raqamli kresloda o'tiruvchi VIP mehmon!"
        ),
        "quizzes": [
            {
                "id": "a1_satz_q1",
                "question": "Quyidagi gaplardan qaysi biri grammatik jihatdan MUTLAQO TO'G'RI?",
                "options": [
                    "Am Wochenende spiele ich Fußball.",
                    "Am Wochenende ich spiele Fußball.",
                    "Ich spiele am Wochenende nicht Fußball gestern.",
                    "Spiele am Wochenende ich Fußball."
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Am Wochenende spiele ich Fußball.</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "1. 'Am Wochenende' (1-o'rin) + 2. 'spiele' (fe'l 2-o'rinda) + 3. 'ich' (ega 3-o'rinda)."
                ),
                "wrong_explanations": {
                    1: "❌ 'Am Wochenende ich spiele...' da fe'l 3-o'ringa tushib qolgan.",
                    2: "❌ Vaqtlar mantiqsiz.",
                    3: "❌ Bu so'roq gap shakliga o'xshab qolgan."
                }
            }
        ]
    },
    {
        "id": "a1_akkusativ",
        "level": "A1",
        "title": "7. Akkusativ Kelishigi (Tushum kelishigi: der ➔ den siri)",
        "keywords": ["akkusativ", "tushum", "kelishik", "der den", "wen was", "einen"],
        "summary": "Kimni? Nimani? so'rog'i va erkak jinsining sehrli o'zgarishi.",
        "content": (
            "📖 <b>7-MAVZU: Akkusativ Kelishigi (Wen? Was? - Kimni? Nimani?)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Akkusativda FAQAT <b>ERKAK JINSI (Maskulin)</b> o'zgaradi! Qolgan barcha jinslar o'zgarmaydi!\n"
            "• Erkak: <b>der ➔ den</b> | <b>ein ➔ einen</b> | <b>kein ➔ keinen</b>\n"
            "• Ayol: <b>die ➔ die</b> | <b>eine ➔ eine</b> (O'zgarmaydi)\n"
            "• O'rta: <b>das ➔ das</b> | <b>ein ➔ ein</b> (O'zgarmaydi)\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Akkusativ erkaklar jinsini <b>N</b>ishonga oladi (de<b>n</b>, eine<b>n</b>)!"
        ),
        "quizzes": [
            {
                "id": "a1_akk_q1",
                "question": "Ich habe ___ Apfel. (der Apfel = olma)",
                "options": ["einen", "ein", "eine", "einer"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: einen</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'haben' Akkusativ talab qiladi. Erkak jinsi Akkusativda <b>einen</b> bo'ladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'ein' faqat das yoki Nominativ der uchun.",
                    2: "❌ 'eine' ayol jinsi uchun.",
                    3: "❌ 'einer' Dativ/Genitiv."
                }
            },
            {
                "id": "a1_akk_q2",
                "question": "'Ich trinke ___ Tee und esse ___ Suppe.' (der Tee, die Suppe)",
                "options": ["den / die", "der / die", "den / den", "das / eine"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: den / die</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Tee (maskulin) ➔ <b>den</b>. Suppe (feminin) Akkusativda o'zgarmasdan <b>die</b> qoladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'der / die' da Tee Akkusativga o'tmagan.",
                    2: "❌ 'den / den' Suppe erkak jinsi emas.",
                    3: "❌ 'das / eine' choy das emas."
                }
            }
        ]
    },
    {
        "id": "a1_dativ",
        "level": "A1",
        "title": "8. Dativ Kelishigi (Wem? - Kimga? Qayerda?)",
        "keywords": ["dativ", "kelishik", "dem der dem den", "wem", "kimga"],
        "summary": "Kimga? Nimaga? so'rog'i va Dativdagi qat'iy artikl o'zgarishlari.",
        "content": (
            "📖 <b>8-MAVZU: Dativ Kelishigi (Wem? - Kimga?)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Dativ shaxsga qaratilgan harakatda ishlatiladi.\n"
            "• Erkak: <b>dem</b> (einem)\n"
            "• O'rta: <b>dem</b> (einem)\n"
            "• Ayol: <b>der</b> (einer) ⚠️ (Ayol jinsi 'der' ga aylanadi!)\n"
            "• Ko'plik: <b>den + (-n)</b>\n\n"
            "🔹 Asosiy fe'llar: <b>helfen</b> (yordam bermoq), <b>danken</b> (rahmat aytmoq), <b>gefallen</b> (yoqmoq), <b>gehören</b> (tegishli bo'lmoq).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> M - R - M - N (dem, der, dem, den)!"
        ),
        "quizzes": [
            {
                "id": "a1_dat_q1",
                "question": "'Ich helfe ___ Frau.' (die Frau)",
                "options": ["der", "die", "dem", "den"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: der</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'helfen' Dativ talab qiladi. Ayol jinsi Dativda 'die' dan <b>der</b> ga aylanadi: Ich helfe <b>der</b> Frau."
                ),
                "wrong_explanations": {
                    1: "❌ 'die' Nominativ/Akkusativ.",
                    2: "❌ 'dem' erkak/o'rta jins.",
                    3: "❌ 'den' ko'plik."
                }
            }
        ]
    },
    {
        "id": "a1_modalverben",
        "level": "A1",
        "title": "9. Modal Fe'llar (können, müssen, dürfen, wollen, sollen, möchten)",
        "keywords": ["modal fe'llar", "können", "müssen", "dürfen", "wollen", "sollen", "möchten", "modalverben"],
        "summary": "Modal fe'llarning ma'nosi, tuslanishi va ikkinchi fe'lni gap oxiriga itarish qoidasi.",
        "content": (
            "📖 <b>9-MAVZU: Modal Fe'llar (Modalverben)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Modal fe'l 2-o'rinda tuslanadi, asosiy fe'l Infinitivda gapning ENG OXIRIGA boradi!\n"
            "• ich va er/sie/es bir xil va qo'shimchasiz bo'ladi: ich <b>kann</b>, er <b>kann</b>.\n"
            "• können (qila olmoq), müssen (majbur bo'lmoq), dürfen (ruxsat), wollen (xohlamoq), sollen (maslahat/buyruq)."
        ),
        "quizzes": [
            {
                "id": "a1_mod_q1",
                "question": "'Er ___ heute lange arbeiten.' (müssen)",
                "options": ["muss", "müsst", "musst", "mussen"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: muss</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "3-shaxs birlikda (er) modal fe'llar qo'shimcha olmaydi va umlautni yo'qotadi: er <b>muss</b>."
                ),
                "wrong_explanations": {
                    1: "❌ 'müsst' ihr uchun.",
                    2: "❌ 'musst' du uchun.",
                    3: "❌ 'mussen' so'zi yo'q."
                }
            }
        ]
    },
    {
        "id": "a1_trennbare",
        "level": "A1",
        "title": "10. Ajraladigan va Ajralmaydigan Fe'llar (Trennbare & Untrennbare)",
        "keywords": ["ajraladigan fe'l", "trennbare verben", "prefiks", "old qo'shimcha", "aufstehen", "einkaufen"],
        "summary": "Prefiks qachon gap oxiriga uchib ketadi va qachon ajralmaydi?",
        "content": (
            "📖 <b>10-MAVZU: Ajraladigan Fe'llar (Trennbare Verben)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• Urg'uli prefikslar (ab-, an-, auf-, aus-, ein-, mit-, vor-, zu-) gap oxiriga ketadi: Ich <b>stehe</b> um 7 Uhr <b>auf</b>.\n"
            "• Ajralmaydiganlar (be-, ge-, er-, ver-, zer-, ent-, emp-, miss-) hech qachon ajralmaydi: Ich <b>verstehe</b> dich."
        ),
        "quizzes": [
            {
                "id": "a1_trn_q1",
                "question": "'Ich ___ jeden Morgen um 6 Uhr ___.' (aufstehen)",
                "options": ["stehe / auf", "aufstehe / -", "stehe auf / -", "auf / stehe"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: stehe / auf</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "aufstehen fe'li ajraladi: Ich <b>stehe</b> ... <b>auf</b>."
                ),
                "wrong_explanations": {
                    1: "❌ 'aufstehe' prefiks ajralishi shart.",
                    2: "❌ 'stehe auf' prefiks oxirga ketishi shart.",
                    3: "❌ Prefiks 2-o'rinda bo'lmaydi."
                }
            }
        ]
    },
    {
        "id": "a1_nicht_kein",
        "level": "A1",
        "title": "11. Inkor Qilish Siri ('nicht' va 'kein' farqi)",
        "keywords": ["nicht", "kein", "inkor", "negation", "inkor qilish"],
        "summary": "Qachon 'nicht', qachon 'kein'? Bir soniyada to'g'ri tanlash formulasi.",
        "content": (
            "📖 <b>11-MAVZU: Inkor Qilish ('nicht' va 'kein')</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• <b>KEIN:</b> Noaniq artiklli (ein) yoki artiklsiz otlarni inkor qilganda: Das ist <b>kein</b> Auto.\n"
            "• <b>NICHT:</b> Fe'l, sifat yoki aniq artiklli otlarni inkor qilganda: Ich schlafe <b>nicht</b>. Das Auto ist <b>nicht</b> teuer."
        ),
        "quizzes": [
            {
                "id": "a1_nk_q1",
                "question": "'Ich verstehe das Wort ___.'",
                "options": ["nicht", "kein", "keine", "keinen"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: nicht</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'das Wort' oldida ANIQ ARTIKL bor, shuning uchun 'nicht' ishlatiladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'kein' aniq artikl bilan ishlatilmaydi.",
                    2: "❌ 'keine' ayol jinsi uchun.",
                    3: "❌ 'keinen' maskulin akkusativ."
                }
            }
        ]
    },
    {
        "id": "a1_imperativ",
        "level": "A1",
        "title": "12. Buyruq Mayli (Imperativ: Du, Ihr, Sie shakllari)",
        "keywords": ["imperativ", "buyruq mayli", "komm", "macht", "kommen sie"],
        "summary": "Keling, qiling, bor! Buyruq va iltimos shakllarini to'g'ri yasash.",
        "content": (
            "📖 <b>12-MAVZU: Buyruq Mayli (Imperativ)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• <b>Du</b> uchun: du va -st tushib qoladi (Komm! Mach! Fahr!)\n"
            "• <b>Ihr</b> uchun: ihr tushib qoladi (Kommt! Macht!)\n"
            "• <b>Sie</b> uchun: fe'l oldinga chiqadi (Kommen Sie bitte!)"
        ),
        "quizzes": [
            {
                "id": "a1_imp_q1",
                "question": "Do'stingizga 'Tezroq hayda!' (fahren) deb buyurmoqchisiz. Qaysi shakl to'g'ri?",
                "options": ["Fahr schneller!", "Fährst schneller!", "Fahre du schneller!", "Fahrt du schneller!"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Fahr schneller!</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "du buyrug'ida olmosh va -st tushib qoladi, 'a' dagi umlaut yo'qoladi: du fährst ➔ <b>Fahr!</b>"
                ),
                "wrong_explanations": {
                    1: "❌ 'Fährst' umlaut va -st qolmaydi.",
                    2: "❌ 'Fahre du' du aytilmaydi.",
                    3: "❌ 'Fahrt du' xato."
                }
            }
        ]
    }
]
