import json
from gendiff.constants import REMOVED, ADDED, NESTED, CHANGED
from gendiff.constants import COMPLEX_VALUE, ADDED_TEMPLATE
from gendiff.constants import REMOVED_TEMPLATE, CHANGED_TEMPLATE


def make_str(element):
    if isinstance(element, str):
        return f"'{element}'"
    else:
        return json.dumps(element)


def format_plain(data, name=''):   # noqa: C901
    result = []
    for key, value in data.items():
        path = f'{name}.{key}'.lstrip('.')
        types = value.get('type')
        values = value.get('value')
        children = value.get('children')

        if types == ADDED:
            if isinstance(values, dict):
                values = COMPLEX_VALUE
            else:
                values = make_str(values)
            result.append(ADDED_TEMPLATE.format(path, values))

        elif types == REMOVED:
            result.append(REMOVED_TEMPLATE.format(path))

        elif types == CHANGED:
            if isinstance(values.get('old_value'), dict):
                old = COMPLEX_VALUE
                new = make_str(values.get('new_value'))
            elif isinstance(values.get('new_value'), dict):
                old = make_str(values.get('old_value'))
                new = COMPLEX_VALUE
            else:
                old = make_str(values.get('old_value'))
                new = make_str(values.get('new_value'))
            result.append(CHANGED_TEMPLATE.format(path, old, new))

        elif types == NESTED:
            if isinstance(children, dict):
                result.append(format_plain(children, path))

    result = '\n'.join(result)
    return result
