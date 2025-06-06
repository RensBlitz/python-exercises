# tests/test_moon_weight_converter.py

import pytest
from exercises.moon_weight_converter import to_moon_weight

def test_to_moon_weight_sixty_kg():
    # 60 × 0.165 = 9.9
    assert pytest.approx(to_moon_weight(60.0), rel=1e-3) == 9.9 