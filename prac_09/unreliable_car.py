from car import Car
from random import randint

RANDOM_LOW_NUMBER = 0
RANDOM_HIGH_NUMBER = 100


class UnreliableCar(Car):
    """Represent an unreliable version of car class."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car according to reliability."""
        random_number = randint(RANDOM_LOW_NUMBER, RANDOM_HIGH_NUMBER)

        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
