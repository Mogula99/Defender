"""
This module includes a Position class and some operations to do with the class.
"""

from __future__ import annotations

import math


class Position:
    """
    Position is a 2D position container.
    """
    def __init__(self, x: float, y: float):
        """
        Position constructor
        :param x: X coordinate of the position
        :param y: Y coordinate of the position
        """
        self.xCoord: float = x
        self.yCoord: float = y

    def __str__(self):
        """
        This method creates a string representation of the Position object
        :return: String representation of the Position object
        """
        return "(" + str(self.xCoord) + "," + str(self.yCoord) + ")"

    def __repr__(self):
        """
        This method returns a string representation of a position
        :return: String representation of the Position object
        """
        return self.__str__()

    def get_tuple(self) -> tuple[float, float]:
        """
        This method creates a tuple out of a position object
        :return: Tuple representing the current position object
        """
        return self.xCoord, self.yCoord

    def count_distance(self, other: Position) -> float:
        """
        This method counts the distance between this position and some other
        :param other: Position used for counting the distance
        :return: Distance between this position and some other position
        """
        return math.sqrt(((self.xCoord - other.xCoord) ** 2) + ((self.yCoord - other.yCoord) ** 2))
