"""
In this module there is only a Difficulty enum.
"""

from enum import IntEnum


class Difficulty(IntEnum):
    """
    Difficulty represents the difficulty of the game. There are 3 option - EASY(1), MEDIUM(2) and HARD(3)
    """
    EASY = 1
    MEDIUM = 2
    HARD = 3
