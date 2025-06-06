# tests/test_student_records.py

import pytest
from exercises.student_records import top_students

def test_basic():
    recs = {"Alice": "A", "Bob": "B", "Carol": "A"}
    assert top_students(recs) == ["Alice", "Carol"] 