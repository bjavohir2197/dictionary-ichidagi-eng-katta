import pytest

def find_max_key(dictionary):
    if not dictionary:
        return None
    return max(dictionary, key=dictionary.get)

def test_find_max_key():
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    assert find_max_key(dictionary) == 'c'

def test_find_max_key_empty():
    dictionary = {}
    assert find_max_key(dictionary) is None

def test_find_max_key_single():
    dictionary = {'a': 1}
    assert find_max_key(dictionary) == 'a'

def test_find_max_key_equal():
    dictionary = {'a': 1, 'b': 1}
    assert find_max_key(dictionary) in ['a', 'b']

def test_find_max_key_negative():
    dictionary = {'a': -1, 'b': -2, 'c': -3}
    assert find_max_key(dictionary) == 'a'
