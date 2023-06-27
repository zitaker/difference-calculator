import json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.plain import make_str


def test_make_str():
    obj_dict = {
        'follow': {
            'type': 'removed',
            'value': False,
            'children': None
        }
    }

    expected_result = obj_dict
    path = open('gendiff/tests/fixtures/test_plain_make_str.txt')
    expected_result_dumps = path.read()

    if isinstance(obj_dict, str):
        assert make_str(obj_dict) == expected_result
    else:
        obj_json_dumps = json.dumps(obj_dict)
        assert make_str(obj_json_dumps) == expected_result_dumps


def test_format_plain():
    obj_dict = {
        'common': {
            'type': 'nested',
            'value': None,
            'children': {
                'follow': {
                    'type': 'added',
                    'value': False,
                    'children': None
                },
                'setting1': {
                    'type': 'unchanged',
                    'value': 'Value 1',
                    'children': None
                },
                'setting2': {
                    'type': 'removed',
                    'value': 200,
                    'children': None
                },
                'setting3': {
                    'type': 'changed',
                    'value': {
                        'old_value': True,
                        'new_value': None
                    },
                    'children': None
                },
                'setting4': {
                    'type': 'added',
                    'value': 'blah blah',
                    'children': None
                },
                'setting5': {
                    'type': 'added',
                    'value': {
                        'key5': 'value5'
                    },
                    'children': None
                },
                'setting6': {
                    'type': 'nested',
                    'value': None,
                    'children': {
                        'doge': {
                            'type': 'nested',
                            'value': None,
                            'children': {
                                'wow': {
                                    'type': 'changed',
                                    'value': {
                                        'old_value': '',
                                        'new_value': 'so much'
                                    },
                                    'children': None
                                }
                            }
                        },
                        'key': {
                            'type': 'unchanged',
                            'value': 'value',
                            'children': None
                        },
                        'ops': {
                            'type': 'added',
                            'value': 'vops',
                            'children': None
                        }
                    }
                }
            }
        },
        'group1': {
            'type': 'nested',
            'value': None,
            'children': {
                'baz': {
                    'type': 'changed',
                    'value': {
                        'old_value': 'bas',
                        'new_value': 'bars'
                    },
                    'children': None
                },
                'foo': {
                    'type': 'unchanged',
                    'value': 'bar',
                    'children': None
                },
                'nest': {
                    'type': 'changed',
                    'value': {
                        'old_value': {
                            'key': 'value'
                        },
                        'new_value': 'str'
                    },
                    'children': None
                }
            }
        },
        'group2': {
            'type': 'removed',
            'value': {
                'abc': 12345,
                'deep': {
                    'id': 45
                }
            },
            'children': None
        },
        'group3': {
            'type': 'added',
            'value': {
                'deep': {
                    'id': {
                        'number': 45
                    }
                },
                'fee': 100500
            },
            'children': None
        }
    }

    path = open('gendiff/tests/fixtures/test_result_plain.txt')
    expected_result = path.read()

    assert format_plain(obj_dict) == expected_result