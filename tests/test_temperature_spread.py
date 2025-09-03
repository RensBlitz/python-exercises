# tests/test_temperature_spread.py

from exercises.temperature_spread import spread_and_average


def test_spread_and_average_basic():
    result = spread_and_average(18.0, 10.0)
    assert result[0] == 8.0
    assert result[1] == 14.0 