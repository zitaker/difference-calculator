from gendiff.generate_diff import generate_diff


def test_generate_diff():
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'

    path_plain = 'gendiff/tests/fixtures/test_result_one_level_formatter.txt'
    path_stylish = 'gendiff/tests/fixtures/test_result_stylish.txt'

    expected_result = open(path_plain).read()
    expected_result2 = open(path_stylish).read()
    assert generate_diff(path1, path2) == expected_result or expected_result2
