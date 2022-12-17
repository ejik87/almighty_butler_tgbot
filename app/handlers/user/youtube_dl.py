from aiogram.types import Message, CallbackQuery, ParseMode
from os import remove
from app.keyboards.main import KB_YOUTUBE
from pytube import YouTube


def youtube_download(url, output_type='audio'):
    """ Функция загрузки файлов с Youtube"""
    download_dir = '../../downloads'
    chars = ['.', ',', '!', '/', '=', '\\', '$', '?', '%', '>', '<']
    youto = YouTube(url)
    file_id = youto.title.translate({ord(x): '' for x in chars})  # убираем лишние символы из названия
    if output_type == 'video':
        file_name = f'{file_id}.mp4'
        youto.streams.filter(mime_type="video/mp4", progressive=True).desc().first().download(download_dir, file_name)
        return f'{download_dir}/{file_name}'
    elif output_type == 'audio':
        file_name = f'{file_id}.mp3'
        youto.streams.filter(only_audio=True).first().download(download_dir, file_name)
        return f'{download_dir}/{file_name}'


# @dp.message_handler(regexp=r'^https://.*?youtu.*?(be|com)/.+$', state="*")
async def yt_dl_message(msg: Message):
    await msg.reply('Что вы хотите загрузить?', reply_markup=KB_YOUTUBE, allow_sending_without_reply=True)


# @dp.callback_query_handler(Text(startswith="youtube_"))
async def send_youtube_file(call: CallbackQuery):
    await call.message.edit_text('Уже загружаю! ☝️ Стоит немного подождать...', reply_markup=None)
    url = call.message.reply_to_message.text
    action = call.data.split("_")[1]
    if action in ['audio', 'video']:
        downloaded_file_path = youtube_download(url, output_type=action)
        await call.answer()
    elif action == 'cancel':
        await call.message.delete()
        await call.message.reply_to_message.delete()
        await call.answer()
        return
    else:
        downloaded_file_path = youtube_download(url)

    dl_file = open(f'{downloaded_file_path}', 'rb')
    await call.message.edit_text(f'👋 Я загрузил для тебя {action} файл! 👇')
    await call.message.reply_to_message.delete()
    try:
        if downloaded_file_path.endswith('.mp3'):
            await call.bot.send_audio(call.message.chat.id, dl_file)
        elif downloaded_file_path.endswith('.mp4'):
            await call.bot.send_video(call.message.chat.id, dl_file)
        else:
            await call.bot.send_document(call.message.chat.id, dl_file)
    except:
        await call.message.answer('Не удалось загрузить файл ❌')
    finally:
        remove(f'{downloaded_file_path}')


# test = 'https://youtu.be/w13bG7j5vc4'
