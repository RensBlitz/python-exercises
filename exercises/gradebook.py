# exercises/gradebook.py

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    grade: float

def top_student(students: list[Student]) -> str:
    """
    Return the name of the student with the highest grade.
    """
    raise NotImplementedError() 