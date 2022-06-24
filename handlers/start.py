import random
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from database.database import select_table_nomenclatures, select_add_information
from database.models import FSMSearch
from keyboards import key_text
from keyboards.keyboards import start_keyboard
from loading import bot, logger
from settings import constants


async def start_command(message: types.Message) -> None:
    """
    Хэндлер - обрабатывает команду start
    :param message: Message
    :return: None
    """
    try:
        await bot.send_message(message.from_user.id, constants.WELCOME)
        await bot.send_message(message.from_user.id, constants.SEARCH_REQUEST)
    except Exception as error:
        logger.error('В работе бота возникло исключение', exc_info=error)


async def help_command(message: types.Message) -> None:
    """
    Хэндлер - обрабатвает команду /help
    :param message: Message
    :return: None
    """
    try:
        await bot.send_message(message.from_user.id, constants.HELP)
    except Exception as error:
        logger.error('В работе бота возникло исключение', exc_info=error)


# async def search_command(message: types.Message) -> None:
#     """
#     Хэндлер - обрабатвает команду /search, входит в машину состояния
#     :param message: Message
#     :return: None
#     """
#     try:
#         await FSMSearch.search.set()
#         await bot.send_message(message.from_user.id, constants.SEARCH_REQUEST)
#     except Exception as error:
#         logger.error('В работе бота возникло исключение', exc_info=error)


async def search_state(message: types.Message) -> None:
    """
    Хэндлер - обрабатывает состояние search
    :param message: Message
    :return: None
    """
    try:
        # await state.finish()
        word_list = message.text.split()
        await bot.send_message(message.from_user.id, constants.AWAIT_ANSWER)
        await bot.send_message(message.from_user.id, constants.TEN_RESPONSE)
        nomenclatures_list = select_table_nomenclatures(word_list)
        if nomenclatures_list:
            total_purchase = len(nomenclatures_list)
            total_sum = 0
            unfriendly = 0
            for elem in nomenclatures_list:
                if elem[5] != '':
                    total_sum += float(elem[5])
                if elem[10] is True:
                    unfriendly += 1
            average_check = int(total_sum / total_purchase)
            set_ten = set()
            index = 0
            while len(set_ten) != 10 and index != 35:
                index += 1
                set_ten.add(random.randint(0, total_purchase - 1))
            result_list = []
            for i in set_ten:
                result_list.append(nomenclatures_list[i])
            for elem in result_list:
                info_list = select_add_information(elem)
                template = ''
                if elem[6] != '':
                    template += constants.DATE.format(elem[6])
                template += constants.NAME.format(elem[0])
                if elem[1] == '' and elem[5] == '':
                    pass
                elif elem[1] == elem[5]:
                    template += constants.QUANTITY.format(1, info_list[0], float(elem[1]), float(elem[5]))
                elif elem[2] != '' and elem[1] != '' and elem[5] != '':
                    template += constants.QUANTITY.format(elem[2], info_list[0], float(elem[1]), float(elem[5]))
                elif elem[1] != '' and elem[2] != '':
                    template += constants.QUANTITY.format(
                        elem[2], info_list[0], float(elem[1]), round(int(elem[2]) * float(elem[1]), 2)
                    )
                elif elem[2] != '' and elem[5] != '':
                    template += constants.QUANTITY.format(
                        elem[2], info_list[0], round(float(elem[5]) / int(elem[2]), 2), float(elem[5])
                    )
                elif elem[1] != '' and elem[5] != '':
                    template += constants.QUANTITY.format(
                        round(float(elem[5]) / float(elem[1]), 2), info_list[0], float(elem[1]), float(elem[5])
                    )
                if info_list[1] != '':
                    template += constants.CLIENT.format(info_list[1])
                if info_list[2] != '':
                    template += constants.CONTRACTOR.format(info_list[2])
                if info_list[3] != '':
                    template += constants.REGION.format(info_list[3])
                if info_list[4] != '':
                    template += constants.COUNTRY.format(info_list[4])
                await bot.send_message(message.from_user.id, template, parse_mode='Markdown')
            total_sum = str(int(total_sum))[:-4]
            total_summ = float(total_sum[:-2] + '.' + total_sum[len(total_sum) - 2:])
            percent = round(unfriendly / (total_purchase / 100), 1)
            await bot.send_message(
                message.from_user.id, constants.TOP_RESULT.format(
                    message.text, total_purchase, int(average_check), total_summ, percent
                ), parse_mode='Markdown'
            )
        else:
            await bot.send_message(message.from_user.id, constants.NONE_RESULT)

    except Exception as error:
        logger.error('В работе бота возникло исключение', exc_info=error)


# async def cancel_state(message: types.Message, state: FSMContext) -> None:
#     """
#     Хэндлер - реагирует на команды и выводит из машины состояния пользователя
#     :param message: Message
#     :param state: FSMContext
#     :return: None
#     """
#     try:
#         current_state = await state.get_state()
#         if current_state is not None:
#             await state.finish()
#         if message.text == '/start':
#             await start_command(message)
#         elif message.text == '/help' or message.text == key_text.HELP:
#             await help_command(message)
#         elif message.text == '/search' or message.text == key_text.SEARCH:
#             await search_command(message)
#     except Exception as error:
#         logger.error('В работе бота возникло исключение', exc_info=error)


def register_start_handlers(dp: Dispatcher) -> None:
    """
    Функция - регистрирует все хэндлеры файла start.py
    :param dp: Dispatcher
    :return: None
    """
    # dp.register_message_handler(cancel_state, Text(startswith=['/start', '/help', '/search']), state='*')
    # dp.register_message_handler(cancel_state, Text(startswith=[key_text.HELP, key_text.SEARCH]), state='*')
    dp.register_message_handler(start_command, commands=['start'], state=None)
    dp.register_message_handler(help_command, commands=['help'], state=None)
    dp.register_message_handler(help_command, lambda message: message.text == key_text.HELP, state=None)
    # dp.register_message_handler(search_command, commands=['search'], state=None)
    # dp.register_message_handler(search_command, lambda message: message.text == key_text.SEARCH, state=None)
    dp.register_message_handler(search_state, content_types=['text'])
