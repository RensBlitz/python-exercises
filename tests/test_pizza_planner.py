# tests/test_pizza_planner.py

import pytest
from exercises.pizza_planner import pizzas_needed

def test_basic():
    # 10 guests, 8 slices/pizza → need 2 pizzas
    assert pizzas_needed(10, 8) == 2 