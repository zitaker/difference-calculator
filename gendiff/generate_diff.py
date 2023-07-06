import os.path

from gendiff.constants import REMOVED, ADDED, UNCHANGED, NESTED, CHANGED
from gendiff.parse import parse
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import json_dumps


def read_file(path):
    with open(path) as file:
        text = file.read()
        return text


def create_diff_get(old_data, new_data):
    result = dict()
    all_keys = sorted(old_data.keys() | new_data.keys())

    for key in all_keys:
        if key not in new_data:
            result[key] = {
                'type': REMOVED,
                'value': old_data[key],
                'children': None
            }

        elif key not in old_data:
            result[key] = {
                'type': ADDED,
                'value': new_data[key],
                'children': None
            }

        elif old_data[key] == new_data[key]:
            result[key] = {
                'type': UNCHANGED,
                'value': old_data[key],
                'children': None
            }

        elif isinstance(old_data[key], dict) and \
                isinstance(new_data[key], dict):
            result[key] = {
                'type': NESTED,
                'value': None,
                'children': create_diff_get(old_data[key], new_data[key])
            }

        else:
            result[key] = {
                'type': CHANGED,
                'value': {
                    'old_value': old_data[key],
                    'new_value': new_data[key]
                },
                'children': None
            }

    return result


def data_format(path):
    format = os.path.splitext(path)[-1].lstrip('.')
    return format


def generate_diff(old_data, new_data, format='stylish'):
    text_1 = read_file(old_data)
    text_2 = read_file(new_data)
    obj_format_1 = data_format(old_data)
    obj_format_2 = data_format(new_data)
    old_obj = parse(text_1, obj_format_1)
    new_obj = parse(text_2, obj_format_2)
    obj_dict = create_diff_get(old_obj, new_obj)

    if format == 'stylish':
        return format_stylish(obj_dict)

    elif format == 'plain':
        return format_plain(obj_dict)

    elif format == 'json':
        return json_dumps(obj_dict)
