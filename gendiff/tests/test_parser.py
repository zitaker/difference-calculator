import json
from gendiff.read_file import read_file
from gendiff.generate_diff import parser


def test_parser():
    text, file_format_1 = read_file('gendiff/tests/fixtures/file1.json')
    data = parser(text, file_format_1)
    path_2 = open('gendiff/tests/fixtures/test_parser.json')
    expected_result = json.loads(path_2.read())
    if format == 'json':
        assert parser(data) == expected_result
