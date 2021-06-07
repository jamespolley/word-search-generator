"""
Functionality for randomly generating word positions, directions, and empty space characters.
"""

import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def origin(width, height):
    """Return a random point as a tuple in the form:
    ( x-direction, y-direction)"""
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return x, y

def direction():
    """Return a random direction as a tuple in the form:
    ( x-direction, y-direction)"""
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    if (x, y) != (0, 0):
        return x, y
    return direction()

def position(width, height, word_length):
    """Return a random pair of coordinates as tuples in the form:
    ( x_first_charater, y_first_character ),
    ( x_last_character, y_last_character )"""
    direction_x, direction_y = direction()
    head_x, head_y = origin(width, height)
    tail_x = head_x + (direction_x * word_length)
    if (tail_x < 0) or (tail_x > width - 1):
        return position(width, height, word_length)
    tail_y = head_y + (direction_y * word_length)
    if (tail_y < 0) or (tail_y > height - 1):
        return position(width, height, word_length)
    return head_x, head_y, direction_x, direction_y

def character():
    """Return a random alphabet character."""
    return random.choice(ALPHABET)