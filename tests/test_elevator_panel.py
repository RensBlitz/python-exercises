# tests/test_elevator_panel.py

import pytest
from exercises.elevator_panel import is_valid_floor

def test_negative():
    assert is_valid_floor(-1) is False

def test_ground():
    assert is_valid_floor(0) is True

def test_too_high():
    assert is_valid_floor(21) is False 