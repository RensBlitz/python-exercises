# tests/test_hello_hero.py

import pytest
from exercises.hello_hero import greet

def test_basic():
    assert greet("Alex") == "Welcome, Alex!" 