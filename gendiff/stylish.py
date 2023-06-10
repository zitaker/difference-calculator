import json
from gendiff.parser import file_parser
from gendiff.constants import REMOVED, ADDED, UNCHANGED, NESTED, CHANGED
from gendiff.constants import SPACE_1, SPACE_2, SPASE


def create_diff_get(path_1, path_2):
    result = dict()
    all_keys = sorted(path_1.keys() | path_2.keys())

    for key in all_keys:
        if key not in path_2:
            result[key] = {
                'type': REMOVED,
                'value': path_1[key],
                'children': None
            }

        elif key not in path_1:
            result[key] = {
                'type': ADDED,
                'value': path_2[key],
                'children': None
            }

        elif path_1[key] == path_2[key]:
            result[key] = {
                'type': UNCHANGED,
                'value': path_1[key],
                'children': None
            }

        elif isinstance(path_1[key], dict) and isinstance(path_2[key], dict):
            result[key] = {
                'type': NESTED,
                'value': None,
                'children': create_diff_get(path_1[key], path_2[key])
            }

        else:
            result[key] = {
                'type': CHANGED,
                'value': {
                    'old_value': path_1[key],
                    'new_value': path_2[key]
                },
                'children': None
            }

    return result


symbols_dict = {UNCHANGED: SPACE,
                ADDED: f"{SPACE_2}+{SPACE_1}",
                REMOVED: f"{SPACE_2}-{SPACE_1}"}


def str_template(spaces, symbol, key, value):
    return f'{spaces}{symbol}{key}: {value}'


def stringify(obj_dict, level):
    if isinstance(obj_dict, str):
        return obj_dict
    if isinstance(obj_dict, dict):
        result = ["{"]
        spaces = SPACE * level

        for key, value in obj_dict.items():
            string_value = stringify(value, level + 1)
            result.append(f"{spaces}{key}: {string_value}")
        result.append(f"{SPACE * (level - 1)}{'}'}")
        result = '\n'.join(result)
        return result
    else:
        return json.dumps(obj_dict)


def create_stylish(obj_dict, level=0):
    result = ['{']
    level += 1
    for k, v in obj_dict.items():
        spaces = SPACE * (level - 1)
        types = v.get('type')
        value = v.get('value')
        children = v.get('children')

        if types == UNCHANGED or types == ADDED or types == REMOVED:
            result.append(
                str_template(
                    spaces, symbols_dict[types], k, stringify(
                        value, level + 1)))

        elif types == CHANGED:
            result.append(
                str_template(
                    spaces, symbols_dict[REMOVED], k, stringify(
                        value.get('old_type'), level + 1)))

            result.append(
                str_template(
                    spaces, symbols_dict[ADDED], k, stringify(
                        value.get('new_type'), level + 1)))

        else:
            result.append(
                str_template(
                    spaces, symbols_dict[UNCHANGED], k, create_stylish(
                        children, level)))

    result.append(spaces + '}')
    result = '\n'.join(result)
    return result


def stylish_diff(path_1, path_2):
    obj_dict = create_diff_get(path_1, path_2)
    return create_stylish(obj_dict)
