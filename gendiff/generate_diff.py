from gendiff.parse import parse
from gendiff.create_diff_get import create_diff_get
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import json_dumps


def read_file(path):
    with open(path) as file:
        text_1 = file.read()
        return text_1, path


def generate_diff(old_data, new_data, format='stylish'):
    old_obj, path_1 = read_file(old_data)
    new_obj, path_2 = read_file(new_data)
    text_1 = parse(old_obj, path_1)
    text_2 = parse(new_obj, path_2)
    obj_dict = create_diff_get(text_1, text_2)

    if format == 'stylish':
        return format_stylish(obj_dict)

    elif format == 'plain':
        return format_plain(obj_dict)

    elif format == 'json':
        return json_dumps(obj_dict)
