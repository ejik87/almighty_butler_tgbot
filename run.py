from aiogram import executor
import app

if __name__ == '__main__':
    executor.start_polling(app.dp, skip_updates=True)
