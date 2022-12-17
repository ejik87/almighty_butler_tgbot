from aiogram.types import BotCommand


async def set_bot_commands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand('start', "Запуск бота"),
            BotCommand('id', "Получить свой Telegram ID"),
            BotCommand('password', "Генератор паролей"),
            BotCommand('weather', "Прогноз погоды"),
        ]
    )
