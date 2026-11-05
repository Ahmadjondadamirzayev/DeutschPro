"""
RASMIY GOETHE-INSTITUT (GYOTE INSTITUTI) TESTLARI BAZASI (A1 - C2)
Goethe-Zertifikat A1, A2, B1, B2, C1 va C2 (GDS - Großes Deutsches Sprachdiplom)
imtihonlarining haqiqiy Sprachbausteine va Grammatik im Kontext formatlari asosida.
"""

GOETHE_TESTS = {
    "A1": [
        {
            "id": "goethe_a1_1",
            "exam_name": "Goethe-Zertifikat A1: Start Deutsch 1",
            "part": "Teil 1: Kundalik Muloqot & E-Mail",
            "question": (
                "📩 <b>E-Mail to'ldirish:</b>\n"
                "<i>'Liebe Maria,\n"
                "ich lade dich herzlich zu ___ Geburtstagsparty ein. Die Party beginnt um 18 Uhr.'</i>\n\n"
                "Bo'sh joyga qaysi so'z to'g'ri keladi?"
            ),
            "options": ["meiner", "meine", "meinem", "mein"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: meiner</b>\n\n"
                "🔍 <b>Goethe A1 & Duden tahlili:</b>\n"
                "1. 'zu' ko'makchisi doimo <b>DATIV</b> kelishigini talab qiladi.\n"
                "2. 'Geburtstagsparty' — ayol jinsi (die Geburtstagsparty).\n"
                "3. Ayol jinsi Dativ kelishigida egalik olmoshiga <b>-er</b> oladi: zu <b>meiner</b> Geburtstagsparty."
            ),
            "wrong_explanations": {
                1: "❌ 'meine' Nominativ yoki Akkusativ shakli. 'zu' esa doimo Dativ talab qiladi.",
                2: "❌ 'meinem' faqat erkak yoki o'rta jins uchun ishlatiladi.",
                3: "❌ 'mein' qo'shimchasiz shakl."
            }
        },
        {
            "id": "goethe_a1_2",
            "exam_name": "Goethe-Zertifikat A1: Start Deutsch 1",
            "part": "Teil 2: E'lonlar va Shaharda",
            "question": (
                "🚉 <b>Vokzaldagi e'lon:</b>\n"
                "<i>'Achtung, Fahrgäste! Der Zug nach München steht heute an ___ Gleis 4 bereit.'</i>",
            ),
            "options": ["dem", "den", "das", "der"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: dem (an dem = am)</b>\n\n"
                "🔍 <b>Goethe A1 & Duden tahlili:</b>\n"
                "'Gleis' — o'rta jins (das Gleis = perron). Poyezd qayerda turibdi? (Wo? ➔ Dativ). "
                "Das Gleis Dativda <b>dem</b> Gleis bo'ladi."
            ),
            "wrong_explanations": {
                1: "❌ 'den' Akkusativ shakli.",
                2: "❌ 'das' Nominativ.",
                3: "❌ 'der' ayol jinsi Dativi."
            }
        },
        {
            "id": "goethe_a1_3",
            "exam_name": "Goethe-Zertifikat A1: Start Deutsch 1",
            "part": "Teil 3: So'zlashuv va Do'konda",
            "question": (
                "🛒 <b>Sotuvchi va Xaridor:</b>\n"
                "<i>'— Guten Tag, kann ich ___ helfen?\n"
                "— Ja bitte, ich suche einen warmen Pullover.'</i>",
            ),
            "options": ["Ihnen", "Sie", "dir", "dich"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: Ihnen</b>\n\n"
                "🔍 <b>Goethe A1 & Duden tahlili:</b>\n"
                "Goethe A1 rasmiy vaziyatlarida 'Sie' olmoshi bilan murojaat qilinadi. "
                "'helfen' fe'li Dativ talab qilgani uchun 'Sie' ➔ <b>Ihnen</b> ga aylanadi: Kann ich <b>Ihnen</b> helfen?"
            ),
            "wrong_explanations": {
                1: "❌ 'Sie' Akkusativ, helfen esa Dativ talab qiladi.",
                2: "❌ 'dir' notanish mijozga nisbatan qo'pol (senlash).",
                3: "❌ 'dich' Akkusativ senlash."
            }
        },
        {
            "id": "goethe_a1_4",
            "exam_name": "Goethe-Zertifikat A1: Start Deutsch 1",
            "part": "Teil 4: Vaqt va Uchrashuv",
            "question": (
                "⏰ <b>Uchrashuv belgilash:</b>\n"
                "<i>'Treffen wir uns morgen ___ 15 Uhr vor dem Kino?'</i>",
            ),
            "options": ["um", "am", "im", "an"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: um</b>\n\n"
                "🔍 <b>Goethe A1 & Duden tahlili:</b>\n"
                "Nemis tilida soat (Uhrzeit) har doim <b>um</b> ko'makchisi bilan aytiladi: <b>um 15 Uhr</b>. "
                "Kunda 'am', oy va faslda 'im' ishlatiladi."
            ),
            "wrong_explanations": {
                1: "❌ 'am' faqat hafta kunlari va sanalarga (am Montag, am 1. Mai).",
                2: "❌ 'im' faqat oylar va fasllarga (im Juli, im Sommer).",
                3: "❌ 'an' soat bilan kelmaydi."
            }
        }
    ],

    "A2": [
        {
            "id": "goethe_a2_1",
            "exam_name": "Goethe-Zertifikat A2",
            "part": "Sprachbausteine: Safar va Taassurotlar",
            "question": (
                "✈️ <b>Sayohat xati:</b>\n"
                "<i>'Wir sind gestern sehr spät im Hotel angekommen, ___ der Flug Verspätung hatte.'</i>",
            ),
            "options": ["weil", "denn", "deshalb", "obwohl"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: weil</b>\n\n"
                "🔍 <b>Goethe A2 & Duden tahlili:</b>\n"
                "Sabab ergash gapida tuslangan fe'l (hatte) gapning ENG OXIRIDA turibdi. Shuning uchun fe'lni oxirga suruvchi <b>weil</b> bo'ladi."
            ),
            "wrong_explanations": {
                1: "❌ 'denn' fe'lni oxirga surmaydi.",
                2: "❌ 'deshalb' natija bildiradi va fe'l 2-o'rinda keladi.",
                3: "❌ 'obwohl' qaramasdan degani."
            }
        },
        {
            "id": "goethe_a2_2",
            "exam_name": "Goethe-Zertifikat A2",
            "part": "Grammatik im Kontext: Kundalik vaziyatlar",
            "question": (
                "🏠 <b>Uy e'loni:</b>\n"
                "<i>'Die Wohnung liegt im Stadtzentrum und ist ___ als unsere alte Wohnung.'</i>",
            ),
            "options": ["viel billiger", "billig", "am billigsten", "sehr billig"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: viel billiger</b>\n\n"
                "🔍 <b>Goethe A2 & Duden tahlili:</b>\n"
                "Gapda <b>als</b> (ko'ra/nisbatan) bor. Shuning uchun sifat Komparativ (-er) darajasida bo'lishi shart: <b>billiger als...</b>"
            ),
            "wrong_explanations": {
                1: "❌ 'billig' oddiy daraja.",
                2: "❌ 'am billigsten' orttirma daraja.",
                3: "❌ 'sehr billig' als bilan taqqoslanmaydi."
            }
        },
        {
            "id": "goethe_a2_3",
            "exam_name": "Goethe-Zertifikat A2",
            "part": "Perfekt tanlovi",
            "question": (
                "🏃 <b>Xabar:</b>\n"
                "<i>'Gestern Abend ___ ich noch zwei Stunden im Park gejoggt.'</i>",
            ),
            "options": ["bin", "habe", "hatte", "wurde"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: bin</b>\n\n"
                "🔍 <b>Goethe A2 & Duden tahlili:</b>\n"
                "'joggen' (yugurmoq) harakat fe'li (Ortswechsel) bo'lib, Perfektda <b>sein</b> (ich bin gejoggt) oladi."
            ),
            "wrong_explanations": {
                1: "❌ Harakat fe'llari haben olmaydi.",
                2: "❌ Präteritum yordamchisi.",
                3: "❌ Passiv shakli."
            }
        },
        {
            "id": "goethe_a2_4",
            "exam_name": "Goethe-Zertifikat A2",
            "part": "Modal fe'llar va Taklif",
            "question": (
                "🎭 <b>Kino taklifi:</b>\n"
                "<i>'Hast du heute Abend Zeit? Wir ___ zusammen ins Theater gehen.'</i>",
            ),
            "options": ["könnten", "müssen", "durften", "wolltest"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: könnten</b>\n\n"
                "🔍 <b>Goethe A2 & Duden tahlili:</b>\n"
                "Muloyim taklif bildirishda 'können' ning Konjunktiv II shakli <b>könnten</b> qo'llanadi: 'Wir könnten... gehen' (Borsak bo'lardi / Borishimiz mumkin)."
            ),
            "wrong_explanations": {
                1: "❌ 'müssen' majburiyat yuklaydi (taklif emas).",
                2: "❌ 'durften' o'tgan zamon.",
                3: "❌ 'wolltest' du uchun shakl."
            }
        }
    ],

    "B1": [
        {
            "id": "goethe_b1_1",
            "exam_name": "Goethe-Zertifikat B1",
            "part": "Sprachbausteine Teil 1: Rasmiy xat",
            "question": (
                "📝 <b>Arizani to'ldirish:</b>\n"
                "<i>'Sehr geehrte Damen und Herren,\n"
                "ich schreibe Ihnen, ___ ich mich über Ihren Service beschweren möchte.'</i>",
            ),
            "options": ["da", "denn", "deswegen", "trotzdem"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: da</b>\n\n"
                "🔍 <b>Goethe B1 & Duden tahlili:</b>\n"
                "'da' rasmiy uslubda 'weil' ning sinonimi bo'lib, sabab ergash gap yasaydi va tuslangan fe'lni (möchte) gap oxiriga itaradi."
            ),
            "wrong_explanations": {
                1: "❌ 'denn' fe'lni oxirga surmaydi.",
                2: "❌ 'deswegen' fe'l darhol 2-o'rinda keladi.",
                3: "❌ 'trotzdem' shunga qaramay degani."
            }
        },
        {
            "id": "goethe_b1_2",
            "exam_name": "Goethe-Zertifikat B1",
            "part": "Sprachbausteine Teil 2: Nisbiy gaplar",
            "question": (
                "🏢 <b>Hamkasb haqida:</b>\n"
                "<i>'Das ist die neue Kollegin, mit ___ wir gestern das Projekt besprochen haben.'</i>",
            ),
            "options": ["der", "die", "denen", "deren"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: der</b>\n\n"
                "🔍 <b>Goethe B1 & Duden tahlili:</b>\n"
                "'mit' Dativ talab qiladi. 'Kollegin' ayol jinsi (die Kollegin). Ayol jinsining Dativdagi nisbiy olmoshi <b>der</b> bo'ladi: mit <b>der</b>."
            ),
            "wrong_explanations": {
                1: "❌ 'die' Akkusativ/Nominativ.",
                2: "❌ 'denen' ko'plik Dativi.",
                3: "❌ 'deren' egalik."
            }
        },
        {
            "id": "goethe_b1_3",
            "exam_name": "Goethe-Zertifikat B1",
            "part": "Konjunktiv II: Orzu",
            "question": (
                "💭 <b>Orzu ifodasi:</b>\n"
                "<i>'Wenn ich doch bloß mehr Zeit für meine Hobbys ___!'</i>",
            ),
            "options": ["hätte", "habe", "hatte", "würde"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: hätte</b>\n\n"
                "🔍 <b>Goethe B1 & Duden tahlili:</b>\n"
                "'Wenn doch bloß...' (Qaniydi vaqtim bo'lganida!) — Konjunktiv II orzu formulasi. Haben fe'li <b>hätte</b> bo'ladi."
            ),
            "wrong_explanations": {
                1: "❌ Indikativ hozirgi zamon.",
                2: "❌ Indikativ o'tgan zamon.",
                3: "❌ Infinitiv kerak bo'lardi."
            }
        },
        {
            "id": "goethe_b1_4",
            "exam_name": "Goethe-Zertifikat B1",
            "part": "Infinitivsatz: um... zu",
            "question": (
                "🎯 <b>Maqsad bildirish:</b>\n"
                "<i>'Er spart jeden Monat Geld, ___ sich im Sommer eine Reise nach Berlin leisten ___ können.'</i>",
            ),
            "options": ["um / zu", "ohne / zu", "statt / zu", "damit / zu"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: um / zu</b>\n\n"
                "🔍 <b>Goethe B1 & Duden tahlili:</b>\n"
                "Maqsad bildirishda har ikkala gapning egasi bir shaxs (er) bo'lsa, <b>um ... zu + Infinitiv</b> qo'llanadi: um ... leisten zu können."
            ),
            "wrong_explanations": {
                1: "❌ 'ohne' qilmasdan ma'nosida.",
                2: "❌ 'statt' o'rniga.",
                3: "❌ 'damit' dan keyin 'zu' kelmaydi."
            }
        }
    ],

    "B2": [
        {
            "id": "goethe_b2_1",
            "exam_name": "Goethe-Zertifikat B2",
            "part": "Lesen Teil 4 / Sprachbausteine: Matbuot tili",
            "question": (
                "📰 <b>Gazeta maqolasi:</b>\n"
                "<i>'Die Ergebnisse der neuen Studie ___ sich durchaus sehen lassen.'</i>",
            ),
            "options": ["können", "müssen", "sollen", "dürfen"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: können (sich sehen lassen können)</b>\n\n"
                "🔍 <b>Goethe B2 & Duden tahlili:</b>\n"
                "'sich sehen lassen können' — B2 darajasidagi mashhur ibora bo'lib, 'o'zini ko'rsata olmoq / yuqori bahoga loyiq bo'lmoq' degan ma'noni bildiradi."
            ),
            "wrong_explanations": {
                1: "❌ 'müssen' bu iboraga kirmaydi.",
                2: "❌ 'sollen' mos emas.",
                3: "❌ 'dürfen' ruxsat ma'nosi."
            }
        },
        {
            "id": "goethe_b2_2",
            "exam_name": "Goethe-Zertifikat B2",
            "part": "Grammatik im Kontext: Passiv ekvivalentlari",
            "question": (
                "🔬 <b>Ilmiy hisobot:</b>\n"
                "<i>'Die genauen Ursachen des Phänomens sind noch genauer ___.'</i>",
            ),
            "options": ["zu untersuchen", "untersucht werden", "untersuchen", "untersuchend"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: zu untersuchen</b>\n\n"
                "🔍 <b>Goethe B2 & Duden tahlili:</b>\n"
                "<b>'sein + zu + Infinitiv'</b> passiv majburiyatni bildiradi (= müssen untersucht werden / o'rganilishi lozim)."
            ),
            "wrong_explanations": {
                1: "❌ 'sind untersucht werden' xato shakl.",
                2: "❌ 'zu' siz bo'lmaydi.",
                3: "❌ Sifatdosh shakli noto'g'ri."
            }
        },
        {
            "id": "goethe_b2_3",
            "exam_name": "Goethe-Zertifikat B2",
            "part": "N-Deklination va Kelishiklar",
            "question": (
                "⚖️ <b>Sud va Politsiya:</b>\n"
                "<i>'Die Polizei befragte den anwesenden ___ zu dem Vorfall.' (der Zeuge = guvoh)</i>",
            ),
            "options": ["Zeugen", "Zeuge", "Zeuges", "Zeugem"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: Zeugen</b>\n\n"
                "🔍 <b>Goethe B2 & Duden tahlili:</b>\n"
                "'der Zeuge' N-Deklination otidir. Akkusativda (den Zeugen) oxiriga <b>-n</b> oladi."
            ),
            "wrong_explanations": {
                1: "❌ 'Zeuge' Nominativda qolgan.",
                2: "❌ N-Deklination -s olmaydi.",
                3: "❌ Bunday shakl yo'q."
            }
        },
        {
            "id": "goethe_b2_4",
            "exam_name": "Goethe-Zertifikat B2",
            "part": "Funktionsverbgefüge (FVG)",
            "question": (
                "💼 <b>Ishbilarmonlik suhbati:</b>\n"
                "<i>'Bevor wir investieren, müssen wir alle Risiken in Betracht ___.'</i>",
            ),
            "options": ["ziehen", "stellen", "bringen", "nehmen"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: ziehen (in Betracht ziehen)</b>\n\n"
                "🔍 <b>Goethe B2 & Duden tahlili:</b>\n"
                "'in Betracht ziehen' = berücksichtigen (inobatga olmoq). Bu B2/C1 darajasidagi eng asosiy Funktionsverbgefüge birikmasidir."
            ),
            "wrong_explanations": {
                1: "❌ 'in Frage stellen' (shubha bildirmoq).",
                2: "❌ 'zum Ausdruck bringen' (ifodalamoq).",
                3: "❌ 'Abschied nehmen' (xayrlashmoq)."
            }
        }
    ],

    "C1": [
        {
            "id": "goethe_c1_1",
            "exam_name": "Goethe-Zertifikat C1",
            "part": "Strukturen und Wortschatz: Nominalstil",
            "question": (
                "🎓 <b>Akademik matn:</b>\n"
                "<i>'___ der weltweiten Rohstoffknappheit stiegen die Produktionskosten drastisch.'</i>",
            ),
            "options": ["Infolge", "Wegen dem", "Durch die", "Anlässlich"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: Infolge (+ Genitiv)</b>\n\n"
                "🔍 <b>Goethe C1 & Duden tahlili:</b>\n"
                "'Infolge' (+ Genitiv) sabab-oqibatni ifodalovchi yuksak C1 akademik ko'makchisidir: 'Xomashyo taqchilligi oqibatida...'."
            ),
            "wrong_explanations": {
                1: "❌ 'Wegen dem' og'zaki til, C1 da 'Wegen des' bo'ladi.",
                2: "❌ 'Durch die' mos kelmaydi.",
                3: "❌ 'Anlässlich' munosabati bilan degani."
            }
        },
        {
            "id": "goethe_c1_2",
            "exam_name": "Goethe-Zertifikat C1",
            "part": "Konjunktiv I: O'zlashtirma matbuot tili",
            "question": (
                "🗞 <b>Siyosiy yangiliklar:</b>\n"
                "<i>'Der Regierungssprecher betonte, die Reform ___ unausweichlich, um den Haushalt zu sanieren.'</i>",
            ),
            "options": ["sei", "wäre", "ist", "werde sein"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: sei</b>\n\n"
                "🔍 <b>Goethe C1 & Duden tahlili:</b>\n"
                "O'zlashtirma gapda (Indirekte Rede) 3-shaxs birlik uchun 'sein' fe'lining sof Konjunktiv I shakli <b>sei</b> dir."
            ),
            "wrong_explanations": {
                1: "❌ 'wäre' Konjunktiv II, nohaqiy shubha uyg'otadi.",
                2: "❌ 'ist' Indikativ bo'lib, xolislikni yo'qotadi.",
                3: "❌ Kelasi zamon shakli noo'rin."
            }
        },
        {
            "id": "goethe_c1_3",
            "exam_name": "Goethe-Zertifikat C1",
            "part": "Gehobene Konnektoren: Bog'lovchilar",
            "question": (
                "🏛 <b>Iqtisodiy tahlil:</b>\n"
                "<i>'Das Land verfügt über kaum nennenswerte Bodenschätze, ___ ist seine Wirtschaft hochentwickelt.'</i>",
            ),
            "options": ["nichtsdestotrotz", "wohingegen", "geschweige denn", "insofern"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: nichtsdestotrotz</b>\n\n"
                "🔍 <b>Goethe C1 & Duden tahlili:</b>\n"
                "'nichtsdestotrotz' (shunga qaramasdan) — C1 darajasidagi oliy zidlik bog'lovchisidir. Undan keyin darhol tuslangan fe'l (ist) keladi."
            ),
            "wrong_explanations": {
                1: "❌ 'wohingegen' ergash gap yasaydi va fe'lni oxirga suradi.",
                2: "❌ 'geschweige denn' inkorli qiyoslash (u yoqda tursin).",
                3: "❌ 'insofern' shart/chegaralash bildiradi."
            }
        },
        {
            "id": "goethe_c1_4",
            "exam_name": "Goethe-Zertifikat C1",
            "part": "Gerundivum: zu + Partizip I",
            "question": (
                "📋 <b>Qonun hujjati:</b>\n"
                "<i>'Die bei der Einreise unbedingt zu ___ Vorschriften wurden verschärft.' (beachten = rioya qilmoq)</i>",
            ),
            "options": ["beachtenden", "beachteten", "beachtete", "beachten"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: beachtenden</b>\n\n"
                "🔍 <b>Goethe C1 & Duden tahlili:</b>\n"
                "Gerundivum: <b>zu + Partizip I + sifat qo'shimchasi</b>. 'die Vorschriften' (ko'plik) bo'lgani uchun: zu <b>beachtenden</b> Vorschriften (= die beachtet werden müssen)."
            ),
            "wrong_explanations": {
                1: "❌ 'beachteten' Partizip II, bu Gerundivum emas.",
                2: "❌ Birlik shakli.",
                3: "❌ Infinitiv sifatdosh o'rnida kelolmaydi."
            }
        }
    ],

    "C2": [
        {
            "id": "goethe_c2_1",
            "exam_name": "Goethe-Zertifikat C2: GDS (Großes Deutsches Sprachdiplom)",
            "part": "Stilistik & Nuancen der Wissenschaftssprache",
            "question": (
                "📜 <b>Falsafiy va Huquqiy Matn:</b>\n"
                "<i>'Die These des Autors entbehrt jeglicher wissenschaftlichen Grundlage, ___ sie auf veralteten Prämissen beruht.'</i>\n\n"
                "Ushbu gapdagi mantiqiy sababni eng yuksak C2 ritorik uslubda qaysi bog'lovchi bog'laydi?",
            ),
            "options": ["zumal", "obzwar", "wenngleich", "indes"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: zumal</b>\n\n"
                "🔍 <b>Goethe C2 GDS & Duden Band 4 tahlili:</b>\n"
                "'zumal' — 'ayniqsa ... ekanligini inobatga olsak / qolaversa ... sababli' degan ma'noni anglatuvchi "
                "oliy ilmiy kausal subyunksiyadir. U keltirilgan hukmga qo'shimcha hal qiluvchi dalil kiritadi."
            ),
            "wrong_explanations": {
                1: "❌ 'obzwar' arxaik zidlik bog'lovchisi (garchi ... bo'lsa ham).",
                2: "❌ 'wenngleich' ham zidlik bog'lovchisi.",
                3: "❌ 'indes' adversativ ravish bo'lib, fe'lni gap oxiriga itarmaydi."
            }
        },
        {
            "id": "goethe_c2_2",
            "exam_name": "Goethe-Zertifikat C2: GDS",
            "part": "Passiversatzformen & Rhetorische Figuren",
            "question": (
                "🏛 <b>Diplomatik Hujjat:</b>\n"
                "<i>'Es ___ unumwunden festzuhalten, dass die Verhandlungen gescheitert sind.'</i>\n\n"
                "Qaysi fe'l ushbu yuksak passiv majburiyat ma'nosini beradi?",
            ),
            "options": ["gilt", "bleibt", "steht", "scheint"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: gilt (es gilt zu + Infinitiv)</b>\n\n"
                "🔍 <b>Goethe C2 GDS & Duden tahlili:</b>\n"
                "<b>'Es gilt + zu + Infinitiv'</b> — bu oliy C2 darajasidagi qat'iy zarurat/burch formulasidir "
                "(= Es muss unumwunden festgehalten werden / Bu ochiq-oydin ta'kidlanishi shart!)."
            ),
            "wrong_explanations": {
                1: "❌ 'es bleibt zu' noaniqlik/kelajakdagi imkoniyat (es bleibt abzuwarten).",
                2: "❌ 'es steht zu' noto'g'ri birikma.",
                3: "❌ 'es scheint' subyektiv tuyulish."
            }
        },
        {
            "id": "goethe_c2_3",
            "exam_name": "Goethe-Zertifikat C2: GDS",
            "part": "Redewendungen & Funktionsverbgefüge der Hochsprache",
            "question": (
                "🖋 <b>Adabiy Tanqid:</b>\n"
                "<i>'Der Regisseur verstand es meisterhaft, die feinen Nuancen des Dramas zur ___ zu bringen.'</i>",
            ),
            "options": ["Geltung", "Wirkung", "Stelle", "Sache"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: Geltung (zur Geltung bringen)</b>\n\n"
                "🔍 <b>Goethe C2 GDS & Duden tahlili:</b>\n"
                "'etwas zur Geltung bringen' — bu nemis adabiy tilining eng yuksak turg'un birikmasi (Funktionsverbgefüge) bo'lib, "
                "'biror narsaning butun jozibasi, kuchi va mohiyatini to'liq namoyon etmoq' degan ma'noni anglatadi."
            ),
            "wrong_explanations": {
                1: "❌ 'zur Wirkung bringen' adabiy tilda ishlatilmaydi.",
                2: "❌ 'zur Stelle sein' hozir bo'lmoq.",
                3: "❌ 'zur Sache kommen' maqsadga o'tmoq."
            }
        },
        {
            "id": "goethe_c2_4",
            "exam_name": "Goethe-Zertifikat C2: GDS",
            "part": "Subjektive Modalverben mit Perfekt Infinitiv",
            "question": (
                "💼 <b>Korrupsiya tergovi:</b>\n"
                "<i>'Der ehemalige Vorstandsvorsitzende will von den geheimen Absprachen nichts gewusst ___.'</i>",
            ),
            "options": ["haben", "sein", "hätte", "hätten"],
            "correct_index": 0,
            "proof": (
                "✅ <b>TO'G'RI JAVOB: haben</b>\n\n"
                "🔍 <b>Goethe C2 GDS & Duden tahlili:</b>\n"
                "C2 subyektiv modal fe'li: <b>'wollen + Infinitiv Perfekt'</b> (o'zining shubhali da'vosi). "
                "wissen fe'li Perfektda 'haben' oladi: <i>gewusst haben</i> (bexabar bo'lganini da'vo qilmoqda)."
            ),
            "wrong_explanations": {
                1: "❌ wissen fe'li sein olmaydi.",
                2: "❌ Infinitiv o'rniga Konjunktiv qo'yilmaydi.",
                3: "❌ Noto'g'ri tuslanish."
            }
        }
    ]
}


def get_goethe_tests_by_level(level: str):
    """Berilgan darajadagi Gyote testlarini qaytaradi"""
    return GOETHE_TESTS.get(level.upper(), [])


def get_all_goethe_tests():
    """Barcha A1-C2 Gyote testlarini bitta ro'yxatda qaytaradi"""
    res = []
    for lvl, tests in GOETHE_TESTS.items():
        res.extend(tests)
    return res
