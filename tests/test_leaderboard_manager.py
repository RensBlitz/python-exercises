# tests/test_leaderboard_manager.py

import pytest
from exercises.leaderboard_manager import update_top_three

def test_basic():
    top3 = [100, 90, 80]
    updated = update_top_three(top3, 85)
    # Should insert 85 between 90 and 80, dropping 80
    assert updated == [100, 90, 85] 