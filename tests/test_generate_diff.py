import json

from gendiff.generate_diff import read_file
from gendiff.generate_diff import generate_diff
from gendiff.data_format import data_format
from gendiff.parse import parse
from gendiff.generate_diff import create_diff_get


def test_read_file():
    path = 'tests/fixtures/file1.json'
    expected_result = open(path).read()
    assert str(read_file(path)) == expected_result

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


def test_generate_diff():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'

    path_stylish = 'tests/fixtures/test_result_stylish.txt'
    path_plain = 'tests/fixtures/test_result_plain.txt'
    path_json = 'tests/fixtures/test_result_json.json'

    expected_result_1 = open(path_stylish).read()
    expected_result_2 = open(path_plain).read()
    expected_result_3 = open(path_json).read()
    assert generate_diff(path1, path2) == expected_result_1 or \
           expected_result_2 or expected_result_3
