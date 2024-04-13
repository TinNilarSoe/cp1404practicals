class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician list"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to band's collection"""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musicians playing instruments"""
        return "\n".join(musician.play() for musician in self.musicians)
