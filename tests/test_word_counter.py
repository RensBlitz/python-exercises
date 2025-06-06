# tests/test_word_counter.py

import pytest
from exercises.word_counter import count_words

def test_basic():
    sentence = "hello world hello"
    expected = {"hello": 2, "world": 1}
    assert count_words(sentence) == expected 