"""Файл - содержит сообщения бота, для общей замены в приложении"""


INCORRECT_INPUT = 'Ошибка ввода. Данной команды не существует. Введи /help и ознакомься с командами бота'
WELCOME = 'Привет, это ZakupMarket!\n\nТут можно изучить рынок госзаказов. 2021 год - бесплатно.\n\nПо вопросам доступа: @introman2020'
HELP = 'Список команд бота:\n\n/help - Помощь\n/search - Поиск'
SEARCH_REQUEST = 'Для изучения рынка введите ключевые слова через пробел. Например: ручк шарик'
AWAIT_ANSWER = 'Подождите немного, идёт загрузка результатов ⏱'
NONE_RESULT = 'К сожалению, по заданным критериям ничего не найдено'
TOP_RESULT = "*Запрос:* {}\n*Всего закупок за 2021г:* {}\n*Средний чек:* {:,} руб\n*Всего рынок:*  {:,} млн руб\n*Недружественные страны:* {}% (доля рынка которая шла из недружественных стран)\n\n\n"
DATE = '*{}*\n\n'
NAME = '{}\n\n'
QUANTITY = "{} {} по  {:,}руб, итого  {:,}руб\n\n"
CLIENT = 'Заказчик: {}\n\n'
CONTRACTOR = 'Поставщик: {}\n\n'
REGION = 'Регион: {}\n\n'
COUNTRY = 'Страна изготовитель: {}\n\n'
TEN_RESPONSE = '10 контрактов по запросу'