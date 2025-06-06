# tests/test_grade_average.py

import pytest
from exercises.grade_average import average

def test_basic():
    # (5 + 7 + 9) / 3 = 7.0
    assert pytest.approx(average(5.0, 7.0, 9.0), rel=1e-3) == 7.0 