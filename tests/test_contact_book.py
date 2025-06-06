# tests/test_contact_book.py

import pytest
from exercises.contact_book import to_map

def test_basic():
    contacts = [("Alice", "1234"), ("Bob", "5678")]
    expected = {"Alice": "1234", "Bob": "5678"}
    assert to_map(contacts) == expected 