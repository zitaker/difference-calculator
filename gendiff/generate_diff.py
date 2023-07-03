from gendiff.data_format import data_format
from gendiff.parse import parse
from gendiff.create_diff_get import create_diff_get
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import json_dumps


def read_file(path):
    with open(path) as file:
        text = file.read()
        return text


def generate_diff(old_data, new_data, path, format='stylish'):
    # old_obj, path_1 = read_file(old_data)
    # new_obj, path_2 = read_file(new_data)
    # text_1 = parse(old_obj, path_1)
    # text_2 = parse(new_obj, path_2)
    # obj_dict = create_diff_get(text_1, text_2)

    text_1 = read_file(old_data)
    text_2 = read_file(new_data)
    obj_format_1 = data_format(path)
    obj_format_2 = data_format(path)
    old_obj = parse(text_1, obj_format_1)
    new_obj = parse(text_2, obj_format_2)
    obj_dict = create_diff_get(old_obj, new_obj)

    if format == 'stylish':
        return format_stylish(obj_dict)

    elif format == 'plain':
        return format_plain(obj_dict)

    elif format == 'json':
        return json_dumps(obj_dict)
