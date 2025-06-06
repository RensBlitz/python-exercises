# tests/test_gradebook.py

import pytest
from exercises.gradebook import Student, top_student

def test_basic():
    students = [
        Student("Alice", 85.0),
        Student("Bob", 92.5),
        Student("Carol", 90.0)
    ]
    assert top_student(students) == "Bob" 