# exercises/course.py

class Course:
    """
    A course management system that can enroll and drop students.

    This class should:
    - Store the course title
    - Maintain a list of enrolled students
    - Handle adding and removing students from the course

    Think about: How do you add items to a list? How do you remove items?
    What happens when you try to enroll a student who's already enrolled?
    """

    def __init__(self, title: str) -> None:
        """
        Create a new course.

        :param title: the name of the course

        TODO: Initialize the course
        """
        raise NotImplementedError()

    def enrol(self, student: str) -> bool:
        """
        Add a student to the course.

        :param student: the name of the student to enroll
        :return: True if enrollment was successful, False if student was already enrolled

        TODO: Implement student enrollment
        """
        raise NotImplementedError()

    def drop(self, student: str) -> bool:
        """
        Remove a student from the course.

        :param student: the name of the student to remove
        :return: True if removal was successful, False if student was not enrolled

        TODO: Implement student removal
        """
        raise NotImplementedError()

    def get_enrolment_count(self) -> int:
        return len(self.students)
