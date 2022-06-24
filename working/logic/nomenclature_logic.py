from database.insert_table import insert_table_nomenclatures


def nomenclature_script(path_file) -> None:
    with open(path_file, 'r', encoding='utf-8-sig') as file:
        db_list = []
        template = []
        index = 0
        i_string = ''
        for string in file:
            string_list = string.split('\x0b|8')
            for elem in string_list:
                index += 1
                if elem.startswith('|=') and index == 1:
                    i_elem = elem[2:]
                    template.append(i_elem)
                elif index == 1:
                    template.append(elem)
                elif elem.endswith('\n') and index == 9:
                    template.append(elem[:-1])
                elif len(elem) > 1:
                    for sym in elem:
                        if sym != '\n':
                            i_string += sym
                    template.append(i_string)
                    i_string = ''
                else:
                    template.append(elem)
            if len(template) == 9:
                db_list.append(tuple(template))
            template = []
            index = 0
        insert_table_nomenclatures(db_list)


def launch() -> None:
    for index in range(1, 4150):
        if index >= 1000:
            index = str(index)
            index = index[:1] + ' ' + index[1:]
        nomenclature_script(f'Данные/Номенклатура/Номенклатура{index}.txt')
    print('Выполнено 4150')
