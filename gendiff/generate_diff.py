# import json
import yaml
# from yaml.loader import SafeLoader
# from gendiff.constants import PLUS, MINUS, SPASE


def compare_files(path):
    path_obj = open(path)
    # obj = yaml.load(path_obj, Loader=SafeLoader)
    obj = yaml.load(path_obj, Loader=yaml.FullLoader)
    return obj


# def read_json_file(path):
#     # определяем файл для чтения человека в словарь
#     obj = json.loads(open(path).read())
#     return obj


# def create_diff_list(dict_1, dict_2):
#     # создаем единый список
#     list_1 = dict_1.items()
#     list_2 = dict_2.items()
#     diff_list = list()
#
#     for _, value in list_1:
#         if (_, value) in list_2:
#             diff_list.append(f"{SPASE}{_}: {value}".lower())
#         elif (_, value) not in list_2:
#             diff_list.append(f"{MINUS}{_}: {value}".lower())
#
#     for _, value in list_2:
#         if (_, value) not in list_1:
#             diff_list.append(f"{PLUS}{_}: {value}".lower())
#
#     return diff_list
#
#
# def create_diff_string(diff_list):
#     # сортируем по алфавиту
#     sorted_diff_list = sorted(diff_list, key=lambda x: x[3:])
#
#     diff = '{'
#     for _ in sorted_diff_list:
#         diff = f"{diff}\n{_}"
#
#     return diff + '\n}'


def generate_diff(path_1, path_2):
    obj_1 = compare_files(path_1)
    obj_2 = compare_files(path_2)
    return obj_1, obj_2

    # obj_1 = read_json_file(path_1)
    # obj_2 = read_json_file(path_2)

    # diff_list = create_diff_list(obj_1, obj_2)
    # return create_diff_string(diff_list)
