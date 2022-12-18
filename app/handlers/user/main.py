from aiogram import Dispatcher, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from app.handlers.user.youtube_dl import yt_dl_message, send_youtube_file
from app.handlers.user.passwd_gen import register_handlers_password_generator
from app.handlers.user.open_weather import answer_city_weather, send_weather, CityName
from app.handlers.user.game import __coin, game_coin


async def __start(msg: Message, state: FSMContext):
    """ Стартовый хендлер предназначен для команды /start"""
    # await state.finish()
    # create_user(msg.from_user.id)  # Добавление юзера в БД
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    # keyboard = get_main_keyboard(user_id)
    await bot.send_message(user_id, f'Привет, {msg.from_user.full_name}!')
    await bot.send_message(user_id, 'Введи команду, а я исполню!\n'
                                    'Например /weather', reply_markup=ReplyKeyboardRemove())


# # @rate_limit(5, 'help')
# async def __help(msg: Message):
#     text = [
#         'Список команд: ',
#         '/start - Начать диалог',
#         '/password - Сгенерировать пароль',
#         '/weather - Погода',
#         '/help - Получить справку',
#     ]
#     await msg.answer('\n'.join(text))
#
#
# async def __support(msg: Message) -> None:
#     bot: Bot = msg.bot
#     await bot.send_message(msg.from_user.id, f"Если у вас возникли проблемы. Напишите нам - {config.HELPER_URL}")


async def __get_id(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user
    await bot.send_message(user.id, f"User: {user.username} Id: {user.id}")


# async def __cancel(message: Message, state: FSMContext):
#     await state.finish()
#     await message.answer(
#         'Действие отменено.',
#         reply_markup=ReplyKeyboardRemove()
#     )
#
#
# async def other_messages(msg: Message) -> None:
#     bot: Bot = msg.bot
#     await bot.send_message(msg.from_user.id, "Я вас не понял, напишите /start!")


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__start, commands='start', state='*')
    dp.register_message_handler(__get_id, commands=["id"])
    dp.register_message_handler(game_coin, commands=["coin"])
    dp.register_callback_query_handler(__coin, lambda c: c.data == "toss_coin")
    dp.register_message_handler(yt_dl_message, regexp=r'^https://.*?youtu.*?(be|com)/.+$', state="*")
    dp.register_callback_query_handler(send_youtube_file, Text(startswith="youtube_"))
    register_handlers_password_generator(dp)
    dp.register_message_handler(answer_city_weather, commands='weather', state='*')
    dp.register_message_handler(send_weather, content_types='text', state=CityName.city)
    # dp.register_message_handler(__start, commands='password', state='*')
    # dp.register_message_handler(__help, content_types=['text'], text="main_info")
    # dp.register_message_handler(__support, content_types=['text'], text='support')
    # dp.register_message_handler(__cancel, commands='cancel', state="*")
    # dp.register_message_handler(__cancel, Text(equals='отмена', ignore_case=True), state='*')
    # dp.register_message_handler(other_messages, content_types=['text'], state=None)

