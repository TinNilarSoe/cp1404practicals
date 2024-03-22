"""
Project
Estimate: 60 minutes
Actual:    minutes
"""

import datetime


class Project:
    """Represent a Project object"""

    def __init__(self, name="", start_date="", priority=0, estimate_cost=0.1, completion=0):
        """Initialize a Project instance.
        priority, completion = integer and estimate_cost = float
        import datetime to format the date"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate_cost = estimate_cost
        self.completion = completion

    def __str__(self):
        """Return a string for name, start_date, priority, estimate_cost and completion"""
        return (
            f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate_cost:.2f}, "
            f"completion: {self.completion}%")

    def is_complete(self):
        if self.completion == 100:
            return True

    def __lt__(self, other):
        """less than"""
        return self.priority < other.priority
