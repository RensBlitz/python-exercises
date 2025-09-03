# exercises/todo_item.py

from datetime import date


class TodoItem:
    """
    A todo item that tracks completion status and due dates.

    This class should:
    - Store the item's title and due date
    - Track whether the item is completed
    - Determine if the item is overdue

    Think about: How do you compare dates? What makes an item overdue?
    How do you toggle between two states?
    """

    def __init__(self, title: str, due_date: date) -> None:
        """
        Create a new todo item.

        :param title: the description of the task
        :param due_date: when the task should be completed

        TODO: Initialize the todo item
        """
        raise NotImplementedError()

    def toggle_completed(self) -> None:
        """
        Toggle the completion status of this item.
        If completed, mark as incomplete; if incomplete, mark as completed.

        TODO: Implement completion status toggle
        """
        raise NotImplementedError()

    def is_completed(self) -> bool:
        return self.completed

    def is_overdue(self, now: date) -> bool:
        """
        Check if this item is overdue.

        :param now: the current date to compare against
        :return: True if the due date has passed and the item is not completed

        TODO: Implement overdue checking
        """
        raise NotImplementedError()
