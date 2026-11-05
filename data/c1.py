"""
C1 DARAJASI GRAMMATIKA MAVZULARI (RASMIY DUDEN & CEFR / GeR STANDARTI)
CEFR C1 oliy akademik me'yorlariga 100% mos va turfa xil test savollari bilan boyitilgan.
"""

C1_TOPICS = [
    {
        "id": "c1_konjunktiv1",
        "level": "C1",
        "title": "1. Konjunktiv I: O'zlashtirma Gap (Indirekte Rede / Jurnalistika & Sud tili)",
        "keywords": ["konjunktiv 1", "indirekte rede", "o'zlashtirma gap", "er habe gesagt", "sei", "habe", "ersatzform"],
        "summary": "Jurnalistlar va OAV tili: birovning gapini o'z mas'uliyatiga olmasdan betaraf yetkazish san'ati.",
        "content": (
            "📖 <b>1-MAVZU: Konjunktiv I (Indirekte Rede - O'zlashtirma Gap)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR C1 Standarti:</b>\n"
            "Konjunktiv I matbuot, sud va jiddiy ilmiy asarlarda birovning fikrini (ko'chirma gapni) "
            "so'zlovchining shaxsiy munosabatisiz, xolis va betaraf yetkazish uchun qo'llanadi.\n\n"
            "🔹 <b>Hozirgi zamon yasalishi (Fe'l o'zagi + e):</b>\n"
            "• <b>ich: -e</b> (Indikativ bilan bir xil bo'lsa ➔ Konjunktiv II ga almashtiriladi!)\n"
            "• <b>du: -est</b>\n"
            "• <b>er / sie / es: -e</b> ⚠️ (Eng mashhur shakl! Hech qanday -t yo'q!)\n"
            "  <i>Der Minister sagt, er <b>habe</b> keine Schuld.</i>\n"
            "  <i>Der Sprecher erklärt, die Lage <b>sei</b> stabil.</i>\n\n"
            "🔹 <b>O'tgan zamon Konjunktiv I (Barcha o'tgan zamonlar uchun bitta formula!):</b>\n"
            "<b>sei / habe + Partizip II</b>\n"
            "• Er sagte, er <b>habe</b> den Zeugen nicht <b>gesehen</b>.\n"
            "• Sie behauptet, sie <b>sei</b> pünktlich <b>angekommen</b>.\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Oddiy gapda 'er hat' yoki 'er ist' bo'lsa, C1 O'zlashtirma gapida ular darhol <b>er HABE</b> va <b>er SEI</b> ga aylanadi!"
        ),
        "quizzes": [
            {
                "id": "c1_k1_q1",
                "question": "Der Zeuge behauptet: 'Ich kenne den Täter nicht.' Buni Konjunktiv I orqali o'zlashtirma qiling:",
                "options": [
                    "Der Zeuge behauptet, er kenne den Täter nicht.",
                    "Der Zeuge behauptet, er kennt den Täter nicht.",
                    "Der Zeuge behauptet, er kannte den Täter nicht.",
                    "Der Zeuge behauptet, er kenne den Täter nicht haben."
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ...er kenne den Täter nicht.</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Kennen fe'lining 3-shaxs birlik (er) Konjunktiv I shakli <b>o'zak + e = kenne</b> bo'ladi. 'er kennt' bu Indikativ bo'lib, C1 normasi hisoblanmaydi."
                ),
                "wrong_explanations": {
                    1: "❌ 'er kennt' bu oddiy darak gap (Indikativ).",
                    2: "❌ 'er kannte' o'tgan zamon indikativi.",
                    3: "❌ Grammatik jihatdan noto'g'ri."
                }
            },
            {
                "id": "c1_k1_q2",
                "question": "Die Kanzlerin teilte mit: 'Wir haben alle Ziele erreicht.' Konjunktiv I shakli qaysi?",
                "options": [
                    "Die Kanzlerin teilte mit, sie hätten alle Ziele erreicht (Formengleichheit tufayli K-II).",
                    "Die Kanzlerin teilte mit, sie haben alle Ziele erreicht.",
                    "Die Kanzlerin teilte mit, sie seien alle Ziele erreicht.",
                    "Die Kanzlerin teilte mit, sie würden erreichen."
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ...sie hätten alle Ziele erreicht.</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot (Ersatzform):</b>\n"
                    "Ko'plikda (sie haben) Konjunktiv I ham 'haben' bo'lib, oddiy Indikativ bilan bir xil bo'lib qoladi (Formengleichheit). "
                    "Duden qoidasiga ko'ra, agar K-I Indikativ bilan bir xil bo'lib qolsa, uning o'rniga majburiy ravishda <b>Konjunktiv II (hätten)</b> ishlatiladi!"
                ),
                "wrong_explanations": {
                    1: "❌ 'haben' Indikativ bilan chalkashib ketadi, Duden K-II ga almashtirishni talab qiladi.",
                    2: "❌ 'seien' noto'g'ri, erreichen haben bilan yasaladi.",
                    3: "❌ O'tgan zamon o'rniga kelasi zamon qo'yilgan."
                }
            }
        ]
    },
    {
        "id": "c1_nominalisierung",
        "level": "C1",
        "title": "2. Nominalisierung va Verbalisierung (Duden Ilmiy Uslubi)",
        "keywords": ["nominalisierung", "verbalisierung", "otlashtirish", "fe'llashtirish", "ilmiy stil", "akademik"],
        "summary": "Gaplarni fe'l uslubidan (Verbalstil) ixcham va salobatli ot uslubiga (Nominalstil) o'tkazish.",
        "content": (
            "📖 <b>2-MAVZU: Nominalisierung va Verbalisierung</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR C1 Standarti:</b>\n"
            "C1 darajadagi akademik maqolalar va ilmiy matnlarda uzun ergash gaplarni <b>Ko'makchi + Ot + Genitiv</b> shakliga siqib ixchamlashtirish talab qilinadi.\n\n"
            "🔄 <b>Ekvivalentlar jadvali:</b>\n"
            "• <b>weil / da</b> (chunki) ➔ <b>wegen / aufgrund + Genitiv</b>\n"
            "  <i>Weil die Preise steigen</i> ➔ <b>Aufgrund des Anstiegs der Preise</b>\n"
            "• <b>wenn / falls</b> (agar) ➔ <b>bei + Dativ</b>\n"
            "  <i>Wenn das System ausfällt</i> ➔ <b>Bei Ausfall des Systems</b>\n"
            "• <b>obwohl</b> (garchi) ➔ <b>trotz + Genitiv</b>\n"
            "  <i>Obwohl die Krise andauert</i> ➔ <b>Trotz des Andauerns der Krise</b>\n"
            "• <b>bevor</b> (oldin) ➔ <b>vor + Dativ</b>\n"
            "• <b>nachdem</b> (keyin) ➔ <b>nach + Dativ</b>\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Fe'lni olib otga aylantiring (steigen ➔ der Anstieg) va uning egasini Genitiv qilib orqasiga qo'ying!"
        ),
        "quizzes": [
            {
                "id": "c1_nom_q1",
                "question": "'Obwohl die Wirtschaftskrise andauert, wächst die Firma.' Ushbu gapning Nominal varianti qaysi?",
                "options": [
                    "Trotz der andauernden Wirtschaftskrise wächst die Firma.",
                    "Wegen der andauernden Wirtschaftskrise wächst die Firma.",
                    "Bei der andauernden Wirtschaftskrise wächst die Firma.",
                    "Anstatt der andauernden Wirtschaftskrise wächst die Firma."
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Trotz der andauernden Wirtschaftskrise...</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "'obwohl' (zidlik) bog'lovchisining aniq nominal ekvivalenti <b>trotz + Genitiv</b> hisoblanadi."
                ),
                "wrong_explanations": {
                    1: "❌ 'Wegen' sabab bildiradi, zidlik emas.",
                    2: "❌ 'Bei' shart/vaqt bildiradi.",
                    3: "❌ 'Anstatt' o'rniga degani."
                }
            }
        ]
    },
    {
        "id": "c1_gerundivum",
        "level": "C1",
        "title": "3. Gerundivum: zu + Partizip I (Majburiyat & Imkoniyat)",
        "keywords": ["gerundivum", "zu partizip 1", "das zu lösende problem", "muss gelöst werden", "kann gelöst werden"],
        "summary": "'Yechilishi shart bo'lgan masala' — zu + Partizip I birikmasining passiv kuchi.",
        "content": (
            "📖 <b>3-MAVZU: Gerundivum (zu + Partizip I)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR C1 Standarti:</b>\n"
            "Partizip I oldiga <b>'zu'</b> qo'shilib, ot oldida sifat sifatida turlanganda, u <b>majburiyat</b> (muss getan werden) yoki <b>imkoniyat</b> (kann getan werden) ma'nosidagi passiv konstruksiyaga aylanadi.\n\n"
            "🔹 <b>Formulasi:</b>\n"
            "<b>zu + Fe'l o'zagi + end + [sifat qo'shimchasi] + Ot</b>\n"
            "• <i>das <b>zu lösende</b> Problem</i> = das Problem, das <b>gelöst werden muss</b> (Yechilishi shart bo'lgan muammo)\n"
            "• <i>die <b>zu beachtenden</b> Regeln</i> = die Regeln, die <b>beachtet werden müssen</b> (Roya qilinishi shart bo'lgan qoidalar)\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Partizip I oldida 'zu' ko'rdingizmi — bu har doim <b>'qilinishi shart bo'lgan'</b> passiv majburiyatdir!"
        ),
        "quizzes": [
            {
                "id": "c1_ger_q1",
                "question": "'Die noch zu erledigenden Aufgaben' nimani anglatadi?",
                "options": [
                    "Die Aufgaben, die noch erledigt werden müssen",
                    "Die Aufgaben, die man schon erledigt hat",
                    "Die Aufgaben, die sich selbst erledigen",
                    "Die Aufgaben, die nicht erledigt werden dürfen"
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ...die noch erledigt werden müssen.</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Gerundivum (zu + Partizip I) grammatik jihatdan 'müssen + Passiv' konstruksiyasining akademik ekvivalentidir."
                ),
                "wrong_explanations": {
                    1: "❌ Allaqachon bajarilgan emas, hali bajarilishi shart bo'lgan vazifalar.",
                    2: "❌ O'z-o'zidan bajarilmaydi.",
                    3: "❌ Taqiqlangan emas."
                }
            }
        ]
    },
    {
        "id": "c1_partizipialattribute",
        "level": "C1",
        "title": "4. Kengaytirilgan Sifatdosh Birikmalari (Erweiterte Partizipialattribute)",
        "keywords": ["partizipialattribut", "erweiterte partizipien", "kengaytirilgan sifatdosh", "relativsatz"],
        "summary": "Nemis ilmiy matnlarining eng uzun va murakkab jumlalarini oson yorib o'tish usuli.",
        "content": (
            "📖 <b>4-MAVZU: Kengaytirilgan Sifatdosh Birikmalari</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR C1 Standarti:</b>\n"
            "Artikl va ot o'rtasiga ko'plab ma'lumotlar bloki kiritiladi:\n"
            "[Artikl] + [<b>Kengaytirilgan izohlar</b>] + [<b>Sifatdosh</b>] + [<b>Ot</b>]\n\n"
            "💡 <b>Misol:</b>\n"
            "• <i>Das</i> [von den Forschern jahrelang intensiv entwickelte] <i>Verfahren</i>.\n"
            "  (Tadqiqotchilar tomonidan yillar davomida ishlab chiqilgan usul)\n\n"
            "🔄 <b>Buni tushunish siri (Relativsatzga aylantirish):</b>\n"
            "➔ <i>Das Verfahren, <b>das</b> von den Forschern jahrelang intensiv entwickelt wurde.</i>\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "Artikl va eng oxiridagi OTni toping — o'rtasidagi hamma so'zlar o'sha otning shunchaki 'bezagi'!"
        ),
        "quizzes": [
            {
                "id": "c1_paratt_q1",
                "question": "'Das vom Parlament gestern einstimmig beschlossene Gesetz' iborasini Relativsatzga aylantiring:",
                "options": [
                    "Das Gesetz, das gestern vom Parlament einstimmig beschlossen wurde",
                    "Das Gesetz beschließt das Parlament gestern einstimmig",
                    "Das Gesetz, das gestern das Parlament einstimmig beschlossen hat zu sein",
                    "Das Gesetz, weil das Parlament es beschlossen hat"
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Das Gesetz, das gestern vom Parlament einstimmig beschlossen wurde</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Partizip II (beschlossene) passiv o'tgan zamon ma'nosini beradi (beschlossen wurde)."
                ),
                "wrong_explanations": {
                    1: "❌ Qonun parlamentni qabul qilmaydi.",
                    2: "❌ Noto'g'ri grammatik tuzilish.",
                    3: "❌ Sabab gapi emas."
                }
            }
        ]
    },
    {
        "id": "c1_subjektive_modalverben_vergangenheit",
        "level": "C1",
        "title": "5. O'tgan Zamondagi Subyektiv Modal Fe'llar (Subjektive Modalverben)",
        "keywords": ["subjektive modalverben", "vergangenheit", "er soll getan haben", "er will gewesen sein", "muss verpasst haben"],
        "summary": "'U o'g'irlagan emish' yoki 'U buni ko'rganman deb da'vo qilmoqda' — taxmin va mish-mishlar.",
        "content": (
            "📖 <b>5-MAVZU: O'tgan Zamondagi Subyektiv Modal Fe'llar</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR C1 Standarti:</b>\n"
            "C1 darajasida modal fe'llar faqat jismoniy qobiliyat emas, balki <b>so'zlovchining voqeaga ishonch darajasi, mish-mish yoki boshqa birovning da'vosini</b> ifodalash uchun xizmat qiladi.\n\n"
            "🔹 <b>Formulasi:</b>\n"
            "<b>Modal fe'l (Präsens) + Partizip II + haben / sein</b>\n\n"
            "1. <b>SOLLEN (Mish-mish / Birovning aytishi bo'yicha - Man sagt, dass...):</b>\n"
            "• <i>Er <b>soll</b> die Million <b>gestohlen haben</b>.</i>\n"
            "  (U millionni o'g'irlagan emish / Aytishlaricha u o'g'irlagan ekan).\n\n"
            "2. <b>WOLLEN (O'zining da'vosi / Boshqalar ishonmaydi - Er behauptet, dass...):</b>\n"
            "• <i>Er <b>will</b> davon nichts <b>gewusst haben</b>.</i>\n"
            "  (U bundan bexabar bo'lganini da'vo qilmoqda — lekin hech kim bunga ishonmaydi).\n\n"
            "3. <b>MÜSSEN (99% qat'iy ishonch / mantiqiy xulosa):</b>\n"
            "• <i>Das Licht ist aus. Sie <b>muss</b> schon <b>eingeschlafen sein</b>.</i>\n"
            "  (Chiroq o'chiq. U allaqachon uxlab qolgan bo'lsa kerak — 99% ishonch).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "• <b>soll... haben</b> = 'Mish-mish / Odamlar shunday deyishyapti'.\n"
            "• <b>will... haben</b> = 'O'zi shunday deb da'vo qilyapti, lekin gumonli'!"
        ),
        "quizzes": [
            {
                "id": "c1_submod_q1",
                "question": "'Er will den berühmten Schauspieler persönlich kennengelernt haben.' Bu gap nimani anglatadi?",
                "options": [
                    "Er behauptet, dass er ihn kennengelernt hat (o'zi shunday deb da'vo qilmoqda)",
                    "Er möchte den Schauspieler unbedingt kennenlernen",
                    "Man sagt, dass er ihn kennengelernt hat (mish-mish)",
                    "Er hat ihn sicher nicht kennengelernt"
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: Er behauptet, dass er ihn kennengelernt hat</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Subyektiv 'wollen + Partizip II + haben' egasining shaxsiy da'vosini (Subjektive Behauptung) ifodalaydi: 'U shunday deb da'vo qilyapti'."
                ),
                "wrong_explanations": {
                    1: "❌ 'Er möchte...' bu oddiy xohish, subyektiv o'tgan zamon emas.",
                    2: "❌ Mish-mish uchun 'sollen' (Er soll kennengelernt haben) ishlatilardi.",
                    3: "❌ Noto'g'ri tushuntirish."
                }
            }
        ]
    },
    {
        "id": "c1_passiversatzformen",
        "level": "C1",
        "title": "6. C1 Passiv O'rinbosarlari (gehören + PII, es gilt zu, es bleibt zu)",
        "keywords": ["passiversatzformen", "gehören partizip 2", "es gilt zu", "es bleibt abzuwarten", "passiv ekvivalent"],
        "summary": "Akademik nemis tilidagi eng nozik va salobatli passiv konstruksiyalari.",
        "content": (
            "📖 <b>6-MAVZU: C1 Passiv O'rinbosarlari (Passiversatzformen)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR C1 Standarti:</b>\n"
            "B2 dagi 'sich lassen' va 'sein zu' dan tashqari, C1 darajasida quyidagi nufuzli passiv konstruksiyalar qo'llanadi:\n\n"
            "🔹 <b>1. gehören + Partizip II (Majburiyat / Qilinishi shart):</b>\n"
            "• <i>Solches Verhalten <b>gehört bestraft</b>.</i>\n"
            "  (= Solches Verhalten <b>muss bestraft werden</b> / Bunday xatti-harakat jazolanishi shart!).\n"
            "• <i>Das Buch <b>gehört verboten</b>.</i> (= muss verboten werden).\n\n"
            "🔹 <b>2. es gilt + zu + Infinitiv (Zarurat / Bajarish talab etiladi):</b>\n"
            "• <i>Nun <b>gilt es</b>, eine Lösung <b>zu finden</b>.</i>\n"
            "  (= Jetzt muss eine Lösung gefunden werden / Endi yechim topilishi lozim!).\n\n"
            "🔹 <b>3. es bleibt + zu + Infinitiv (Kelajakdagi imkoniyat):</b>\n"
            "• <i>Es <b>bleibt abzuwarten</b>, wie sich die Krise entwickelt.</i>\n"
            "  (= Man kann nur abwarten / Buni faqat kutib ko'rish mumkin).\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "<b>'gehört + Partizip II'</b> ko'rdingizmi — bu 'muss werden' (shart)! "
            "Buning egalik (gehören mir) ga hech qanday aloqasi yo'q!"
        ),
        "quizzes": [
            {
                "id": "c1_pasers_q1",
                "question": "'Dieser Umweltzerstörer gehört sofort bestraft!' nimani bildiradi?",
                "options": [
                    "Dieser Umweltzerstörer muss sofort bestraft werden",
                    "Dieser Umweltzerstörer gehört der Polizei",
                    "Man kann ihn vielleicht bestrafen",
                    "Er hat sich selbst bestraft"
                ],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: ...muss sofort bestraft werden.</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Dudenda 'gehören + Partizip II' konstruksiyasi qat'iy ma'naviy yoki huquqiy majburiyat passivini (muss gemacht werden) bildiradi."
                ),
                "wrong_explanations": {
                    1: "❌ 'Politsiyaga tegishli' emas, bu egalik emas.",
                    2: "❌ Imkoniyat emas, qat'iy majburiyat.",
                    3: "❌ O'zlik fe'li emas."
                }
            }
        ]
    },
    {
        "id": "c1_gehobene_konnektoren",
        "level": "C1",
        "title": "7. Yuksak Akademik Bog'lovchilar (geschweige denn, ungeachtet dessen)",
        "keywords": ["c1 bog'lovchilar", "ungeachtet dessen", "geschweige denn", "wohingegen", "insofern als", "demnach"],
        "summary": "Nutqingizni C1 darajasiga olib chiqadigan yuksak akademik bog'lovchilar.",
        "content": (
            "📖 <b>7-MAVZU: Yuksak Akademik Bog'lovchilar (Gehobene Konnektoren)</b>\n\n"
            "🎯 <b>Duden Qoidasi & CEFR C1 Standarti:</b>\n"
            "• <b>geschweige denn:</b> u yoqda tursin, hatto ... ham emas (doim inkordan keyin!)\n"
            "  <i>Er hat kein Fahrrad, <b>geschweige denn</b> ein Auto.</i>\n"
            "• <b>ungeachtet dessen:</b> bularga parvo qilmay, shunga qaramasdan (trotzdem sinonimi)\n"
            "• <b>wohingegen:</b> holbuki, boshqa tomondan esa (kontrast ergash gap, fe'l oxirida)\n"
            "• <b>insofern, als...:</b> shu ma'nodaki / shuni hisobga olganda\n\n"
            "🧠 <b>BUTUN UMR ESDA QOLISH SIRI:</b>\n"
            "<b>'geschweige denn'</b> = 'U yoqda tursin!'. Har doim inkorli gapdan keyin keladi!"
        ),
        "quizzes": [
            {
                "id": "c1_konn_q1",
                "question": "'Er hat nicht einmal ein Fahrrad, ___ ein teures Auto!'",
                "options": ["geschweige denn", "ungeachtet dessen", "wohingegen", "demnach"],
                "correct_index": 0,
                "proof": (
                    "✅ <b>TO'G'RI JAVOB: geschweige denn</b>\n\n"
                    "🔍 <b>Duden qoidasiga ko'ra isbot:</b>\n"
                    "Kichik narsaning yo'qligi aytilib, undan kattaroq narsa (qimmat mashina u yoqda tursin) inkor qilinganda <b>geschweige denn</b> ishlatiladi."
                ),
                "wrong_explanations": {
                    1: "❌ 'ungeachtet dessen' (shunga qaramay) bu kontekstda ma'nosiz.",
                    2: "❌ 'wohingegen' taqqoslash ergash gapi yasaydi.",
                    3: "❌ 'demnach' demak, xulosa bildiradi."
                }
            }
        ]
    }
]
