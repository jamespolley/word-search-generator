import Random as rand

class Table(list):
    """
    Handles construction of word search table and access of elements.
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
    
    def place_word(self, word, fail_by=100):
        for attempt in range(fail_by):
            x, y, direction_x, direction_y = rand.position(
                self.width, self.height, len(word))
            success = self.attempt_to_place_word(
                word, 0, x, y, direction_x, direction_y)
            if success:
                return True
        return False

    def attempt_to_place_word(self, word, index, x, y, direction_x, direction_y):
        if index >= len(word):
            return True
        value_in_table = self[y][x]
        if (value_in_table == None) or (value_in_table == word[index]):
            new_x = x + direction_x
            new_y = y + direction_y
            index += 1
            if self.attempt_to_place_word(word, index, new_x, new_y, direction_x, direction_y):
                self[y][x] = word[index-1]
                return True
        else:
            return False
    
    def fill_empty_spaces(self):
        for y in range(self.height):
            for x in range(self.width):
                value = self[y][x]
                if value == None:
                    self[y][x] = rand.character()
    
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