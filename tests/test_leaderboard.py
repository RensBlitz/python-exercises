# tests/test_leaderboard.py

from exercises.leaderboard import top_three


def test_top_three_basic():
    players = [
        {"name": "A", "points": 90},
        {"name": "B", "points": 70},
        {"name": "C", "points": 80},
        {"name": "D", "points": 95}
    ]
    top = top_three(players)
    assert top[0] == "1. D (95)"
    assert len(top) == 3
