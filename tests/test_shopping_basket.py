# tests/test_shopping_basket.py

import pytest
from exercises.shopping_basket import calculate_total

def test_basic():
    prices = [2.50, 3.00, 4.75]
    assert pytest.approx(calculate_total(prices), rel=1e-3) == 10.25 