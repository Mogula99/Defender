"""
This module contains only DirectionVector class
"""

from __future__ import annotations
from app.utils.position import Position


class DirectionVector:
    """
    DirectionVector class is a container for 2 coordinates. It represents a vector along which objects are moved
    DirectionVector can be converted to string, to tuple(get_tuple()) or created in a static method
    """
    def __init__(self, x: float, y: float):
        """
        Constructor of the DirectionVector class
        :param x: X coordinate of the vector
        :param y: Y coordinate of the vector
        """
        self.xCoord: float = x
        self.yCoord: float = y
        self.__normalize()

    def __str__(self):
        """
        This method returns the string representation of the DirectionVector class
        :return: String representation of the DirectionVector class
        """
        return "(" + str(self.xCoord) + "," + str(self.yCoord) + ")"

    def get_tuple(self) -> tuple[float, float]:
        """
        This method creates a tuple out of the current vector
        :return: Tuple that represents the current vector
        """
        return self.xCoord, self.yCoord

    def __normalize(self):
        """
        This method normalizes the vector so that it has only values between 0 and 1
        """
        magnitude: float = self.xCoord ** 2 + self.yCoord ** 2
        magnitude: float = magnitude ** 0.5
        if magnitude != 0:
            self.xCoord = self.xCoord / magnitude
            self.yCoord = self.yCoord / magnitude

    @staticmethod
    def create_vector(start: Position, end: Position) -> DirectionVector:
        """
        Static method that creates a vector from the start and end position
        :param start: Start position of the vector
        :param end: End position of the vector
        :return: vector representing the direction between start and end position
        """
        return DirectionVector(end.xCoord - start.xCoord, end.yCoord - start.yCoord)
