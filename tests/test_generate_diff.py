from gendiff.generate_diff import read_file
from gendiff.generate_diff import generate_diff


def test_read_file():
    path = 'tests/fixtures/file1.json'
    expected_result = open(path).read()
    assert str(read_file(path)) == expected_result


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
