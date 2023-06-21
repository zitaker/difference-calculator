from gendiff.parser import file_parser
from gendiff.create_diff_get import create_diff_get
from gendiff.formaters.stylish import create_stylish
from gendiff.formaters.one_level_formatter import create_diff_string
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json_dumps


def generate_diff(path_1, path_2, format='stylish'):
    obj_1 = file_parser(path_1)
    obj_2 = file_parser(path_2)

    if format == 'stylish':
        obj_dict = create_diff_get(obj_1, obj_2)
        return create_stylish(obj_dict)

    elif format == 'one_level_formatter':
        obj_dict = create_diff_get(obj_1, obj_2)
        return create_diff_string(obj_dict)

    elif format == 'plain':
        obj_dict = create_diff_get(obj_1, obj_2)
        return plain(obj_dict)

    elif format == 'json':
        obj_dict = create_diff_get(obj_1, obj_2)
        return json_dumps(obj_dict)
