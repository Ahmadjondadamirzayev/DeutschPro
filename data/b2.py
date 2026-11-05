"""
B2 DARAJASI GRAMMATIKA MAVZULARI (RASMIY DUDEN & CEFR / GeR STANDARTI)
"""

B2_TOPICS = [
    {
        "id": "b2_konjunktiv2_vergangenheit",
        "level": "B2",
        "title": "1. O'tgan Zamondagi Konjunktiv II (Hätte/Wäre + Partizip II)",
        "keywords": ["konjunktiv 2 vergangenheit", "hätte gewesen", "wäre gegangen", "afsus", "o'tib ketgan imkoniyat"],
        "summary": "'Agar kecha kelganingda edi...' — ortga qaytmas o'tmish afsusi.",
        "content": (
            "📖 <b>1-MAVZU: Konjunktiv II O'tgan Zamonda (Irreale Vergangenheit)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR B2 Standarti:</b>\n"
            "O'tmishda sodir bo'lmagan, endi o'zgartirib bo'lmaydigan voqealar bo'yicha afsus yoki nohaqiy shartni bildiradi.\n"
            "<b>Formulasi:</b> <b>hätte / wäre</b> + ... + <b>Partizip II</b>\n"
            "• <i>Wenn ich mehr gelernt <b>hätte</b>, <b>hätte</b> ich die Prüfung <b>bestanden</b>.</i>\n"
            "• <i>Wenn er pünktlich gekommen <b>wäre</b>, <b>wären</b> wir nicht zu spät <b>gekommen</b>.</i>\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> Xuddi Perfektga o'xshaydi, faqat 'hat' o'rniga <b>hätte</b>, 'ist' o'rniga <b>wäre</b> qo'yiladi!"
        ),
        "quizzes": [
            {
                "id": "b2_k2v_q1",
                "question": "'Hättest du mich angerufen, ___ ich dir gerne geholfen.'",
                "options": ["hätte", "würde", "hatte", "wäre"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: hätte</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'helfen' Perfektda haben oladi. O'tgan zamon Konjunktiv II shakli <b>hätte + geholfen</b> bo'ladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'würde' faqat hozirgi/kelasi zamonda ishlatiladi.",
                    2: "❌ 'hatte' indikativ.",
                    3: "❌ 'wäre' helfen bilan kelmaydi."
                }
            }
        ]
    },
    {
        "id": "b2_zustandspassiv",
        "level": "B2",
        "title": "2. Holat Majhul Nisbati (Zustandspassiv: sein + Partizip II)",
        "keywords": ["zustandspassiv", "ist geöffnet", "ist repariert", "holat majhul nisbati"],
        "summary": "Jarayon emas, balki ish tugagandan keyingi tayyor holatni ifodalash.",
        "content": (
            "📖 <b>2-MAVZU: Zustandspassiv (Holat Majhul Nisbati)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR B2 Standarti:</b>\n"
            "• <b>Vorgangspassiv (Jarayon): werden + Partizip II</b>\n"
            "  <i>Die Tür <b>wird geschlossen</b>.</i> (Eshik yopilyapti — kimdir hozir yopyapti).\n"
            "• <b>Zustandspassiv (Tayyor holat / Natija): sein + Partizip II</b>\n"
            "  <i>Die Tür <b>ist geschlossen</b>.</i> (Eshik yopiq — harakat allaqachon tugagan, hozirgi holat shunday).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b> 'wird' ko'rsangiz film kabi jarayon ketyapti, 'ist' ko'rsangiz rasm kabi holat qotib turibdi!"
        ),
        "quizzes": [
            {
                "id": "b2_zpas_q1",
                "question": "'Das Geschäft ___ um 20 Uhr geschlossen.' (Hozir do'kon yopiq holatda turibdi)",
                "options": ["ist", "wird", "hat", "sein"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ist</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Holat majhul nisbati (Zustandspassiv) <b>sein + Partizip II</b> bilan yasaladi: Das Geschäft <b>ist</b> geschlossen."
                ),
                "wrong_explanations": {
                    1: "❌ 'wird' do'kon ayni daqiqada yopilayotgan jarayonni bildiradi.",
                    2: "❌ 'hat' passiv bo'la olmaydi.",
                    3: "❌ 'sein' tuslanmagan."
                }
            }
        ]
    },
    {
        "id": "b2_passivalternativen",
        "level": "B2",
        "title": "3. Passiv O'rinbosarlari (sich lassen, sein zu, -bar, -lich)",
        "keywords": ["passivalternativen", "sich lassen", "sein zu", "machbar", "passiv o'rniga"],
        "summary": "Passiv so'zini ishlatmasdan Passiv ma'nosini beruvchi konstruksiyalar.",
        "content": (
            "📖 <b>3-MAVZU: Passiv O'rinbosarlari (Passivalternativen)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "1. <b>sich lassen + Infinitiv:</b> (= kann gemacht werden - mumkinlik)\n"
            "   <i>Das Problem <b>lässt sich lösen</b>.</i> (= Das Problem kann gelöst werden).\n"
            "2. <b>sein + zu + Infinitiv:</b> (= muss/kann gemacht werden - majburiyat/imkoniyat)\n"
            "   <i>Die Aufgabe <b>ist</b> bis morgen <b>zu machen</b>.</i> (= muss gemacht werden).\n"
            "3. <b>-bar / -lich suffikslari:</b> lös<b>bar</b> (yechsa bo'ladigan), verständ<b>lich</b>."
        ),
        "quizzes": [
            {
                "id": "b2_pasalt_q1",
                "question": "'Das Auto lässt sich nicht mehr reparieren' nimani anglatadi?",
                "options": [
                    "Das Auto kann nicht mehr repariert werden",
                    "Das Auto will nicht repariert werden",
                    "Man muss das Auto reparieren",
                    "Das Auto hat sich selbst repariert"
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ...kann nicht mehr repariert werden.</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'sich lassen + Infinitiv' = 'können + Passiv' ekvivalentidir."
                ),
                "wrong_explanations": {
                    1: "❌ Mashina irodaga ega emas.",
                    2: "❌ Majburiyat emas, imkoniyat.",
                    3: "❌ O'zlik fe'li emas."
                }
            }
        ]
    },
    {
        "id": "b2_n_deklination",
        "level": "B2",
        "title": "4. N-Deklination (Kuchsiz Otlarning Turlanishi)",
        "keywords": ["n-deklination", "schwache nomen", "der herr", "der junge", "des herrn", "dem studenten"],
        "summary": "Nega 'Ich kenne den Student' emas, balki 'den Studenten' bo'ladi?",
        "content": (
            "📖 <b>4-MAVZU: N-Deklination (Kuchsiz Otlar)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Erkak jinsidagi ba'zi otlar <b>faqat Nominativdan tashqari barcha kelishiklarda</b> birlikda ham <b>-(e)n</b> oladi!\n"
            "• -e bilan tugagan erkak jonzotlar: der Junge, der Kollege, der Kunde, der Löwe\n"
            "• Chet tildan kirgan kasblar (-ent, -ist, -at): der Student, der Polizist, der Diplomat\n"
            "• Muhim so'zlar: der Herr (des Herrn), der Mensch (des Menschen), der Nachbar."
        ),
        "quizzes": [
            {
                "id": "b2_ndek_q1",
                "question": "'Ich habe mit einem neuen ___ gesprochen.' (der Kunde = mijoz)",
                "options": ["Kunden", "Kunde", "Kundes", "Kunder"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Kunden</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "der Kunde N-Deklination ga mansub. Dativda oxiriga <b>-n</b> oladi: mit einem neuen <b>Kunden</b>."
                ),
                "wrong_explanations": {
                    1: "❌ 'Kunde' Nominativda qolib ketgan.",
                    2: "❌ N-Deklination hech qachon -s olmaydi.",
                    3: "❌ Kunder xato."
                }
            }
        ]
    },
    {
        "id": "b2_partizipien",
        "level": "B2",
        "title": "5. Sifatdoshlar (Partizip I va Partizip II sifat o'rnida)",
        "keywords": ["partizip 1", "partizip 2", "sifatdosh", "das weinende kind", "das gelesene buch"],
        "summary": "Yig'layotgan bola (Partizip I) va yozilgan kitob (Partizip II) farqi.",
        "content": (
            "📖 <b>5-MAVZU: Sifatdoshlar (Partizip I va Partizip II)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "1. <b>PARTIZIP I (Hozir ro'y berayotgan aktiv harakat):</b> Infinitiv + <b>-d</b> + sifat qo'shimchasi\n"
            "   • weinen ➔ das weinen<b>de</b> Kind (yig'layotgan bola)\n"
            "   • kochen ➔ das kochen<b>de</b> Wasser (qaynayotgan suv)\n"
            "2. <b>PARTIZIP II (Tugallangan passiv natija):</b>\n"
            "   • schreiben ➔ der geschrieb<b>ene</b> Brief (yozilgan xat)\n"
            "   • reparieren ➔ das reparier<b>te</b> Auto (ta'mirlangan mashina)"
        ),
        "quizzes": [
            {
                "id": "b2_part_q1",
                "question": "'Die ___ Sonne scheint warm.' (aufgehen = chiqmoq/ko'tarilmoq - chiqayotgan quyosh)",
                "options": ["aufgehende", "aufgegangene", "aufgeht", "aufzugehende"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: aufgehende</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Ayni damda chiqayotgan quyosh uchun Partizip I (Infinitiv + d) kerak: aufgehen + d + e = <b>aufgehende</b>."
                ),
                "wrong_explanations": {
                    1: "❌ 'aufgegangene' allaqachon chiqib bo'lgan quyosh.",
                    2: "❌ 'aufgeht' fe'l shakli.",
                    3: "❌ Gerundivum."
                }
            }
        ]
    },
    {
        "id": "b2_fvg",
        "level": "B2",
        "title": "6. Funktionsverbgefüge (Nominalstil: Turg'un Fe'l-Ot Birikmalari)",
        "keywords": ["funktionsverbgefüge", "fvg", "in betracht ziehen", "zur verfügung stehen", "entscheidung treffen"],
        "summary": "Oddiy so'zlashuvdan akademik va professional uslubga o'tish kaliti.",
        "content": (
            "📖 <b>6-MAVZU: Funktionsverbgefüge (FVG)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "Bitta fe'l o'rniga 'Ot + Ko'makchi + Yordamchi fe'l' birikmasi qo'llanadi:\n"
            "• entscheiden ➔ <b>eine Entscheidung treffen</b> (qaror qabul qilmoq)\n"
            "• berücksichtigen ➔ <b>in Betracht ziehen</b> (inobatga olmoq)\n"
            "• beenden ➔ <b>zu Ende bringen</b> (oxiriga yetkazmoq)\n"
            "• zweifeln ➔ <b>in Zweifel ziehen</b> (shubhaga olmoq)"
        ),
        "quizzes": [
            {
                "id": "b2_fvg_q1",
                "question": "'Wir müssen dieses Problem unbedingt berücksichtigen.' FVG shakli qaysi?",
                "options": [
                    "Wir müssen dieses Problem in Betracht ziehen.",
                    "Wir müssen dieses Problem zur Verfügung stellen.",
                    "Wir müssen dieses Problem in Frage stellen.",
                    "Wir müssen dieses Problem zum Ausdruck bringen."
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: in Betracht ziehen</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "berücksichtigen = <b>in Betracht ziehen</b> (e'tiborga olmoq)."
                ),
                "wrong_explanations": {
                    1: "❌ taqdim etmoq.",
                    2: "❌ shubha ostiga qo'ymoq.",
                    3: "❌ ifodalamoq."
                }
            }
        ]
    },
    {
        "id": "b2_subjektive_modalverben",
        "level": "B2",
        "title": "7. Hozirgi Zamonda Subyektiv Modal Fe'llar (Vermutung: müssen, dürften)",
        "keywords": ["subjektive bedeutung", "vermutung", "müsste", "dürfte", "taxmin bildirish"],
        "summary": "Ishonch darajasiga qarab 100%, 75% va 50% li taxminlarni ifodalash.",
        "content": (
            "📖 <b>7-MAVZU: Subyektiv Modal Fe'llar (Taxmin ifodalash)</b>\n\n"
            "🎯 <b>Duden Qoidasi:</b>\n"
            "• <b>müssen (100% Qat'iy ishonch):</b> <i>Er <b>muss</b> zu Hause sein.</i> (U uyda bo'lsa kerak - 100% aminman).\n"
            "• <b>dürfte (75% Katta ehtimol):</b> <i>Er <b>dürfte</b> bald ankommen.</i> (U tez orada kelsa kerak).\n"
            "• <b>könnte / kann (50% Ehtimol):</b> <i>Es <b>könnte</b> heute regnen.</i> (Bugun yomg'ir yog'ishi ham, yog'masligi ham mumkin)."
        ),
        "quizzes": [
            {
                "id": "b2_smod_q1",
                "question": "'Er hat den ganzen Tag nichts gegessen. Er ___ großen Hunger haben.' (99% mantiqiy ishonch)",
                "options": ["muss", "darf", "soll", "will"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: muss</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Kun bo'yi ovqat yemagan odamning qorni och bo'lishiga 99% mantiqiy ishonch bor (Muss-Vermutung): Er <b>muss</b> großen Hunger haben."
                ),
                "wrong_explanations": {
                    1: "❌ 'darf' ruxsat ma'nosi.",
                    2: "❌ 'soll' mish-mish.",
                    3: "❌ 'will' xohish."
                }
            }
        ]
    }
]
