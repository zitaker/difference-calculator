from gendiff.constants import PLUS, MINUS, SPASE
from gendiff.parser import file_parser


def create_diff_dict(dict_1, dict_2):
    list_1 = dict_1.items()
    list_2 = dict_2.items()

    diff_dict = dict()

    for key, value in list_1:
        if (key, value) in list_2:
            diff_dict[f"{SPASE}{key}"] = value

        elif (key, value) not in list_2:
            diff_dict[f"{MINUS}{key}"] = value

    for key, value in list_2:
        if (key, value) not in list_1:
            diff_dict[f"{PLUS}{key}"] = value

    return diff_dict


            # def create_diff_string(diff_list):
            #     # сортируем по алфавиту
            #     sorted_diff_list = sorted(diff_list, key=lambda x: x[4:])
            #
            #     # diff = '{'
            #     # for _ in sorted_diff_list:
            #     #     diff = f"{diff}\n{_}"
            #     #
            #     # return diff + '\n}'
            #     sorted_diff_dict = sorted_diff_list
            #     # return sorted_diff_list
            #     return sorted_diff_dict


def stringify(obj, level=0):
    spaces_count = 2
    space = " "

    if isinstance(obj, dict):
        result = "{\n"
        spaces = space * spaces_count * level

        for key, value in obj.items():
            string_value = stringify(value, level + 1)
            result += f"{spaces} {key}: {string_value}\n"

        result += f"{spaces}{'}'}"
    else:
        result = str(obj)

    return result


def generate_diff(path_1, path_2):
    dict_1 = file_parser(path_1)
    dict_2 = file_parser(path_2)

    diff_list = create_diff_dict(dict_1, dict_2)

    return stringify(diff_list)