import json


def generate_diff():
    # вводим два файла
    string_as_json_format1 = open('file1_json.json')
    obj1 = json.loads(string_as_json_format1.read())

    string_as_json_format2 = open('file2_json.json')
    obj2 = json.loads(string_as_json_format2.read())

    PLUS = " + "
    MINUS = " - "
    SPASE = "   "

    # переводим файлы в списки
    obj1_translate_in_list = list(obj1.items())
    obj2_translate_in_list = list(obj2.items())

    # создаем единый список
    unified_obj_list = list()

    for key in obj1_translate_in_list:
        if key in obj2_translate_in_list:
            unified_obj_list.append(f"{SPASE}{key}")

    for key in obj1_translate_in_list:
        if key not in obj2_translate_in_list:
            unified_obj_list.append(f"{MINUS}{key}")

    for key in obj2_translate_in_list:
        if key not in obj1_translate_in_list:
            unified_obj_list.append(f"{PLUS}{key}")

    # начинаем редактировать единый список
    unified_obj_list1 = str(unified_obj_list)
    unified_obj_list2 = unified_obj_list1.split('",')

    # исключаем дубликаты
    list_without_duplicates = []
    for key in unified_obj_list2:
        if key not in list_without_duplicates:
            list_without_duplicates.append(key)

    # исключаем лишние символы
    str_without_duplicates = str(list_without_duplicates)
    str_without_duplicates1 = str_without_duplicates.replace("[", '')
    str_without_duplicates2 = str_without_duplicates1.replace("]", '')
    str_without_duplicates3 = str_without_duplicates2.replace("\\',", ':')
    str_without_duplicates4 = str_without_duplicates3.replace("'", '')
    str_without_duplicates5 = str_without_duplicates4.replace('"', '')
    str_without_duplicates6 = str_without_duplicates5.replace('(', '')
    str_without_duplicates7 = str_without_duplicates6.replace(')', '')
    str_without_duplicates8 = str_without_duplicates7.replace('\\', '')

    # сортируем по алфавиту
    list_in_alphabetical_order = str_without_duplicates8.split(',  ')
    sort_alphabetically = sorted(list_in_alphabetical_order, key=lambda x: x[2:])

    # исключаем лишние символы
    sort_alphabetically_str = str(sort_alphabetically)
    sort_alphabetically_str1 = sort_alphabetically_str.replace("[", '')
    sort_alphabetically_str2 = sort_alphabetically_str1.replace("]", '')
    sort_alphabetically_str3 = sort_alphabetically_str2.replace("'", '')
    sort_alphabetically_str4 = sort_alphabetically_str3.replace(",", '\n')
    sort_alphabetically_str5 = sort_alphabetically_str4.replace("  ", ' ')
    sort_alphabetically_str6 = sort_alphabetically_str5.replace("  ", '   ')

    sort_alphabetically_str7 = (f"{'{'}{sort_alphabetically_str6}{'}'}")

    sort_alphabetically_str8 = sort_alphabetically_str7.replace("{", '{\n')
    sort_alphabetically_str9 = sort_alphabetically_str8.replace("}", '\n}')

    sort_alphabetically_str10 = sort_alphabetically_str9.lower()
    print(sort_alphabetically_str10)


generate_diff()
