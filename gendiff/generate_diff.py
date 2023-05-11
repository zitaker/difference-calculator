import json
from gendiff.constants import PLUS, MINUS, SPASE


# def diff_generate(file1, file2):  # noqa: C901
#     # вводим 2 файла
#     file1 = open('gendiff/tests/fixtures/file1.json')
#     file2 = open('gendiff/tests/fixtures/file2.json')
#
#     # определяем два файла для чтения человека
#     obj1 = json.loads(file1.read())
#     obj2 = json.loads(file2.read())
#
#     # переводим файлы в списки
#     obj1_translate_in_list = list(obj1.items())
#     obj2_translate_in_list = list(obj2.items())
#
#     # создаем единый список
#     unified_obj_list = list()
#
#     for key in obj1_translate_in_list:
#         if key in obj2_translate_in_list:
#             unified_obj_list.append(f"{SPASE}{key}")
#
#     for key in obj1_translate_in_list:
#         if key not in obj2_translate_in_list:
#             unified_obj_list.append(f"{MINUS}{key}")
#
#     for key in obj2_translate_in_list:
#         if key not in obj1_translate_in_list:
#             unified_obj_list.append(f"{PLUS}{key}")
#
#     # начинаем редактировать единый список
#     unified_obj_list1 = str(unified_obj_list)
#     unified_obj_list2 = unified_obj_list1.split('",')
#
#     # исключаем дубликаты
#     list_without_duplicates = []
#     for key in unified_obj_list2:
#         if key not in list_without_duplicates:
#             list_without_duplicates.append(key)
#
#     # исключаем лишние символы
#     str_without_duplicates = str(list_without_duplicates)
#     str_without_duplicates1 = str_without_duplicates.replace("[", '')
#     str_without_duplicates2 = str_without_duplicates1.replace("]", '')
#     str_without_duplicates3 = str_without_duplicates2.replace("\\',", ':')
#     str_without_duplicates4 = str_without_duplicates3.replace("'", '')
#     str_without_duplicates5 = str_without_duplicates4.replace('"', '')
#     str_without_duplicates6 = str_without_duplicates5.replace('(', '')
#     str_without_duplicates7 = str_without_duplicates6.replace(')', '')
#     str_without_duplicates8 = str_without_duplicates7.replace('\\', '')
#
#     # сортируем по алфавиту
#     list_in_alphabe_order = str_without_duplicates8.split(',  ')
#     sort_alphabetically = sorted(list_in_alphabe_order, key=lambda x: x[2:])
#
#     # исключаем лишние символы
#     sort_alphabetically_str = str(sort_alphabetically)
#     sort_alphabetically_str1 = sort_alphabetically_str.replace("[", '')
#     sort_alphabetically_str2 = sort_alphabetically_str1.replace("]", '')
#     sort_alphabetically_str3 = sort_alphabetically_str2.replace("'", '')
#     sort_alphabetically_str4 = sort_alphabetically_str3.replace(",", '\n')
#     sort_alphabetically_str5 = sort_alphabetically_str4.replace("  ", ' ')
#     sort_alphabetically_str6 = sort_alphabetically_str5.replace("  ", '   ')
#
#     sort_alphabetically_str7 = (f"{'{'}{sort_alphabetically_str6}{'}'}")
#
#     sort_alphabetically_str8 = sort_alphabetically_str7.replace("{", '{\n')
#     sort_alphabetically_str9 = sort_alphabetically_str8.replace("}", '\n}')
#
#     sort_alphabetically_str10 = sort_alphabetically_str9.lower()
#     return sort_alphabetically_str10


# # вводим 2 файла
# print(diff_generate(open('tests/fixtures/file1.json'),
#                     open('tests/fixtures/file2.json')))

# file1 = open('gendiff/tests/fixtures/file1.json')
# file2 = open('gendiff/tests/fixtures/file2.json')

# file1 = open('tests/fixtures/file1.json')
# file2 = open('tests/fixtures/file2.json')
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


def exclusion_duplicates():
    unified_obj_list = translate_to_single_list()

    # редактируем список
    unified_obj_list1 = str(unified_obj_list)
    unified_obj_list2 = unified_obj_list1.split('",')

    # исключаем дубликаты
    list_without_duplicates = []
    for key in unified_obj_list2:
        if key not in list_without_duplicates:
            list_without_duplicates.append(key)

    return list_without_duplicates


def diff_generate(file1, file2):
    list_without_duplicates = exclusion_duplicates()
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
    list_in_alphabe_order = str_without_duplicates8.split(',  ')
    sort_alphabetically = sorted(list_in_alphabe_order, key=lambda x: x[2:])

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
    return sort_alphabetically_str10
