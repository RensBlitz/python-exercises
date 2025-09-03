# tests/test_todo_item.py

from datetime import date, timedelta
from exercises.todo_item import TodoItem


def test_overdue_and_toggle():
    yesterday = date.today() - timedelta(days=1)
    t = TodoItem("Finish report", yesterday)
    assert t.is_overdue(date.today()) is True
    t.toggle_completed()
    assert t.is_completed() is True
