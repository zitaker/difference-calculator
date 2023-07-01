import json
from gendiff.generate_diff import read_file
from gendiff.generate_diff import parse


def test_parse():
    text, file_format_1 = read_file('gendiff/tests/fixtures/file1.json')
    data = parse(text, file_format_1)
    path_2 = open('gendiff/tests/fixtures/test_parser.json')
    expected_result = json.loads(path_2.read())
    if format == 'json':
        assert parse(data) == expected_result
