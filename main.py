"""Файл для запуска бота. Содержит в себе все регистраторы приложения"""
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook
from loading import dp
from handlers import start, echo
from settings.settings import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT

start.register_start_handlers(dp)
echo.register_echo_handlers(dp)


if __name__ == '__main__':
    # start_webhook(
    #     dispatcher=dp,
    #     webhook_path=WEBHOOK_PATH,
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT,
    # )
    executor.start_polling(dp, skip_updates=True)
