from gendiff.generate_diff import file_parser


def test_file_parser():
    path = 'gendiff/tests/fixtures/file1.json'
    expected_result = {
        'follow': False,
        'host': 'hexlet.io',
        'proxy': '123.234.53.22',
        'timeout': 50,
    }
    if path.endswith('.json'):
        assert file_parser(path) == expected_result
