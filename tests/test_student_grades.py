# tests/test_student_grades.py

import pytest
from exercises.student_grades import average_grades

def test_basic():
    records = {"Alice": [80.0, 90.0], "Bob": [70.0, 75.0]}
    expected = {"Alice": 85.0, "Bob": 72.5}
    assert average_grades(records) == expected 