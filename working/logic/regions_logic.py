from database.insert_table import insert_table_regions


def regions_script(path_file) -> None:
    with open(path_file, 'r', encoding='utf-8-sig') as file:
        db_list = []
        for string in file:
            string_list = string.split('\x0b|=')
            for elem in string_list:
                template = elem.split('\x0b|8')
                if len(template) == 2:
                    db_list.append(tuple(template))
        insert_table_regions(db_list)


def launch() -> None:
    regions_script('Данные/Регионы1.txt')
