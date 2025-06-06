# tests/test_rain_streak_counter.py

import pytest
from exercises.rain_streak_counter import longest_streak

def test_sample_week():
    week = [True, True, False, True, True, True, False]
    assert longest_streak(week) == 3 