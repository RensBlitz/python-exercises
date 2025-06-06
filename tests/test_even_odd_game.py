# tests/test_even_odd_game.py

import pytest
from exercises.even_odd_game import classify

def test_even():
    assert classify(4) == "wizard"

def test_odd():
    assert classify(7) == "orc" 