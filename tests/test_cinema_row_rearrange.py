# tests/test_cinema_row_rearrange.py

from exercises.cinema_row_rearrange import rearrange


def test_rearrange_basic():
    out = rearrange([20, 15, 30, 12])
    assert out == [15, 12, 20, 30]
