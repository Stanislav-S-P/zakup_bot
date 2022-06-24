from database.insert_table import insert_table_units_of_measurement


def units_of_measurement_script(path_file) -> None:
    with open(path_file, 'r', encoding='utf-8-sig') as file:
        db_list = []
        for string in file:
            string_list = string.split('\x0b|=')
            for elem in string_list:
                template = elem.split('\x0b|8')
                if len(template) == 3:
                    db_list.append(tuple(template))
        insert_table_units_of_measurement(db_list)


def launch() -> None:
    units_of_measurement_script('Данные/ЕдИзм1.txt')
