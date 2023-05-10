from gendiff.generate_diff import read_json_file


def test_read_json_file():
    path = open('gendiff/tests/fixtures/file1.json')
    expected_result = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
    assert read_json_file(path) == expected_result
