from gendiff.generate_diff import create_diff_list
from gendiff.generate_diff import create_diff_string
from gendiff.generate_diff import generate_diff
from gendiff.generate_diff import file_parser


def test_file_parser():
    path = 'gendiff/tests/fixtures/file1.json'
    expected_result = {
        'follow': False,
        'host': 'hexlet.io',
        'proxy': '123.234.53.22',
        'timeout': 50,
    }
    if path.endswith('.json'):
        assert file_parser(path) == expected_result


def test_create_diff_list():
    obj1 = file_parser('gendiff/tests/fixtures/file1.json')
    obj2 = file_parser('gendiff/tests/fixtures/file2.json')

    expected_result = [
        '    host: hexlet.io',
        '  - timeout: 50',
        '  - proxy: 123.234.53.22',
        '  - follow: false',
        '  + timeout: 20',
        '  + verbose: true',
    ]
    actual_result = create_diff_list(obj1, obj2)
    assert actual_result == expected_result


def test_create_diff_string():
    x_1 = '  + x_1'
    x_2 = '  - x_2'
    x_3 = '    x_3'
    diff_list = [
        x_1,
        x_2,
        x_3,
    ]
    expected_result = '{\n' + f'{x_1}\n{x_2}\n{x_3}\n' + '}'
    assert create_diff_string(diff_list) == expected_result


def test_generate_diff():
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'
    expected_result = open('gendiff/tests/fixtures/test_result.txt').read()
    assert generate_diff(path1, path2) == expected_result
