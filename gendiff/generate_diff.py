from gendiff.constants import PLUS, MINUS, SPASE
from gendiff.parser import file_parser


def create_diff_list(dict_1, dict_2):
    list_1 = dict_1.items()
    list_2 = dict_2.items()
    diff_list = list()

    for _, value in list_1:
        if (_, value) in list_2:
            diff_list.append(f"{SPASE}{_}: {value}".lower())
        elif (_, value) not in list_2:
            diff_list.append(f"{MINUS}{_}: {value}".lower())

    for _, value in list_2:
        if (_, value) not in list_1:
            diff_list.append(f"{PLUS}{_}: {value}".lower())

    return diff_list


def create_diff_string(diff_list):
    sorted_diff_list = sorted(diff_list, key=lambda x: x[3:])

    diff = '{'
    for _ in sorted_diff_list:
        diff = f"{diff}\n{_}"

    return diff + '\n}'


def generate_diff(path_1, path_2):
    obj_1 = file_parser(path_1)
    obj_2 = file_parser(path_2)

    diff_list = create_diff_list(obj_1, obj_2)
    return create_diff_string(diff_list)
