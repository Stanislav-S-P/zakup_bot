"""
Файл содержащий Token бота
"""

import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Файл .env отсутствует')
else:
    load_dotenv()


"""Токен бота"""
TOKEN = os.environ.get('TOKEN')


"""Данные БД"""
HOST = os.environ.get('HOST')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
PORT = os.environ.get('PORT')


"""Данные для вебхука"""

WEBHOOK_HOST = os.environ.get('WEBHOOK_HOST')
WEBHOOK_PATH = os.environ.get('WEBHOOK_PATH')
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
WEBAPP_HOST = os.environ.get('WEBAPP_HOST')
WEBAPP_PORT = os.environ.get('WEBAPP_PORT')
