# tests/test_vowel_counter.py

from exercises.vowel_counter import count


def test_count_basic():
    m = count("Hello World")
    assert m['e'] == 1
    assert m['o'] == 1
