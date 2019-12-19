class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """
        Take values to construct a ProgrammingLanguage like name, typing, reflection, year
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string that represents a set of information related to ProgrammingLanguage"""
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Check to see if typing is Dynamic"""
        return self.typing == "Dynamic"
