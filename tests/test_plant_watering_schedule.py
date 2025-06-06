# tests/test_plant_watering_schedule.py

import pytest
from exercises.plant_watering_schedule import should_water

def test_monday_true():
    assert should_water("Monday") is True

def test_friday_false():
    assert should_water("Friday") is False 