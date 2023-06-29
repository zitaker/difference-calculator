from gendiff.formaters.stylish import stringify
from gendiff.formaters.stylish import format_stylish
import json


def test_stringify():
    path_1 = open('gendiff/tests/fixtures/test_stringify.json')
    obj_dict = json.loads(path_1.read())

    path_2 = open('gendiff/tests/fixtures/test_result_stringify.txt')
    expected_result = path_2.read()
    assert stringify(obj_dict, level=1) == expected_result


def test_format_stylish():
    path = open('gendiff/tests/fixtures/test_stringify.json')
    obj_dict = json.loads(path.read())

    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    print(type(obj_dict), obj_dict)
    print(type(expected_result), expected_result)
    assert format_stylish(obj_dict) == expected_result
