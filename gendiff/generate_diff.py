# from gendiff.constants import PLUS, MINUS, SPASE
from gendiff.constants import REMOVED, ADDED, UNCHANGED, NESTED, CHANGED
from gendiff.parser import file_parser


def create_diff_get(dict_1, dict_2):
    result = dict()
    all_keys = sorted(dict_1.keys() | dict_2.keys())

    for key in all_keys:
        if key not in dict_2:
            result[key] = {
                'type': REMOVED,
                'value': dict_1[key],
                'children': None
            }

        elif key not in dict_1:
            result[key] = {
                'type': ADDED,
                'value': dict_2[key],
                'children': None
            }

        elif dict_1[key] == dict_2[key]:
            result[key] = {
                'type': UNCHANGED,
                'value': dict_1[key],
                'children': None
            }

        elif isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
            result[key] = {
                'type': NESTED,
                'value': None,
                'children': create_diff_get(dict_1[key], dict_2[key])
            }

        else:
            result[key] = {
                'type': CHANGED,
                'value': {
                    'old_value': dict_1[key],
                    'new_value': dict_2[key]
                },
                'children': None
            }

    return result


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

    diff_get = create_diff_get(dict_1, dict_2)

    return stringify(diff_get)