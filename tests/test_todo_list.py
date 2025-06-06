# tests/test_todo_list.py

import pytest
from exercises.todo_list import pending_tasks

def test_basic():
    tasks = ["Laundry", "Dishes", "Homework"]
    completed = [1]
    assert pending_tasks(tasks, completed) == ["Laundry", "Homework"] 