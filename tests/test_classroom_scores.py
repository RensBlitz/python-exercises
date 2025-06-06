# tests/test_classroom_scores.py

import pytest
from exercises.classroom_scores import average

def test_basic():
    scores = [80, 90, 100]
    assert pytest.approx(average(scores), rel=1e-3) == 90.0 