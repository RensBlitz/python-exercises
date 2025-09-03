# exercises/simple_car.py

class SimpleCar:
    """
    A car class that stores basic information and can generate descriptions.

    This class should:
    - Store the car's make, model, and year
    - Generate a readable description of the car

    Think about: How do you format multiple pieces of information into a readable string?
    What makes a car description clear and informative?
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Create a new car.

        :param make: the manufacturer of the car
        :param model: the specific model name
        :param year: the manufacturing year

        TODO: Initialize the car attributes
        """
        raise NotImplementedError()

    def description(self) -> str:
        """
        Generate a description of the car.

        :return: a formatted string describing the car (e.g., "2020 Toyota Camry")

        TODO: Implement car description generation
        """
        raise NotImplementedError()
