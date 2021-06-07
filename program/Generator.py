from Table import Table

class Generator:
    """
    Main class. Drives the word search generation process.
    """
    def __init__(self, width, height, words=[], fail_by=100):
        self.table = Table(width, height)
        self.words = words
        self.fail_by = fail_by
    
    def generate(self):
        for word in self.words:
            self.table.place_word(word.upper(), self.fail_by)
        self.table.fill_empty_spaces()
    
    def __repr__(self):
        return self.table.__repr__()

# test
g = Generator(10, 10, ["lizard", "frog", "snake", "turtle"])
g.generate()
print(g.table)