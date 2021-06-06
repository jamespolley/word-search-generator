class Table(list):
    """
    Handles construction of word search table and access of elements
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self = self.construct_table()
        
    def construct_table(self):
        for h in range(self.height):
            row = []
            for w in range(self.width):
                row.append(None)
            self.append(row)
    
    def __repr__(self):
        repr = ""
        for h in self:
            for w in h:
                if w:
                    repr += str(w) + " "
                else:
                    repr += "- "
            repr += "\n"
        return repr

# test
t = Table(10, 10)
print(t)