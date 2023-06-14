from gendiff.constants import SPACE_1, SPACE_2, SPACE_4
from gendiff.constants import UNCHANGED, ADDED, REMOVED, CHANGED
from gendiff.str_template import str_template


symbols_dict = {UNCHANGED: SPACE_4,
                ADDED: f"{SPACE_2}+{SPACE_1}",
                REMOVED: f"{SPACE_2}-{SPACE_1}"}


def create_diff_string(obj_dict, level=0):
    result = ['{']
    level += 1
    for k, v in obj_dict.items():
        spaces = SPACE_4 * (level - 1)
        types = v.get('type')
        value = v.get('value')

        if types == UNCHANGED or types == ADDED or types == REMOVED:
            result.append(
                str_template(
                    spaces, symbols_dict[types], k, value))

        elif types == CHANGED:
            result.append(
                str_template(
                    spaces, symbols_dict[REMOVED], k, value.get('old_value')))

            result.append(
                str_template(
                    spaces, symbols_dict[ADDED], k, value.get('new_value')))

        else:
            result.append(
                str_template(
                    spaces, symbols_dict[UNCHANGED], k, value))

    result.append(spaces + '}')
    result = '\n'.join(result)
    return result.lower()
