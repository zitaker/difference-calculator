import json
from gendiff.parser import file_parser
from gendiff.formaters.stylish import create_diff_get, create_stylish
from gendiff.formaters.plain import create_diff_list, create_diff_string


def generate_diff(path_1, path_2, format='stylish'):
    obj_1 = file_parser(path_1)
    obj_2 = file_parser(path_2)

    if format == 'stylish':
        obj_dict = create_diff_get(obj_1, obj_2)
        return create_stylish(obj_dict)

    elif format == 'plain':
        diff_list = create_diff_list(obj_1, obj_2)
        return create_diff_string(diff_list)
