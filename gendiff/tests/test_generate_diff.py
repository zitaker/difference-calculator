from gendiff.generate_diff import generate_diff


def test_generate_diff():
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'

    obj_txt_1 = 'gendiff/tests/fixtures/test_result_plain.txt'
    obj_txt_2 = 'gendiff/tests/fixtures/test_result_stylish.txt'

    expected_plain = open(obj_txt_1).read()
    expected_stylish = open(obj_txt_2).read()
    assert generate_diff(path1, path2) == expected_plain or expected_stylish
