import json

from gendiff.formaters.json import json_dumps


def test_json_dumps():

    path_1 = open('tests/fixtures/test_result_json.json')
    expected_result = path_1.read()

    path_2 = open('tests/fixtures/test_json_dumps.txt')
    obj = json.loads(path_2.read())
    assert json_dumps(obj) == expected_result
