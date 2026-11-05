"""
B1 DARAJASI GRAMMATIKA MAVZULARI (RASMIY DUDEN & CEFR / GeR STANDARTI)
"""

B1_TOPICS = [
    {
        "id": "b1_konjunktiv2",
        "level": "B1",
        "title": "1. Konjunktiv II: Orzu, Xayol va Muloyimlik (hätte, wäre, würde)",
        "keywords": ["konjunktiv 2", "würde", "hätte", "wäre", "orzu", "tilak", "muloyimlik", "wenn ich reich wäre"],
        "summary": "Real bo'lmagan dunyo: 'Agar boy bo'lganimda...' yoki 'Iltimos, yordam bera olarmidingiz?'.",
        "content": (
            "📖 <b>1-MAVZU: Konjunktiv II (Hozirgi va Kelasi zamonda)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR B1 Standarti:</b>\n"
            "Konjunktiv II xayoliy orzu, shart yoki o'ta muloyim takliflarni bildiradi:\n"
            "1. <b>haben ➔ hätte:</b> <i>Wenn ich Zeit <b>hätte</b>...</i> (Vaqtim bo'lganida...)\n"
            "2. <b>sein ➔ wäre:</b> <i>Wenn ich reich <b>wäre</b>...</i> (Boy bo'lganimda...)\n"
            "3. <b>Barcha fe'llar uchun: würde + Infinitiv:</b> <i>Ich <b>würde</b> gerne ein Auto kaufen.</i>\n"
            "4. <b>können ➔ könnte:</b> <i><b>Könntest</b> du mir bitte helfen?</i>\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> O'zbek tilidagi '-sa edi' yoki '-gan bo'lardim' aynan Konjunktiv II dir!"
        ),
        "quizzes": [
            {
                "id": "b1_k2_q1",
                "question": "'Wenn ich Zeit ___, ___ ich dir helfen.' (hätte / würde)",
                "options": ["hätte / würde", "habe / werde", "hatte / wollte", "wäre / hätte"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: hätte / würde</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "haben fe'lining Konjunktiv II shakli <b>hätte</b>, asosiy fe'l bilan esa <b>würde + helfen</b> ishlatiladi."
                ),
                "wrong_explanations": {
                    1: "❌ Indikativ haqiqiy shart shakli.",
                    2: "❌ Oddiy o'tgan zamon.",
                    3: "❌ 'wäre' vaqt bo'lganimda bo'lib qoladi."
                }
            }
        ]
    },
    {
        "id": "b1_relativsaetze",
        "level": "B1",
        "title": "2. Nisbiy Ergash Gaplar (Relativsätze: der, die, das, dessen, deren)",
        "keywords": ["relativsatz", "nisbiy gap", "qaysiki", "dessen", "deren", "denen", "relativpronomen"],
        "summary": "'Men kecha ko'rgan odam...' — shaxs yoki narsani aniqlab beruvchi zanjir.",
        "content": (
            "📖 <b>2-MAVZU: Nisbiy Ergash Gaplar (Relativsätze)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Bosh gapdagi otni aniqlovchi ergash gap. Ergash gap bo'lgani uchun <b>FE'L HAR DOIM ENG OXIRIDA</b> turadi!\n"
            "• Nominativ: der, die, das, die\n"
            "• Akkusativ: <b>den</b>, die, das, die\n"
            "• Dativ: dem, der, dem, <b>denen</b> (ko'plikda denen!)\n"
            "• Genitiv: <b>dessen</b> (mask/neutr) | <b>deren</b> (fem/plural)"
        ),
        "quizzes": [
            {
                "id": "b1_rel_q1",
                "question": "'Das ist der Kollege, ___ ich das Buch gegeben habe.'",
                "options": ["dem", "den", "der", "dessen"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: dem</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Erkak jinsiga (der Kollege) Dativda (Wem? - Kimga berdim?) nisbiy olmosh <b>dem</b> bo'ladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'den' Akkusativ.",
                    2: "❌ 'der' Nominativ.",
                    3: "❌ 'dessen' Genitiv."
                }
            }
        ]
    },
    {
        "id": "b1_zu_infinitiv",
        "level": "B1",
        "title": "3. Infinitiv bilan 'zu' va 'um... zu', 'ohne... zu', 'statt... zu'",
        "keywords": ["infinitiv zu", "um zu", "ohne zu", "statt zu", "fe'l infinitiv", "maqsad"],
        "summary": "Qachon 'zu' qo'yiladi, qachon qo'yilmaydi? 'uchun', 'qilmasdan' tuzilmalari.",
        "content": (
            "📖 <b>3-MAVZU: Infinitiv Konstruksiyalari (zu / um... zu / ohne... zu)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• <b>Es ist wichtig, Deutsch zu lernen.</b>\n"
            "• <b>um ... zu + Infinitiv:</b> Maqsad (-ish uchun): <i>Ich lerne Deutsch, <b>um</b> in Deutschland <b>zu</b> studieren.</i>\n"
            "• <b>ohne ... zu + Infinitiv:</b> Qilmasdan: <i>Er ging, <b>ohne</b> tschüss <b>zu</b> sagen.</i>\n"
            "• <b>(an)statt ... zu + Infinitiv:</b> O'rniga: <i>Er schläft, <b>statt zu</b> lernen.</i>\n\n"
            "⚠️ <i>Modal fe'llardan keyin 'zu' QO'YILMAYDI! (Ich kann schwimmen).</i>"
        ),
        "quizzes": [
            {
                "id": "b1_inf_q1",
                "question": "'Er arbeitet viel, ___ seiner Familie ein schönes Leben ___ ermöglichen.'",
                "options": ["um / zu", "ohne / zu", "statt / zu", "damit / zu"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: um / zu</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Maqsad infinitiv konstruksiyasi doimo <b>um ... zu + Infinitiv</b> bo'ladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'ohne' qilmasdan ma'nosi.",
                    2: "❌ 'statt' o'rniga.",
                    3: "❌ damit shaxsli gap talab qiladi, 'zu' olmaydi."
                }
            }
        ]
    },
    {
        "id": "b1_genitiv",
        "level": "B1",
        "title": "4. Genitiv Kelishigi va Genitiv Ko'makchilari (wegen, während, trotz)",
        "keywords": ["genitiv", "qaratqich", "wessen", "des es", "wegen", "während", "trotz", "statt"],
        "summary": "Kimning? Nimaning? Otning oxiriga -s/-es qo'shilishi va 4 ta muhim ko'makchi.",
        "content": (
            "📖 <b>4-MAVZU: Genitiv Kelishigi (Wessen? - Kimning?)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• Erkak va O'rta: <b>des</b> Mann<b>es</b> / <b>des</b> Kind<b>es</b> (Ot oxiriga -(e)s oladi!)\n"
            "• Ayol va Ko'plik: <b>der</b> Frau / <b>der</b> Kinder\n"
            "🔹 4 ta buyuk Genitiv ko'makchisi:\n"
            "1. <b>wegen</b> (tufayli): wegen des Wetters\n"
            "2. <b>während</b> (davomida): während der Pause\n"
            "3. <b>trotz</b> (qaramasdan): trotz des Regens\n"
            "4. <b>(an)statt</b> (o'rniga): statt eines Autos"
        ),
        "quizzes": [
            {
                "id": "b1_gen_q1",
                "question": "'Wegen ___ (der Sturm) fällt der Flug aus.'",
                "options": ["des Sturmes", "dem Sturm", "den Sturm", "des Sturm"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: des Sturmes</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'wegen' Genitiv talab qiladi. der Sturm ➔ <b>des Sturmes</b>."
                ),
                "wrong_explanations": {
                    1: "❌ dem Sturm og'zaki tildagi noto'g'ri shakl.",
                    2: "❌ Akkusativ.",
                    3: "❌ Ot oxiridagi -es tushib qolgan."
                }
            }
        ]
    },
    {
        "id": "b1_verben_praepositionen",
        "level": "B1",
        "title": "5. Fe'llarning Boshqaruvi va Pronominaladverbien (worauf, darauf)",
        "keywords": ["verben mit präpositionen", "worauf", "darauf", "wovon", "davon", "fe'l boshqaruvi"],
        "summary": "warten auf, sich freuen über/auf va narsalarga nisbatan worauf/darauf birikmalari.",
        "content": (
            "📖 <b>5-MAVZU: Fe'llarning Boshqaruvi va Pronominaladverbien</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR B1 Standarti:</b>\n"
            "Nemis tilidagi ko'plab fe'llar qat'iy bir ko'makchi bilan ishlatiladi:\n"
            "• <b>warten auf + Akkusativ:</b> kutmoq (Ich warte auf den Bus)\n"
            "• <b>träumen von + Dativ:</b> orzu qilmoq (Ich träume von einer Reise)\n"
            "• <b>sich interessieren für + Akkusativ:</b> qiziqmoq\n"
            "• <b>denken an + Akkusativ:</b> o'ylamoq\n\n"
            "🔥 <b>Narsa va Shaxs farqi (Pronominaladverbien):</b>\n"
            "1. <b>Shaxs bo'lsa:</b> Ko'makchi + Olmosh (Auf wen wartest du? — Ich warte auf <i>ihn</i>).\n"
            "2. <b>Narsa bo'lsa:</b> <b>wo(r) + Ko'makchi</b> va <b>da(r) + Ko'makchi</b>:\n"
            "   • <b>Worauf</b> wartest du? ➔ Ich warte <b>darauf</b>. (Nimani kutyapsan? — Shuni kutyapman).\n"
            "   • <b>Wovon</b> träumst du? ➔ Ich träume <b>davon</b>."
        ),
        "quizzes": [
            {
                "id": "b1_vprp_q1",
                "question": "'___ wartest du? — Auf den Bus.' (Narsaga nisbatan qaysi so'roq so'zi ishlatiladi?)",
                "options": ["Worauf", "Auf wen", "Woran", "Wovon"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Worauf</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'warten' auf ko'makchisini oladi. Narsa (avtobus) haqida so'ralganda 'wo + r + auf' = <b>Worauf</b> bo'ladi. Agar odam bo'lsa 'Auf wen' bo'lardi."
                ),
                "wrong_explanations": {
                    1: "❌ 'Auf wen' odamlar uchun (Auf wen wartest du? - Auf meinen Bruder).",
                    2: "❌ 'Woran' denken an uchun.",
                    3: "❌ 'Wovon' träumen von uchun."
                }
            }
        ]
    },
    {
        "id": "b1_plusquamperfekt",
        "level": "B1",
        "title": "6. Plusquamperfekt va 'nachdem' Bog'lovchisi (O'tgan zamondan oldingi zamon)",
        "keywords": ["plusquamperfekt", "nachdem", "vorzeitigkeit", "hatte gemacht", "war gegangen"],
        "summary": "O'tmishdagi ikkita voqeadan oldinroq sodir bo'lganini ko'rsatish formulasi.",
        "content": (
            "📖 <b>6-MAVZU: Plusquamperfekt va nachdem</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Plusquamperfekt — o'tgan zamondagi boshqa bir harakatdan ham oldin sodir bo'lgan harakatni bildiradi.\n"
            "<b>Formulasi:</b> <b>hatte / war</b> + ... + <b>Partizip II</b>\n"
            "• <i>Nachdem er gegessen <b>hatte</b>, ging er spazieren.</i>\n"
            "  (U ovqatlanib bo'lganidan so'ng, sayrga chiqdi — avval ovqatlangan!).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> 'nachdem' qismida Plusquamperfekt (hatte/war + PII), asosiy gapda esa Präteritum bo'ladi!"
        ),
        "quizzes": [
            {
                "id": "b1_pluq_q1",
                "question": "'Nachdem er die Hausaufgaben gemacht ___, ging er ins Bett.'",
                "options": ["hatte", "hat", "habe", "wäre"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: hatte</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Asosiy gap o'tgan zamonda (ging - Präteritum). 'nachdem' ergash gapida undan oldin sodir bo'lgan harakat Plusquamperfektda bo'lishi shart: gemacht <b>hatte</b>."
                ),
                "wrong_explanations": {
                    1: "❌ 'hat' hozirgi/Perfekt shakli, zamonlar moslashuvi buziladi.",
                    2: "❌ 'habe' 1-shaxs hozirgi zamon.",
                    3: "❌ machen fe'li sein/wäre olmaydi."
                }
            }
        ]
    },
    {
        "id": "b1_passiv_komplett",
        "level": "B1",
        "title": "7. Majhul Nisbatning Barcha Zamonlari (Vorgangspassiv)",
        "keywords": ["passiv alle zeiten", "wurde gebaut", "ist gebaut worden", "majhul zamonlar"],
        "summary": "Passivni Präteritum, Perfekt va modal fe'llar bilan to'liq qo'llash.",
        "content": (
            "📖 <b>7-MAVZU: Majhul Nisbatning Barcha Zamonlari (Passiv)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "1. <b>Präsens:</b> Das Haus <b>wird gebaut</b>.\n"
            "2. <b>Präteritum:</b> Das Haus <b>wurde gebaut</b>. (wurde + PII)\n"
            "3. <b>Perfekt:</b> Das Haus <b>ist gebaut worden</b>. (ist ... worden)\n"
            "4. <b>Modal fe'l bilan:</b> Das Haus <b>muss gebaut werden</b>.\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> Perfekt Passivda 'geworden' emas, faqat <b>worden</b> ishlatiladi!"
        ),
        "quizzes": [
            {
                "id": "b1_pascomp_q1",
                "question": "'Die Schule ___ im Jahr 1990 gebaut.' (Präteritum Passiv)",
                "options": ["wurde", "worden", "wird", "ist"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: wurde</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "1990 yil o'tib ketgan o'tmish. Passiv Präteritum formulasi: <b>wurde + Partizip II</b> (wurde gebaut)."
                ),
                "wrong_explanations": {
                    1: "❌ 'worden' yordamchi fe'lsiz ishlatilmaydi.",
                    2: "❌ 'wird' hozirgi zamon.",
                    3: "❌ 'ist' bilan worden kerak bo'lardi."
                }
            }
        ]
    },
    {
        "id": "b1_doppelkonnektoren",
        "level": "B1",
        "title": "8. Ikki Qismli Bog'lovchilar (Doppelkonnektoren)",
        "keywords": ["doppelkonnektoren", "sowohl als auch", "nicht nur sondern auch", "weder noch", "je desto"],
        "summary": "sowohl... als auch, weder... noch, je... desto — nutqni boyituvchi juftliklar.",
        "content": (
            "📖 <b>8-MAVZU: Ikki Qismli Bog'lovchilar (Doppelkonnektoren)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• <b>sowohl ... als auch:</b> ham ... ham (Er spricht sowohl Deutsch als auch Englisch)\n"
            "• <b>nicht nur ... sondern auch:</b> nafaqat ... balki ... ham\n"
            "• <b>weder ... noch:</b> na ... va na ... (Ich trinke weder Kaffee noch Tee)\n"
            "• <b>entweder ... oder:</b> yo ... yoki\n"
            "• <b>je ... desto:</b> qanchalik ... shunchalik"
        ),
        "quizzes": [
            {
                "id": "b1_dop_q1",
                "question": "'Je mehr Bücher man liest, ___ klüger wird man.'",
                "options": ["desto", "als", "und", "denn"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: desto</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'Je' komparativining ikkinchi qismi doimo <b>desto</b> (yoki umso) bilan davom etadi."
                ),
                "wrong_explanations": {
                    1: "❌ 'als' taqqoslashda ishlatiladi.",
                    2: "❌ 'und' ma'nosiz.",
                    3: "❌ 'denn' sabab bog'lovchisi."
                }
            }
        ]
    },
    {
        "id": "b1_obwohl_trotzdem",
        "level": "B1",
        "title": "9. Zidlik Bog'lovchilari: obwohl vs trotzdem",
        "keywords": ["obwohl", "trotzdem", "garchi", "shunga qaramay", "konzessiv"],
        "summary": "Ikkalasi ham zidlik bildiradi, lekin fe'l o'rni tubdan farq qiladi!",
        "content": (
            "📖 <b>9-MAVZU: obwohl va trotzdem farqi</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• <b>obwohl:</b> Ergash gap bog'lovchisi ➔ FE'LNI ENG OXIRIGA SURADI!\n"
            "  <i>Er geht spazieren, <b>obwohl</b> es stark <b>regnet</b>.</i>\n"
            "• <b>trotzdem:</b> 1-o'rinda keladi ➔ FE'L DARHOL 2-O'RINDA KELADI!\n"
            "  <i>Es regnet stark. <b>Trotzdem geht</b> er spazieren.</i>"
        ),
        "quizzes": [
            {
                "id": "b1_obw_q1",
                "question": "'Er ist müde. ___, lernt er weiter.'",
                "options": ["Trotzdem", "Obwohl", "Weil", "Dass"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Trotzdem</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Fe'l (lernt) darhol 2-o'rinda turibdi. Shuning uchun <b>Trotzdem</b> to'g'ri."
                ),
                "wrong_explanations": {
                    1: "❌ 'Obwohl' bo'lsa fe'l gap oxiriga ketishi kerak edi.",
                    2: "❌ 'Weil' sabab bildiradi.",
                    3: "❌ 'Dass' to'ldiruvchi gap."
                }
            }
        ]
    }
]
