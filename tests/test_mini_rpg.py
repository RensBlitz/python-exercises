# tests/test_mini_rpg.py

from exercises.mini_rpg import Character, battle


def test_battle_simple():
    hero = Character("Hero", 10, 4)
    monster = Character("Goblin", 8, 3)
    winner = battle(hero, monster)
    assert winner == "Hero"
    assert hero.is_alive() is True
    assert monster.is_alive() is False