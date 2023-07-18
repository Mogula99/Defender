"""
This module defines the Enemy class
"""
from pygame import Surface

from app.src.gameobject.movable_gameobject import MovableGameObject
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class Enemy(MovableGameObject):
    """
    This class is the representation of enemies in the game.
    """
    def __init__(self, health: int, position: Position, surface: Surface, direction: DirectionVector, speed: float):
        """
        Constructor of the Enemy class
        :param health: Health points of the enemy
        :param position: Position of the center of the enemy on the screen
        :param surface: Surface of the enemy
        :param direction: Direction in which the enemy should move
        :param speed: Speed of the movement of the enemy
        """
        MovableGameObject.__init__(self, position, surface, direction, speed)
        self.health: int = health

    def receive_damage(self, damage: int):
        """
        This method just subtracts a specified value from enemy's health points value
        :param damage: Value to subtract
        """
        self.health -= damage
