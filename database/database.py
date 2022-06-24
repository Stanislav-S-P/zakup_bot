"""
Файл - с запросами бота к БД и декоратором коннекта к БД
"""

import psycopg2
from sqlite3 import Cursor
from typing import Callable, Any, List, Union, Tuple
from loading import logger
from settings.settings import HOST, USER, PASSWORD, DB_NAME, PORT


def db_decorator(func: Callable) -> Any:
    """
    Декоратор - Подключается к базе данных
    :param func: Callable
    :return: Any
    """
    def wrapped_func(*args, **kwargs):
        try:
            connection = psycopg2.connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DB_NAME,
                port=PORT
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                result = func(*args, **kwargs, cursor=cursor)
                return result
        except Exception as ex:
            logger.error('Ошибка БД', exc_info=ex)
            print(ex, 'Ошибка БД')
        finally:
            connection.close()
    return wrapped_func


@db_decorator
def select_table_nomenclatures(word_list: List,  cursor: Cursor) -> Union[List, None]:
    base_select = """SELECT n.nomenclature, n.price, n.quantity, n.unit_of_measurement, n.country, n.cost, c.date_of_conclusion, c.client, c.contractor, c.region, l.unfriendly FROM nomenclatures n JOIN contracts c ON c.id = n.contract_number JOIN countries l ON n.country = l.code WHERE n.nomenclature ILIKE '% {}%'"""
    part_select = """ AND n.nomenclature ILIKE '% {}%'"""
    end_select = """ AND c.date_of_conclusion LIKE '%21'"""
    for index in range(len(word_list)):
        if index == 0:
            base_select = base_select.format(word_list[index])
        else:
            base_select += part_select.format(word_list[index])
    base_select += end_select
    cursor.execute(base_select)
    result = cursor.fetchall()
    return result


@db_decorator
def select_add_information(elem: Tuple, cursor: Cursor) -> List:
    info_list = []
    if elem[3] != '':
        cursor.execute("""SELECT name, full_name FROM units_of_measurement WHERE code=%s""", (elem[3], ))
        unit, *_ = cursor.fetchall()
        if unit[0] != '':
            info_list.append(unit[0])
        else:
            info_list.append(unit[1])
    else:
        info_list.append(elem[3])
    if elem[7] != '':
        cursor.execute("""SELECT name, full_name FROM counterparty WHERE id=%s""", (elem[7], ))
        counter, *_ = cursor.fetchall()
        if counter[0] != '':
            info_list.append(counter[0])
        else:
            info_list.append(counter[1])
    else:
        info_list.append(elem[7])
    if elem[8] != '':
        cursor.execute("""SELECT name, full_name FROM counterparty WHERE id=%s""", (elem[8], ))
        counter, *_ = cursor.fetchall()
        if counter[0] != '':
            info_list.append(counter[0])
        else:
            info_list.append(counter[1])
    else:
        info_list.append(elem[8])
    if elem[9] != '':
        cursor.execute("""SELECT name FROM regions WHERE code=%s""", (elem[9], ))
        region, *_ = cursor.fetchone()
        info_list.append(region)
    else:
        info_list.append(elem[9])
    if elem[4] != '':
        cursor.execute("""SELECT name FROM countries WHERE code=%s""", (elem[4], ))
        country, *_ = cursor.fetchone()
        info_list.append(country)
    else:
        info_list.append(elem[4])
    return info_list
