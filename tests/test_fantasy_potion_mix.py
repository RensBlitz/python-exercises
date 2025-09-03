# tests/test_fantasy_potion_mix.py

from exercises.fantasy_potion_mix import ingredient_volumes


def test_ingredient_volumes_750ml():
    v = ingredient_volumes(750)
    assert v == [225, 375, 150] 