from gendiff.generate_diff import read_file
from gendiff.generate_diff import generate_diff


def test_read_file():
    path_1 = 'gendiff/tests/fixtures/file1.json'
    path_2 = open('gendiff/tests/fixtures/test_read_file.txt')
    expected_result = path_2.read()
    assert str(read_file(path_1)) == expected_result


def test_generate_diff():
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'

    path_stylish = 'gendiff/tests/fixtures/test_result_stylish.txt'
    path_plain = 'gendiff/tests/fixtures/test_result_plain.txt'
    path_json = 'gendiff/tests/fixtures/test_result_json.json'

    expected_result_1 = open(path_stylish).read()
    expected_result_2 = open(path_plain).read()
    expected_result_3 = open(path_json).read()
    assert generate_diff(path1, path2) == expected_result_1 or \
           expected_result_2 or expected_result_3
