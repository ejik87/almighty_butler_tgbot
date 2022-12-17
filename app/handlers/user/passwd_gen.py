from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from random import choice
from datetime import datetime


# ================================= PASSWORDS GENERATOR =========================================
async def gen_pwd(pwd_len, pwd_count=5) -> list:
    """ Gen List Passwords. Parameters length and counts variants passwords """
    try:
        chars = '_^&!?@abcdefghijklnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ1234567890'
        pwd_list = []
        for count in range(int(pwd_count)):
            passwd = ''
            for char in range(int(pwd_len)):
                passwd += choice(chars)
            pwd_list.append(passwd)
        return pwd_list
    except (ValueError, TypeError):
        return ['Ошибка! Введите значение только цифрами.']


class GeneratePassword(StatesGroup):
    waiting_length_password = State()
    waiting_count_password = State()


# async def password_gen_start(message: Message, state: FSMContext):
#     kb = InlineKeyboardMarkup(row_width=3)
#     for count in range(6, 24, 2):
#         kb.add(str(count))
#     await message.answer('Укажите длинну пароля:', reply_markup=kb)
#     await state.set_state(GeneratePassword.waiting_length_password.state)
#
#
# async def password_count_set(call: CallbackQuery, state: FSMContext):
#     if not call.message.text.isdigit() and len(call.message.text) < 32:
#         await call.message.answer('Необходимо вводить цифру от 6 до 32.')
#         return
#     await state.update_data(len_password=call.message.text)
#     kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     for count in range(2, 20, 2):
#         kb.add(str(count))
#     await state.set_state(GeneratePassword.waiting_count_password.state)
#     await call.message.answer('Сколько штук сделать?')


async def password_generate(msg: Message, state: FSMContext):
    # if not message.text.isdigit() and len(message.text) < 21:
    #     await message.answer('Необходимо вводить цифры от 1 до 20.')
    #     return
    # user_data = await state.get_data()
    # passwords_list = await gen_pwd(user_data['len_password'], message.text)
    passwords_list = await gen_pwd(12, 5)

    await msg.bot.send_message(msg.from_user.id, f'Время генерации {datetime.now()}')
    for p in passwords_list:
        await msg.bot.send_message(msg.from_user.id, p)
    await state.finish()


def register_handlers_password_generator(dp: Dispatcher):
    dp.register_message_handler(password_generate, commands='password', state='*')
    # dp.register_message_handler(password_gen_start, commands='password', state='*')
    # # dp.register_callback_query_handler(password_gen_start, callback='gen_password', state='*')
    # dp.register_message_handler(password_count_set, state=GeneratePassword.waiting_length_password)
    # dp.register_message_handler(password_generate, state=GeneratePassword.waiting_count_password)

