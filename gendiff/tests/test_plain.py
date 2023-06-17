from gendiff.formaters.plain import plain


def test_path_keys():
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
        },
        'verbose': {
            'type': 'added',
            'value': True,
            'children': None}
    }

    path = open('gendiff/tests/fixtures/test_plain.txt')
    expected_result = path.read()

    assert plain(obj_dict) == expected_result
