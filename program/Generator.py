from Table import Table


class Generator:
    """
    Main class. Drives word search generation process.
    """
    def __init__(self, width, height, words=[]):
        self.table = Table(width, height)
        self.words = words
    
    def __repr__(self):
        return self.table.__repr__()

# test
g = Generator(5, 5, ["lizard", "frog", "snake"])
print(g.table)
print(g)
print(g.words)