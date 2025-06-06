# tests/test_tiny_encryption.py

import pytest
from exercises.tiny_encryption import encrypt

def test_basic():
    # "abc" shifted by 1 → "bcd"
    assert encrypt("abc", 1) == "bcd" 