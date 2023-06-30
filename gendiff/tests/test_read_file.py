from gendiff.read_file import read_file


def test_read_file():
    path_1 = 'gendiff/tests/fixtures/file1.json'
    path_2 = open('gendiff/tests/fixtures/test_read_file.txt')
    expected_result = path_2.read()
    assert str(read_file(path_1)) == expected_result
