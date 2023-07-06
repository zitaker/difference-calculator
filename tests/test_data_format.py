from gendiff.data_format import data_format


def test_data_format():
    path = 'tests/fixtures/file1.json'
    expected_result = 'json'
    assert data_format(path) == expected_result
