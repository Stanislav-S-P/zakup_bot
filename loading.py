"""Файл - инициализирующий бота, диспетчер, логгер и хранилище для машины состояния"""


from aiogram import Bot
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from logging_config import custom_logger
from settings import settings
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logger = custom_logger('bot_logger')


storage = MemoryStorage()


bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot, storage=storage)
# dp.middleware.setup(LoggingMiddleware())


# async def on_startup(dp):
#     await bot.set_webhook(settings.WEBHOOK_URL)
#     webhook = await bot.get_webhook_info()
#     if webhook.url != settings.WEBHOOK_URL:
#         if not webhook.url:
#             await bot.delete_webhook()
#         await bot.set_webhook(settings.WEBHOOK_URL, certificate=open('/home/zakup/bot_database/webhook_cert.pem', 'rb'))
#
#
# async def on_shutdown(dp):
#     await bot.delete_webhook()
#     await dp.storage.close()
#     await dp.storage.wait_closed()
