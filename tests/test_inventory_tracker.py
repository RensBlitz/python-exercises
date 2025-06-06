# tests/test_inventory_tracker.py

import pytest
from exercises.inventory_tracker import update_inventory

def test_basic():
    inv = {"apple": 10, "banana": 5}
    purchases = {"apple": 3, "banana": 1}
    expected = {"apple": 7, "banana": 4}
    assert update_inventory(inv, purchases) == expected 