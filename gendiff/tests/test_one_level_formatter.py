from gendiff.formaters.one_level_formatter import create_diff_string


def test_create_diff_string():
    obj_dict = {
        'follow': {'type': 'removed', 'value': False, 'children': None},
        'host': {'type': 'unchanged', 'value': 'hexlet.io', 'children': None},
        'proxy': {'type': 'removed', 'value': '123.234.53.22',
                  'children': None},
        'timeout': {'type': 'changed',
                    'value': {'old_value': 50, 'new_value': 20},
                    'children': None},
        'verbose': {'type': 'added', 'value': True, 'children': None}
    }

    expected_result = """{
      - follow: false
        host: hexlet.io
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: true
    }"""

    assert create_diff_string(obj_dict, level=1) == expected_result
