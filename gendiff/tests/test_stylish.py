from gendiff.formaters.stylish import stringify
from gendiff.formaters.stylish import format_stylish
import json


def test_stringify():
    path_1 = open('gendiff/tests/fixtures/test_stringify.json')
    obj_dict = json.loads(path_1.read())

    path_2 = open('gendiff/tests/fixtures/test_result_stringify.txt')
    expected_result = path_2.read()
    assert stringify(obj_dict, level=1) == expected_result


# def test_format_stylish():
#     # obj = {
#     #     "follow": {
#     #         "type": "removed",
#     #         "value": False,
#     #         "children": None
#     #     },
#     #     "host": {
#     #         "type": "unchanged",
#     #         "value": "hexlet.io",
#     #         "children": None
#     #     },
#     #     "proxy": {
#     #         "type": "removed",
#     #         "value": "123.234.53.22",
#     #         "children": None
#     #     },
#     #     "timeout": {
#     #         "type": "changed",
#     #         "value": {
#     #             "old_value": 50,
#     #             "new_value": 20
#     #         },
#     #         "children": None
#     #     },
#     #     "verbose": {
#     #         "type": "added",
#     #         "value": True,
#     #         "children": None
#     #     }
#     # }
#
#     path_1 = open('gendiff/tests/fixtures/test_stringify.json')
#     obj_dict = json.loads(path_1.read())
#
#     path_2 = open('gendiff/tests/fixtures/test_result_stylish.txt')
#     expected_result = path_2.read()
#
# #     expected_result = """{
# #   - follow: false
# #     host: hexlet.io
# #   - proxy: 123.234.53.22
# #   - timeout: 50
# #   + timeout: 20
# #   + verbose: true
# # }"""
#     print(type(expected_result))
#     assert format_stylish(obj_dict) == expected_result
