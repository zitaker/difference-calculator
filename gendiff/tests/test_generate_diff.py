from gendiff.generate_diff import read_json_file
from gendiff.generate_diff import create_diff_list
from gendiff.generate_diff import create_diff_string
from gendiff.generate_diff import generate_diff


def test_read_json_file():
    path = 'gendiff/tests/fixtures/file1.json'
    expected_result = {
        'follow': False,
        'host': 'hexlet.io',
        'proxy': '123.234.53.22',
        'timeout': 50
    }

    assert read_json_file(path) == expected_result


def test_create_diff_list():
    obj1 = read_json_file('gendiff/tests/fixtures/file1.json')
    obj2 = read_json_file('gendiff/tests/fixtures/file2.json')

    expected_result = [
        "    host: hexlet.io",
        "  - timeout: 50",
        "  - proxy: 123.234.53.22",
        "  - follow: false",
        "  + timeout: 20",
        "  + verbose: true"
    ]
    actual_result = create_diff_list(obj1, obj2)
    assert actual_result == expected_result


def test_create_diff_string():
    a = '  + a'
    b = '  - b'
    diff_list = [
        b,
        a
    ]
    expected_result = '{\n' + f'{a}\n{b}\n' + '}'
    assert create_diff_string(diff_list) == expected_result


def test_generate_diff():
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'
    expected_result = open('gendiff/tests/fixtures/test_result.txt').read()
    assert generate_diff(path1, path2) == expected_result
