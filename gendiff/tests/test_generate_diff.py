from gendiff.generate_diff import read_json_file
from gendiff.generate_diff import translate_to_lists
from gendiff.generate_diff import translate_to_single_list


def test_read_json_file():
    path = 'gendiff/tests/fixtures/file1.json'
    expected_result = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
    assert read_json_file(path) == expected_result


def test_translate_to_lists():
    path1 = [('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'), ('follow', False)]
    path2 = [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')]
    expected_result1 = [('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'), ('follow', False)]
    expected_result2 = [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')]
    assert translate_to_lists(path1, path2) == (expected_result1, expected_result2)


def test_translate_to_single_list():
    obj1_in_list = [('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'), ('follow', False)]
    obj2_in_list = [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')]
    expected_result = ([('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'), ('follow', False)], [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')])
    assert translate_to_lists(obj1_in_list, obj2_in_list) == expected_result