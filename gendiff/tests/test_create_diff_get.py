import json
from gendiff.read_file import read_file
from gendiff.parser import parser
from gendiff.create_diff_get import create_diff_get


def test_create_diff_get():
    text_1, file_format_1 = read_file('gendiff/tests/fixtures/file1.json')
    text_2, file_format_2 = read_file('gendiff/tests/fixtures/file2.json')
    old_data = parser(text_1, file_format_1)
    new_data = parser(text_2, file_format_2)
    actual_result = create_diff_get(old_data, new_data)

    path = open('gendiff/tests/fixtures/test_create_diff_get.json')
    expected_result = json.loads(path.read())
    assert actual_result == expected_result
