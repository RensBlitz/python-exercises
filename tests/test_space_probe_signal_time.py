# tests/test_space_probe_signal_time.py

import pytest
from exercises.space_probe_signal_time import round_trip_seconds

def test_moon_distance():
    # One-way: 384_400 km. Round-trip = 2 × 384_400 / 299_792 ≈ 2.565
    expected = (2 * 384_400.0) / 299_792.0
    assert pytest.approx(round_trip_seconds(384_400.0), rel=1e-4) == expected 