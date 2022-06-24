"""
Файл с запросами добавления записей в таблицы БД
"""
import psycopg2
from sqlite3 import Cursor
from typing import Callable, Any, Tuple
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
            print(ex, 'Ошибка БД')
        finally:
            connection.close()
    return wrapped_func


@db_decorator
def insert_table_okpd2_code(tuple_record: Tuple,  cursor: Cursor) -> None:
    cursor.executemany(
        """INSERT INTO okpd2_code (code, name) VALUES (%s, %s)""", tuple_record
    )


@db_decorator
def insert_table_countries(tuple_record: Tuple,  cursor: Cursor) -> None:
    cursor.executemany(
        """INSERT INTO countries (code, name, unfriendly) VALUES (%s, %s, %s)""", tuple_record
    )


@db_decorator
def insert_table_regions(tuple_record: Tuple,  cursor: Cursor) -> None:
    cursor.executemany(
        """INSERT INTO regions (code, name) VALUES (%s, %s)""", tuple_record
    )


@db_decorator
def insert_table_units_of_measurement(tuple_record: Tuple,  cursor: Cursor) -> None:
    cursor.executemany(
        """INSERT INTO units_of_measurement (code, name, full_name) VALUES (%s, %s, %s)""", tuple_record
    )


@db_decorator
def insert_table_ktru_code(tuple_record: Tuple,  cursor: Cursor) -> None:
    cursor.executemany(
        """INSERT INTO ktru_code (id, name, okpd2_code, description, type_of_medical_device) VALUES (%s, %s, %s, %s, %s)""", tuple_record
    )


@db_decorator
def insert_table_counterparty(tuple_record: Tuple,  cursor: Cursor) -> None:
    cursor.executemany(
        """INSERT INTO counterparty (id, name, full_name, inn, kpp, address, region, okved_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", tuple_record
    )


@db_decorator
def insert_table_contracts(tuple_record: Tuple,  cursor: Cursor) -> None:
    cursor.executemany(
        """INSERT INTO contracts (id, date_of_conclusion, client, contractor, notification_number, region, contract_amount, subject_of_the_contract, method_of_devermining_the_supplier) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", tuple_record
    )


@db_decorator
def insert_table_nomenclatures(tuple_record: Tuple,  cursor: Cursor) -> None:
    cursor.executemany(
        """INSERT INTO nomenclatures (contract_number, nomenclature, price, quantity, ktru_code, okpd2_code, unit_of_measurement, country, cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", tuple_record
    )
