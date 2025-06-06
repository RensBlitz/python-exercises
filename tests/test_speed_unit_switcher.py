# tests/test_speed_unit_switcher.py

import pytest
from exercises.speed_unit_switcher import miles_to_km_per_hour

def test_basic():
    # 100 mph → 160.934 kph
    assert pytest.approx(miles_to_km_per_hour(100.0), rel=1e-3) == 160.934 