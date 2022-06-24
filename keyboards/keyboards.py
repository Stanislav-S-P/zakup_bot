"""
Файл - содержит клавиатуры бота
"""


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards import key_text


def start_keyboard() -> ReplyKeyboardMarkup:
    """
    Функция - создаёт и возвращает клавиатуру главного меню бота
    :return: ReplyKeyboardMarkup
    """
    keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    first_key = KeyboardButton(text=key_text.SEARCH)
    second_key = KeyboardButton(text=key_text.HELP)
    return keyboards.add(first_key, second_key)