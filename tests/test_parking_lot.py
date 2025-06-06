# tests/test_parking_lot.py

import pytest
from exercises.parking_lot import turned_away

def test_basic():
    # capacity = 3, arrivals count = 4 → one turned away
    assert turned_away(3, [1, 2, 3, 4]) == 1 