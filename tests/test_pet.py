# tests/test_pet.py

from exercises.pet import Pet


def test_speak_dog():
    assert Pet("Rex", "dog", 2).speak() == "Woof!"


def test_speak_unknown():
    assert Pet("Mystery", "dragon", 500).speak() == "..."
