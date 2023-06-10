from gendiff.generate_diff import generate_diff


def test_generate_diff():
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'
    expected_result_plain = open('gendiff/tests/fixtures/test_result_plain.txt').read()
    expected_result_stylish = open('gendiff/tests/fixtures/test_result_stylish.txt').read()
    assert generate_diff(path1, path2) == expected_result_plain or expected_result_stylish
