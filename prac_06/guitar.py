"""
Guitar
Estimate: 40 minutes
Actual:  45  minutes
"""


class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0.1):
        """Initialize a Guitar instance.
        year: integer, cost: float"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string for guitar name, year and cost"""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self, current_year=2024):
        """Return the age of the guitar"""
        return current_year - self.year

    def is_vintage(self):
        """Return True if guitar is older than 50"""
        if self.get_age() < 50:
            return False
        else:
            return True
