import json
from gendiff.constants import PLUS, MINUS, SPASE


def read_json_file(path):
    # определяем файл для чтения человека в словарь
    obj = json.loads(open(path).read())
    return obj


obj1 = read_json_file('gendiff/tests/fixtures/file1.json')
obj2 = read_json_file('gendiff/tests/fixtures/file2.json')


def translate_to_lists(path1=obj1.items(), path2=obj2.items()):
    # переводим файлы в списки
    obj1_translate_in_list = list(path1)
    obj2_translate_in_list = list(path2)
    return obj1_translate_in_list, obj2_translate_in_list


obj1_translate_in_list, obj2_translate_in_list = translate_to_lists()


def translate_to_single_list(obj1_in_list=None, obj2_in_list=None):
    # создаем единый список
    if obj2_in_list is None:
        obj2_in_list = obj2_translate_in_list
    if obj1_in_list is None:
        obj1_in_list = obj1_translate_in_list

    unified_obj_list = list()

    for key in obj1_in_list:
        if key in obj2_in_list:
            unified_obj_list.append(f"{SPASE}{key}")
        elif key not in obj2_in_list:
            unified_obj_list.append(f"{MINUS}{key}")

    for key in obj2_in_list:
        if key not in obj1_in_list:
            unified_obj_list.append(f"{PLUS}{key}")

    return unified_obj_list


def diff_generate(file1, file2):
    unified_obj_list = translate_to_single_list()
    # исключаем лишние символы
    str_without_duplicates = str(unified_obj_list)
    str_without_duplicates1 = str_without_duplicates.replace("[", '')
    str_without_duplicates2 = str_without_duplicates1.replace("]", '')
    str_without_duplicates3 = str_without_duplicates2.replace("',", ':')
    str_without_duplicates4 = str_without_duplicates3.replace("('", '')
    str_without_duplicates5 = str_without_duplicates4.replace("'", '')
    str_without_duplicates6 = str_without_duplicates5.replace(",", '')

    # сортируем по алфавиту
    list_in_alphabe_order = str_without_duplicates6.split(')" ')
    sort_alphabetically = sorted(list_in_alphabe_order, key=lambda x: x[3:])

    sort_alphabetically_str = str(sort_alphabetically)

    str_without_duplicates7 = sort_alphabetically_str.replace(",", '\n')
    str_without_duplicates8 = str_without_duplicates7.replace("'", '')
    str_without_duplicates9 = str_without_duplicates8.replace('"', '')
    str_without_duplicates10 = str_without_duplicates9.replace('[', ' ')
    str_without_duplicates11 = str_without_duplicates10.replace(')]', '')

    str_without_duplicates12 = (f"{'{'}{str_without_duplicates11}{'}'}")
    str_without_duplicates13 = str_without_duplicates12.replace("{", '{\n')
    str_without_duplicates14 = str_without_duplicates13.replace("}", '\n}')

    str_without_duplicates15 = str_without_duplicates14.lower()
    return str_without_duplicates15
