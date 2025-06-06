# tests/test_mini_rpg.py

import pytest
from exercises.mini_rpg import simulate_battle

def test_basic():
    damages = [10, 20, 30]
    assert simulate_battle(100, damages) == 40 