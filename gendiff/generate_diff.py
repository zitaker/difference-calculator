from gendiff.parser import file_parser
from gendiff.create_diff_get import create_diff_get
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import json_dumps


def generate_diff(old_data, new_data, format='stylish'):
    old_obj = file_parser(old_data)
    new_obj = file_parser(new_data)
    obj_dict = create_diff_get(old_obj, new_obj)

    if format == 'stylish':
        return format_stylish(obj_dict)

    elif format == 'plain':
        return format_plain(obj_dict)

    elif format == 'json':
        return json_dumps(obj_dict)
