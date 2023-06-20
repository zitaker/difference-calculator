import json
from gendiff.constants import REMOVED, ADDED, NESTED, CHANGED
from gendiff.constants import COMPLEX_VALUE, ADDED_TEMPLATE, REMOVED_TEMPLATE, CHANGED_TEMPLATE


def make_str(element):
    if isinstance(element, str):
        return f"'{element}'"
    else:
        return json.dumps(element)


def plain(obj_dict, name=''):
    result = []
    for k, v in obj_dict.items():
        path = f'{name}.{k}'.lstrip('.')
        types = v.get('type')
        value = v.get('value')
        children = v.get('children')

        if types == ADDED:
            if isinstance(value, dict):
                value = COMPLEX_VALUE
            else:
                value = make_str(value)
            result.append(ADDED_TEMPLATE.format(path, value))

        elif types == REMOVED:
            result.append(REMOVED_TEMPLATE.format(path))

        elif types == CHANGED:
            if isinstance(value.get('old_value'), dict):
                old = COMPLEX_VALUE
                new = make_str(value.get('new_value'))
            elif isinstance(value.get('new_value'), dict):
                old = make_str(value.get('old_value'))
                new = COMPLEX_VALUE
            else:
                old = make_str(value.get('old_value'))
                new = make_str(value.get('new_value'))
            result.append(CHANGED_TEMPLATE.format(path, old, new))

        elif types == NESTED:
            if isinstance(children, dict):
                result.append(plain(children, path))

    result = '\n'.join(result)
    return result
