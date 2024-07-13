import secretData
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = secretData.BOT_TOKEN

BOT = Bot(token=TOKEN)

dp = Dispatcher()
router = Router()

@dp.message(CommandStart())
async def main(message: Message):
    await message.reply("Hello! I'm a simple Telegram bot. Type '/start' to get started.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())