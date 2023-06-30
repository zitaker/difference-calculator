from gendiff.read_file import read_file
from gendiff.parser import parser
from gendiff.create_diff_get import create_diff_get
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import json_dumps


def generate_diff(old_data, new_data, format='stylish'):
    text_1, file_format1 = read_file(old_data)
    text_2, file_format2 = read_file(new_data)
    old_obj = parser(text_1, file_format1)
    new_obj = parser(text_2, file_format2)
    obj_dict = create_diff_get(old_obj, new_obj)

    if format == 'stylish':
        return format_stylish(obj_dict)

    elif format == 'plain':
        return format_plain(obj_dict)

    elif format == 'json':
        return json_dumps(obj_dict)
