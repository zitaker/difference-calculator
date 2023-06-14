import json
from gendiff.constants import REMOVED, ADDED, UNCHANGED, CHANGED
from gendiff.constants import SPACE_1, SPACE_2, SPACE_4
from gendiff.str_template import str_template


symbols_dict = {UNCHANGED: SPACE_4,
                ADDED: f"{SPACE_2}+{SPACE_1}",
                REMOVED: f"{SPACE_2}-{SPACE_1}"}


def stringify(obj_dict, level):
    if isinstance(obj_dict, str):
        return obj_dict
    if isinstance(obj_dict, dict):
        result = ["{"]
        spaces = SPACE_4 * level

        for key, value in obj_dict.items():
            string_value = stringify(value, level + 1)
            result.append(f"{spaces}{key}: {string_value}")
        result.append(f"{SPACE_4 * (level - 1)}{'}'}")
        result = '\n'.join(result)
        return result
    else:
        return json.dumps(obj_dict)


def create_stylish(obj_dict, level=0):
    result = ['{']
    level += 1
    for k, v in obj_dict.items():
        spaces = SPACE_4 * (level - 1)
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
                        value.get('old_value'), level + 1)))

            result.append(
                str_template(
                    spaces, symbols_dict[ADDED], k, stringify(
                        value.get('new_value'), level + 1)))

        else:
            result.append(
                str_template(
                    spaces, symbols_dict[UNCHANGED], k, create_stylish(
                        children, level)))

    result.append(spaces + '}')
    result = '\n'.join(result)
    return result
