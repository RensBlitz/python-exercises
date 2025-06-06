# tests/test_fizz_buzz_lite.py

import pytest
from exercises.fizz_buzz_lite import generate

def test_sequence():
    seq = generate()
    assert len(seq) == 20
    assert seq[2] == "Fizz"   # 3 → "Fizz"
    assert seq[3] == "4"      # 4 → "4"
    assert seq[5] == "Fizz"   # 6 → "Fizz" 