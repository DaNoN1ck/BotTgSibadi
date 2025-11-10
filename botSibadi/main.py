import re

import aiogram
import logging
import asyncio
from aiogram import F, Bot,Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums import ParseMode

import start
from config_reader import config
from aiogram.client.default import DefaultBotProperties
from aiogram import F
from get_btn import show_menu


logging.basicConfig(level=logging.INFO)
bot = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)
dp = Dispatcher()
dp.include_routers(start.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())