from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, BotCommand
# from utils.bot_commands import set_bot_commands
from app.config import BOT_API_TOKEN
import logging
from handlers.main import register_user_handlers


logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=BOT_API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

register_user_handlers(dp)
bot.set_my_commands(
        commands=[
            BotCommand('start', "Запуск бота"),
            BotCommand('id', "Получить свой Telegram ID"),
            BotCommand('password', "Генератор паролей"),
            BotCommand('weather', "Прогноз погоды"),
        ], language_code='ru')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
