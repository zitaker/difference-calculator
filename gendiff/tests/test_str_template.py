from gendiff.str_template import str_template
from gendiff.constants import SPACE_1, SPACE_2, SPACE_4
from gendiff.constants import UNCHANGED, ADDED, REMOVED


def test_str_template():
    symbols_dict = {UNCHANGED: SPACE_4,
                    ADDED: f"{SPACE_2}+{SPACE_1}",
                    REMOVED: f"{SPACE_2}-{SPACE_1}"}

    spaces = SPACE_4 * (-1)

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

    expected_result = [
        "{'unchanged': '    ', 'added': '  + ', 'removed': '  - '}"
        "follow: {'type': 'removed', 'value': False, 'children': None}",

        "{'unchanged': '    ', 'added': '  + ', 'removed': '  - '}"
        "host: {'type': 'unchanged', 'value': 'hexlet.io', 'children': None}",

        "{'unchanged': '    ', 'added': '  + ', 'removed': '  - '}"
        "proxy: {'type': 'removed', 'value': '123.234.53.22', "
        "'children': None}",

        "{'unchanged': '    ', 'added': '  + ', 'removed': '  - '}"
        "timeout: {'type': 'changed', 'value': {'old_value': 50, "
        "'new_value': 20}, " "'children': None}",

        "{'unchanged': '    ', 'added': '  + ', 'removed': '  - '}"
        "verbose: {'type': 'added', 'value': True, 'children': None}"
    ]

    actual_result = list()
    for key, value in obj.items():
        actual_result.append(str_template(spaces, symbols_dict, key, value))
    assert actual_result == expected_result

