from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from utils.bot_commands import set_bot_commands
from config import BOT_API_TOKEN
import logging
from handlers.main import register_user_handlers


logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=BOT_API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

register_user_handlers(dp)


async def on_startup(dispatcher):
    await set_bot_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
