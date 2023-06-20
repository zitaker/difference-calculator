from gendiff.formaters.plain import plain
# from gendiff.formaters.plain import make_str
#
#
# def test_make_str():
#     obj_dict = {
#         'follow': {
#             'type': 'removed',
#             'value': False,
#             'children': None
#         },
#         'host': {
#             'type': 'unchanged',
#             'value': 'hexlet.io',
#             'children': None
#         },
#         'proxy': {
#             'type': 'removed',
#             'value': '123.234.53.22',
#             'children': None
#         },
#         'timeout': {
#             'type': 'changed',
#             'value': {
#                 'old_value': 50,
#                 'new_value': 20
#             }, 'children': None
#         }, 'verbose': {
#             'type': 'added',
#             'value': True,
#             'children': None
#         }
#     }
#
#     if isinstance(obj_dict, str):
#         return f"'{obj_dict}'"
#         assert
#     else:
#         return json.dumps(element)



def test_plain():
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

    assert plain(obj_dict) == expected_result
