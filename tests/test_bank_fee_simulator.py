# tests/test_bank_fee_simulator.py

import pytest
from exercises.bank_fee_simulator import simulate_transactions

def test_basic():
    # initial=100, transactions=12:
    # cost = 0.50 × 12 + 0.30 × (12 - 10) = 6 + 0.60 = 6.60 → final = 93.4
    assert pytest.approx(simulate_transactions(100.0, 12), rel=1e-3) == 93.4 