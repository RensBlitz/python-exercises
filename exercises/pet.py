# exercises/pet.py

class Pet:
    """
    A pet class that can make different sounds based on their type.

    This class should:
    - Store the pet's name, type, and age
    - Return appropriate sounds based on the pet type
    - Handle different pet types efficiently

    Think about: How do you handle different types of pets? What sound should each type make?
    How do you handle pets that aren't dogs or cats?
    """

    def __init__(self, name: str, type: str, age: int) -> None:
        """
        Create a new pet.

        :param name: the pet's name
        :param type: the type of pet (e.g., "dog", "cat")
        :param age: the pet's age in years

        TODO: Initialize the pet
        """
        raise NotImplementedError()

    def speak(self) -> str:
        """
        Make the pet speak based on its type.

        :return: the sound the pet makes:
                - Dogs say "Woof!"
                - Cats say "Meow!"
                - Other pets say "..."
        """
        # type→sound mapping (dog→"Woof!", cat→"Meow!", default→"...").
        # TODO: Implement type-based sound generation
        raise NotImplementedError()
