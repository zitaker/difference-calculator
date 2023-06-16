from gendiff.formaters.plain import path_keys


def test_path_keys():
    # obj_dict = {'1k': '1v', '2k': '2v', '3k': {'4k': '4v', '5k': {'6k': '6v'}}}
    # obj_dict = {'3k': {'5k': {'6k': '6v'}}}
    obj_dict = {'group1': {'type': 'nested', 'value': None, 'children': {
         'baz': {'type': 'changed', 'value': {'old_value': 'bas', 'new_value': 'bars'}, 'children': None},
         'foo': {'type': 'unchanged', 'value': 'bar', 'children': None},
         'nest': {'type': 'changed', 'value': {'old_value': {'key': 'value'}, 'new_value': 'str'}, 'children': None}}}}

    # expected_result = '3k.5k.6k'
    expected_result = 'group1.baz.foo.nest'

    assert path_keys(obj_dict) == expected_result
