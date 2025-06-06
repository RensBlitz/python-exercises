# tests/test_tip_calculator.py

import pytest
from exercises.tip_calculator import calculate_tip_in_cents

def test_basic():
    # bill = 1000¢ ($10.00), tip_percent=15 → tip = 150¢
    assert calculate_tip_in_cents(1000, 15) == 150 