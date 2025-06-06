# tests/test_simple_dungeon_crawler.py

import pytest
from exercises.simple_dungeon_crawler import simulate

def test_basic():
    actions = ["hit", "potion", "hit", "hit"]
    assert simulate(actions) == 4 