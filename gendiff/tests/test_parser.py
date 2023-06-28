from gendiff.generate_diff import file_parser
import json


def test_file_parser():
    path_1 = 'gendiff/tests/fixtures/file1.json'
    path_2 = open('gendiff/tests/fixtures/test_file_parser.json')
    expected_result = json.loads(path_2.read())
    if path_1.endswith('.json'):
        assert file_parser(path_1) == expected_result
