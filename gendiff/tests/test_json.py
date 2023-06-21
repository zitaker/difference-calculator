from gendiff.formaters.json import json_dumps


def test_json_dumps():
    obj = {
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
        },
        'verbose': {
            'type': 'added',
            'value': True,
            'children': None
        }
    }

    path = open('gendiff/tests/fixtures'
                '/test_result_json.txt')
    expected_result = path.read()

    assert json_dumps(obj) == expected_result
