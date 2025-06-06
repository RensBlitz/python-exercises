# tests/test_fantasy_potion_mix.py

import pytest
from exercises.fantasy_potion_mix import ingredient_volumes

def test_volumes_750():
    assert ingredient_volumes(750) == [225, 375, 150] 