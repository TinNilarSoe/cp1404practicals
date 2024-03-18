"""
Programming Language
Estimate: 30 minutes
Actual:  35  minutes
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object"""

    def __init__(self, field="", typing="", reflection="", year=0):
        """Initialize a ProgrammingLanguage instance.
        year: integer"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string for a language, typing, reflection, and year"""
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return a boolean for typing"""
        if self.typing == "Dynamic":
            return True
