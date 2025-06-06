# tests/test_library.py

import pytest
from exercises.library import is_available

def test_found():
    books = ["Kotlin in Action", "Effective Java"]
    assert is_available(books, "Kotlin in Action") is True

def test_not_found():
    books = ["Kotlin in Action", "Effective Java"]
    assert is_available(books, "Clean Code") is False 