from gendiff.generate_diff import read_json_file
from gendiff.generate_diff import translate_to_lists
from gendiff.generate_diff import translate_to_single_list
from gendiff.generate_diff import diff_generate


def test_read_json_file():
    path = 'gendiff/tests/fixtures/file1.json'
    expected_result = {'follow': False, 'host': 'hexlet.io',
                       'proxy': '123.234.53.22', 'timeout': 50}

    assert read_json_file(path) == expected_result


def test_translate_to_lists():  # noqa: N400
    obj1 = [('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'),
            ('follow', False)]

    obj2 = [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')]
    expected_result1 = [('host', 'hexlet.io'), ('timeout', 50),
                        ('proxy', '123.234.53.22'), ('follow', False)]

    expected_result2 = [('timeout', 20), ('verbose', True),
                        ('host', 'hexlet.io')]

    assert translate_to_lists(obj1, obj2) == \
           (expected_result1, expected_result2)


def test_translate_to_single_list():
    obj1 = None
    obj2 = None
    expected_result = ["   ('host', 'hexlet.io')", " - ('timeout', 50)",
                       " - ('proxy', '123.234.53.22')",
                       " - ('follow', False)", " + ('timeout', 20)",
                       " + ('verbose', True)"]
    assert translate_to_single_list(obj1, obj2) == expected_result


def test_diff_generate():
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'
    expected_result = open('gendiff/tests/fixtures/test_result.txt').read()
    assert diff_generate(path1, path2) == expected_result
