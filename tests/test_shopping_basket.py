# tests/test_shopping_basket.py

from exercises.shopping_basket import join


def test_join_basic():
    items = ["milk", "eggs", "bread"]
    assert join(items) == "milk, eggs, bread" 