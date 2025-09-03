# exercises/mini_rpg.py

class Character:
    """
    A character in the RPG battle system.

    Each character has:
    - A name (cannot be changed after creation)
    - Health points (can change during battle)
    - Attack power (cannot be changed after creation)
    """

    def __init__(self, name: str, health: int, attack: int) -> None:
        """
        Create a new character with the specified attributes.

        :param name: the character's name
        :param health: the starting health points
        :param attack: the attack power

        TODO: Initialize character attributes
        """
        raise NotImplementedError()

    def is_alive(self) -> bool:
        """Return True if health > 0, False otherwise."""
        return self.health > 0

    def attack(self, target: "Character") -> None:
        """
        Attack another character, reducing their health by this character's attack power.

        :param target: the character to attack

        TODO: Implement attack logic
        """
        raise NotImplementedError()

    def get_health(self) -> int:
        return self.health

    def get_name(self) -> str:
        return self.name


def battle(a: Character, b: Character) -> str:
    """
    Conduct a battle between two characters until one is defeated.

    This function should:
    - Have characters take turns attacking each other
    - Continue until one character's health drops to 0 or below
    - Return the name of the winning character

    Think about: How do you implement turn-based combat? How do you determine when the battle ends?
    What happens if both characters have the same attack power?

    TODO: Implement the battle system
    """
    raise NotImplementedError()