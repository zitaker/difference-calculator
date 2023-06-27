from gendiff.create_diff_get import create_diff_get
from gendiff.parser import file_parser


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

    # path_3 = open('gendiff/tests/fixtures/test_create_diff_get_result.txt')
    # expected_result = path_3.read()
    # expected_result = {'follow': {'children': None, 'type': 'removed', 'value': False}, 'host': {'children': None, 'type': 'unchanged', 'value': 'hexlet.io'}, 'proxy': {'children': None, 'type': 'removed', 'value': '123.234.53.22'}, 'timeout': {'children': None, 'type': 'changed', 'value': {'new_value': 20, 'old_value': 50}}, 'verbose': {'children': None, 'type': 'added', 'value': True}}
    assert actual_result == expected_result
