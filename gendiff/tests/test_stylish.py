from gendiff.parser import file_parser
from gendiff.create_diff_get import create_diff_get
from gendiff.formaters.stylish import stringify
from gendiff.formaters.stylish import format_stylish


def test_create_diff_get():
    path_1 = file_parser('gendiff/tests/fixtures/file1.json')
    path_2 = file_parser('gendiff/tests/fixtures/file2.json')
    actual_result = create_diff_get(path_1, path_2)

    expected_result = {
        "follow": {
            "type": "removed",
            "value": False,
            "children": None
        },
        "host": {
            "type": "unchanged",
            "value": "hexlet.io",
            "children": None
        },
        "proxy": {
            "type": "removed",
            "value": "123.234.53.22",
            "children": None
        },
        "timeout": {
            "type": "changed",
            "value": {
                "old_value": 50,
                "new_value": 20
            },
            "children": None
        },
        "verbose": {
            "type": "added",
            "value": True,
            "children": None
        }
    }
    assert actual_result == expected_result


def test_stringify():
    obj_dict = {
        'follow': {
            'type': 'removed',
            'value': False,
            'children': None
        },
        'host': {
            'type': 'unchanged',
            'value': 'hexlet.io',
            'children': None
        },
        'proxy': {
            'type': 'removed',
            'value': '123.234.53.22',
            'children': None
        },
        'timeout': {
            'type': 'changed',
            'value': {
                'old_value': 50,
                'new_value': 20
            },
            'children': None
        }, 'verbose': {
            'type': 'added',
            'value': True,
            'children': None
        }
    }

    path = open('gendiff/tests/fixtures/test_result_stringify.txt')
    expected_result = path.read()
    assert stringify(obj_dict, level=1) == expected_result


def test_format_stylish():
    obj = {
        "follow": {
            "type": "removed",
            "value": False,
            "children": None
        },
        "host": {
            "type": "unchanged",
            "value": "hexlet.io",
            "children": None
        },
        "proxy": {
            "type": "removed",
            "value": "123.234.53.22",
            "children": None
        },
        "timeout": {
            "type": "changed",
            "value": {
                "old_value": 50,
                "new_value": 20
            },
            "children": None
        },
        "verbose": {
            "type": "added",
            "value": True,
            "children": None
        }
    }

    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert format_stylish(obj) == expected_result
