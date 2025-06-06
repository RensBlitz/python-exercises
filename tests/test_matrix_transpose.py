# tests/test_matrix_transpose.py

import pytest
from exercises.matrix_transpose import transpose

def test_basic():
    mat = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    assert transpose(mat) == expected 