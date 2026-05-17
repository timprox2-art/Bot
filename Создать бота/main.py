import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import handlers  # Импортируем нашу папку с логикой

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем единый роутер со всеми обработчиками
    dp.include_router(handlers.router)

    print("Модульный бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())