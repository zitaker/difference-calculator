from gendiff.formaters.plain import create_diff_list
from gendiff.formaters.plain import create_diff_string
from gendiff.parser import file_parser


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