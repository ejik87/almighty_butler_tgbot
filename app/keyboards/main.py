from typing import Final
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

icons = '1️⃣ 2️⃣ 3️⃣ 3️ 4️⃣ 5️⃣ 6️⃣ 9️⃣ 👋 🗺️ 📌 ☎️ 📞 ☝️ 🎲 ✉️ ✅ ⛔️ ❌ ⚠️ ➕ ✨ 🤡 💸 👍 👆 👇 👉 👈 👌 🤘 ☝️' \
        ' 🌍 ☀️ 🌤 ⛅️ 🌥 ☁️ 🌦 🌧 🌩 🌨 ❄️ 🌬 💨 ☔️ ☂️ 🔑 🗝 🚪 🛒 🧳 🛠 🔋 📲 📬 📆 📝 ✏️ 🔍 🔙 🔚 🌡 👀 🎰'
btn_info = InlineKeyboardButton(text='Информация о способностях бота 📌', callback_data='main_info')

btn_next = InlineKeyboardButton(text='Продолжить ✅', callback_data='next')
btn_accept = InlineKeyboardButton(text='Принять ✅', callback_data='accept')
btn_cancel = InlineKeyboardButton(text='Отмена ❌', callback_data='cancel')

btn_add = InlineKeyboardButton(text='Добавить ➕', callback_data='btn_add')
btn_remove = InlineKeyboardButton(text='Удалить ⛔️', callback_data='btn_remove')
btn_exit = InlineKeyboardButton(text='Выйти ⛔️', callback_data='next')

btn_locate = InlineKeyboardButton(text='Отправить местоположение 🌍', request_location=True)

btn_admin_add = InlineKeyboardButton('Добавить администратора ➕', callback_data='admin_add'),
btn_give_reg = InlineKeyboardButton('Назначить привелегии ✨', callback_data='give_reg'),
btn_adv = InlineKeyboardButton('Оповещение ✉️', callback_data='advertising'),
btn_admin_exit = InlineKeyboardButton('Выйти ⛔️', callback_data='admin_exit')

btn_reg_request = InlineKeyboardButton('Получить доступ 💸', callback_data='access_request')
btn_support = InlineKeyboardButton('Тех.поддержка ⚙', callback_data='support')  # TODO вставить адрес поддержки
btn_admin_panel = InlineKeyboardButton('Панель Администратора', callback_data='admin_panel')

btn_youtube_audio = InlineKeyboardButton('Аудио', callback_data='youtube_audio')
btn_youtube_video = InlineKeyboardButton('Видео', callback_data='youtube_video')
btn_youtube_cancel = InlineKeyboardButton('Отмена ❌', callback_data='youtube_cancel')

btn_game_coin = InlineKeyboardButton('Бросить монетку 🎰', callback_data='toss_coin')

KB_START: Final = InlineKeyboardMarkup().add(btn_info)  # Стартовые кнопки
KB_STOP: Final = InlineKeyboardMarkup().add(btn_cancel)
KB_LOCATE: Final = InlineKeyboardMarkup().add(btn_locate)  # Запрос местоположения
KB_YOUTUBE: Final = InlineKeyboardMarkup(2).row(btn_youtube_audio, btn_youtube_video).add(btn_youtube_cancel)
