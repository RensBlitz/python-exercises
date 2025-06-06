# tests/test_game_leaderboard.py

import pytest
from exercises.game_leaderboard import top_players

def test_basic():
    scores = {"Alice": 150, "Bob": 200, "Carol": 100}
    assert top_players(scores) == ["Bob", "Alice", "Carol"] 