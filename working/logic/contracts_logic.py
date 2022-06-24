from typing import Dict
from database.insert_table import insert_table_contracts


def contracts_script(path_file) -> Dict:
    with open(path_file, 'r', encoding='utf-8-sig') as file:
        db_dict = {}
        i_string = ''
        for string in file:
            if string != '\n':
                if string.endswith('\n'):
                    i_string += string[:-1]
                else:
                    i_string += string
        string_list = i_string.split('\x0b|=')
        for elem in string_list:
            template = elem.split('\x0b|8')
            if len(template) == 9:
                db_dict[template[0]] = tuple(template)
        return db_dict


def launch() -> None:
    db_correct_dict = {}
    db_list = []
    for index in range(1, 716):
        db_dict = contracts_script(f'Данные/Контракты/Контракты{index}.txt')
        for key, values in db_dict.items():
            db_correct_dict[key] = values
    for value in db_correct_dict.values():
        db_list.append(value)
    insert_table_contracts(db_list)
    print('Выполнено')


