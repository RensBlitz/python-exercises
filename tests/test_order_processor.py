# tests/test_order_processor.py

import pytest
from exercises.order_processor import total_with_free_shipping_for_big_orders

def test_big_order():
    orders = [40.0, 60.0]
    assert pytest.approx(total_with_free_shipping_for_big_orders(orders), rel=1e-3) == 100.0

def test_small_order():
    orders = [10.0, 20.0]
    assert pytest.approx(total_with_free_shipping_for_big_orders(orders), rel=1e-3) == 0.0 