"""
Файл с запросами создания таблиц в БД
"""
import psycopg2
from sqlite3 import Cursor
from typing import Callable, Any
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
def create_table_okpd2_code(cursor: Cursor) -> None:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "okpd2_code" (code VARCHAR(30) PRIMARY KEY, name TEXT);"""
    )


@db_decorator
def create_table_countries(cursor: Cursor) -> None:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "countries" (code VARCHAR(30) PRIMARY KEY, name TEXT, unfriendly BOOL)"""
    )


@db_decorator
def create_table_regions(cursor: Cursor) -> None:
    cursor.execute("""CREATE TABLE IF NOT EXISTS "regions" (code VARCHAR(30) PRIMARY KEY UNIQUE , name TEXT)"""
    )


@db_decorator
def create_table_units_of_measurement(cursor: Cursor) -> None:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "units_of_measurement" (code VARCHAR(30) PRIMARY KEY, name TEXT, full_name TEXT)"""
    )


@db_decorator
def create_table_ktru_code(cursor: Cursor) -> None:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "ktru_code" (id VARCHAR(30) PRIMARY KEY, name TEXT, okpd2_code  VARCHAR(30), description TEXT, type_of_medical_device TEXT)"""
    )


@db_decorator
def create_table_counterparty(cursor: Cursor) -> None:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "counterparty" (id VARCHAR(30) PRIMARY KEY UNIQUE, name TEXT, full_name TEXT, inn VARCHAR(30), kpp VARCHAR(30), address TEXT, region  TEXT, okved_code TEXT)"""
    )


@db_decorator
def create_table_contracts(cursor: Cursor) -> None:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "contracts" (id VARCHAR(30) PRIMARY KEY UNIQUE, date_of_conclusion TEXT, client VARCHAR(30), contractor VARCHAR(30), notification_number TEXT, region  TEXT, contract_amount VARCHAR(30), subject_of_the_contract TEXT, method_of_devermining_the_supplier VARCHAR(30))"""
    )


@db_decorator
def create_table_nomenclatures(cursor: Cursor) -> None:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "nomenclatures" (id SERIAL, contract_number VARCHAR(30), nomenclature TEXT, price TEXT, quantity VARCHAR(30), ktru_code VARCHAR(30), okpd2_code VARCHAR(30), unit_of_measurement VARCHAR(30), country VARCHAR(30), cost TEXT)"""
    )


create_table_okpd2_code()
create_table_countries()
create_table_regions()
create_table_units_of_measurement()
create_table_ktru_code()
create_table_counterparty()
create_table_contracts()
create_table_nomenclatures()
