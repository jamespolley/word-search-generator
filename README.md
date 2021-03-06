# word-search-generator
## Description
Randomly generates a word search given a list of words. Width and height can be adjusted. This project is separated into the following modules:
* __Generator__ - Main class. Drives the word search generation process.
* __Random__ - Functionality for randomly generating word positions, directions, and empty space characters.
* __Table__ - Handles construction of word search table and placement of characters.

## Usage
```python
# Import Generator.
from program.Generator import Generator

# Create word list.
words = ["lizard", "snake", "frog", "turtle", "reptile", "animal"]

# Create Generator with width, height, and word list.
gen = Generator(10, 10, words)

# Generate word search.
gen.generate()

# Print word search.
print(gen)
    # Prints:
        # O Z U A R Z X E X M
        # E Z E Y O K X L P Y
        # J D K X G R E I O D
        # U M A Z F L D T N P
        # E K N I A R T P M M
        # I J S M A C S E M Q
        # C W I Z P L A R G T
        # D N I U E L T R U T
        # A L F T T S X P Y A
    # Note: Is randomized. Above is only representative of output.
```