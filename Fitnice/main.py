import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from Fitnice.handlers import main_router
from Fitnice.middlewares import CustomMiddleware

TOKEN = "7037879367:AAG0ISCCehaD3XKZT8K6Ka7D0Rk-w14gS_0"

#https://t.me/asfbaksbot token qoyilgan botni linki
# Docker hubga yuklolmadim, eski proyektlarni kodini copy qilib qoydim faqat.


dp = Dispatcher()

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(*[main_router])
    dp.update.middleware(CustomMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
