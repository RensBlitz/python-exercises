# tests/test_course.py

from exercises.course import Course


def test_enrol_drop_flow():
    c = Course("Java 101")
    assert c.enrol("Alice") is True
    assert c.enrol("Alice") is False  # already enrolled
    assert c.get_enrolment_count() == 1
    assert c.drop("Alice") is True
    assert c.get_enrolment_count() == 0
