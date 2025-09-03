# tests/test_amusement_park_ticket.py

from exercises.amusement_park_ticket import compute_price


def test_child_free():
    assert compute_price(10, 25) == 0.0


def test_adult_pays():
    assert compute_price(30, 25) == 25.0


def test_senior_free():
    assert compute_price(70, 25) == 0.0 