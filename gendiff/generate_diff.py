import json
from gendiff.constants import PLUS, MINUS, SPASE


def read_json_file(path):
    # определяем файл для чтения человека в словарь
    obj = json.loads(open(path).read())
    return obj


def create_diff_list(a_dict, b_dict):
    # создаем единый список
    a_list = a_dict.items()
    b_list = b_dict.items()
    diff_list = list()

    for key, value in a_list:
        if (key, value) in b_list:
            diff_list.append(f"{SPASE}{key}: {value}".lower())
        elif (key, value) not in b_list:
            diff_list.append(f"{MINUS}{key}: {value}".lower())

    for key, value in b_list:
        if (key, value) not in a_list:
            diff_list.append(f"{PLUS}{key}: {value}".lower())

    return diff_list


def create_diff_string(diff_list):
    # сортируем по алфавиту
    sorted_diff_list = sorted(diff_list, key=lambda x: x[3:])

    diff = '{'
    for item in sorted_diff_list:
        diff = f"{diff}\n{item}"

    return diff + '\n}'


def generate_diff(path1, path2):
    obj1 = read_json_file(path1)
    obj2 = read_json_file(path2)

    diff_list = create_diff_list(obj1, obj2)
    return create_diff_string(diff_list)
