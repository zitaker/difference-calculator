import json

from gendiff.generate_diff import read_file
from gendiff.data_format import data_format
from gendiff.generate_diff import parse


def test_parse():
    path = 'tests/fixtures/file1.json'
    text = read_file(path)
    file_format = data_format(text)
    data = parse(text, file_format)
    expected_result = json.loads(open(path).read())
    if format == 'json':
        assert data == expected_result
