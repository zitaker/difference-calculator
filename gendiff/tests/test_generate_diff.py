import json
from gendiff.constants import PLUS, MINUS, SPASE
from gendiff.generate_diff import is_dictionary


def test_is_dictionary():
    assert is_dictionary({'qwerty': '123'}, {'qwerty1': '1123'}) == ({'qwerty': '123'}, {'qwerty1': '1123'})