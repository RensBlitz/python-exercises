# tests/test_vat_calculator.py

import pytest
from exercises.vat_calculator import add_vat

def test_basic():
    # 100 + 20% = 120
    assert pytest.approx(add_vat(100.0, 20.0), rel=1e-3) == 120.0 