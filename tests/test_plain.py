import json

from gendiff.formaters.plain import plain
from gendiff.formaters.plain import make_str


def test_make_str():
    path_1 = open('tests/fixtures/test_make_str.json')
    expected_result_else = json.loads(path_1.read())
    expected_result_if = path_1.read()

    if isinstance(expected_result_if, str):
        assert make_str(expected_result_if) == f"'{expected_result_if}'"
    else:
        assert make_str(expected_result_if) == expected_result_else


def test_plain():
    path_1 = open('tests/fixtures/test_plain.json')
    obj_dict = json.loads(path_1.read())

    path_2 = open('tests/fixtures/test_result_plain.txt')
    expected_result = path_2.read()
    assert plain(obj_dict) == expected_result
