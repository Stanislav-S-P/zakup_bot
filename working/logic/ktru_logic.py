from database.insert_table import insert_table_ktru_code


def ktru_script(path_file) -> None:
    with open(path_file, 'r', encoding='utf-8-sig') as file:
        db_list = []
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
            if len(template) == 5:
                db_list.append(tuple(template))
        insert_table_ktru_code(db_list)


def launch() -> None:
    for index in range(1, 8):
        ktru_script(f'Данные/КТРУ{index}.txt')
