# ==========================================
# ASOSIY STARTUP (BOT VA WEB SERVER BIRGA)
# ==========================================

async def main():
    logger.info("Nemis Tili Duden, Goethe & Worthub Boti ishga tushmoqda...")
    logger.info(f"Rasmiy Veb-Sayt: {config.WEBSITE_URL}")
    logger.info(f"Jami Duden darslari: {len(ALL_TOPICS)} ta")

    # Flask veb-serverni alohida oqimda (background thread) ishga tushiramiz (UptimeRobot uchun)
    threading.Thread(target=run_web_server, daemon=True).start()
    logger.info("Render uchun HTTP web-server portni tinglashni boshladi.")

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot to'xtatildi.")
