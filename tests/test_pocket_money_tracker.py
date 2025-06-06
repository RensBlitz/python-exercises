# tests/test_pocket_money_tracker.py

import pytest
from exercises.pocket_money_tracker import calculate_total

def test_calculate_total():
    assert calculate_total(5, 3) == 8 