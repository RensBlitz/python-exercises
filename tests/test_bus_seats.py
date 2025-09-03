# tests/test_bus_seats.py

from exercises.bus_seats import first_free


def test_first_free_basic():
    seats = [False] * 40  # Create a list of 40 False values (all available)
    seats[0] = True  # occupied
    seats[1] = True  # occupied
    assert first_free(seats) == 2
