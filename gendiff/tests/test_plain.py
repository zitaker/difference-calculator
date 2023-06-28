import json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.plain import make_str


def test_make_str():
    path_1 = open('gendiff/tests/fixtures/test_make_str_if.json')
    expected_result = json.loads(path_1.read())

    path_2 = open('gendiff/tests/fixtures/test_make_str_else.json')
    expected_result_dumps = path_2.read()

    if isinstance(expected_result, str):
        assert make_str(expected_result) == expected_result
    else:
        assert make_str(expected_result) == expected_result_dumps


def test_format_plain():
    path_1 = open('gendiff/tests/fixtures/test_plain.json')
    obj_dict = json.loads(path_1.read())

    path_2 = open('gendiff/tests/fixtures/test_result_plain.txt')
    expected_result = path_2.read()
    assert format_plain(obj_dict) == expected_result
