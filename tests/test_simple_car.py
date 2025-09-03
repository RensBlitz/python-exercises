# tests/test_simple_car.py

from exercises.simple_car import SimpleCar


def test_description_basic():
    c = SimpleCar("Tesla", "Model 3", 2024)
    assert c.description() == "2024 Tesla Model 3"
