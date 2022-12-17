from asyncio import sleep
from random import randint, choice
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from app.keyboards.main import btn_game_coin


async def game_coin(msg: Message):
    KB_COIN = InlineKeyboardMarkup(1).add(btn_game_coin)
    await msg.answer('Испытай судьбу!  🎰', reply_markup=KB_COIN)


async def __coin(call: CallbackQuery):
    loader = (
        f'{randint(1, 10)}%   █▒▒▒▒▒▒▒▒▒▒▒▒',
        f'{randint(15, 30)}%  ███▒▒▒▒▒▒▒▒▒▒',
        f'{randint(30, 40)}%  █████▒▒▒▒▒▒▒▒',
        f'{randint(45, 55)}%  ███████▒▒▒▒▒▒',
        f'{randint(60, 75)}%  █████████▒▒▒▒',
        f'{randint(80, 90)}%  ███████████▒▒',
        '100% █████████████',
    )
    await call.message.edit_text(f'<b>🎲 Бросаю монетку.</b>', reply_markup=None)
    for i in range(2, 4):
        await call.message.edit_text(f'<b>🎲 Бросаю монетку{"." * i}</b>')
        await sleep(0.5)
    for text in loader:
        await call.message.edit_text(f'{text}')
        await sleep(0.5)
    await sleep(1)
    await call.message.edit_text(f"<b>Мой вердикт: {choice(('Орел', 'Решка'))}</b>")
