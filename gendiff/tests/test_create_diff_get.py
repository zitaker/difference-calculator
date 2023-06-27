from gendiff.create_diff_get import create_diff_get
from gendiff.parser import file_parser
import json


def test_create_diff_get():
    path_1 = file_parser('gendiff/tests/fixtures/file1.json')
    path_2 = file_parser('gendiff/tests/fixtures/file2.json')
    actual_result = create_diff_get(path_1, path_2)

    path_3 = open('gendiff/tests/fixtures/'
                  'test_create_diff_get.json')
    expected_result = json.loads(path_3.read())
    assert actual_result == expected_result
