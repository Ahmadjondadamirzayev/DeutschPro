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
        plural_val = w.get('plural')
        plural_info = f" ({plural_val})" if plural_val and plural_val != "-" else ""
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
