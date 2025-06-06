# tests/test_temperature_spread.py

import pytest
from exercises.temperature_spread import spread_and_average

def test_spread_and_average_basic():
    diff, avg = spread_and_average(18.0, 10.0)
    assert pytest.approx(diff, rel=1e-3) == 8.0
    assert pytest.approx(avg, rel=1e-3) == 14.0 