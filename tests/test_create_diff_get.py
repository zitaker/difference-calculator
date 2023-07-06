import json

from gendiff.generate_diff import read_file
from gendiff.data_format import data_format
from gendiff.parse import parse
from gendiff.create_diff_get import create_diff_get


def test_create_diff_get():
    text_1 = read_file('tests/fixtures/file1.json')
    text_2 = read_file('tests/fixtures/file2.json')
    obj_format_1 = data_format('tests/fixtures/file1.json')
    obj_format_2 = data_format('tests/fixtures/file2.json')
    old_data = parse(text_1, obj_format_1)
    new_data = parse(text_2, obj_format_2)
    actual_result = create_diff_get(old_data, new_data)

    path = open('tests/fixtures/test_create_diff_get.json')
    expected_result = json.loads(path.read())
    assert actual_result == expected_result
