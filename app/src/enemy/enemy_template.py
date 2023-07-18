"""
This module defines the EnemyTemplate class
"""
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class EnemyTemplate:
    """
    This class represents enemy template from which the Enemy objects are being created.
    """
    def __init__(self, health: int, surface: Surface, speed: float):
        """
        EnemyTemplate class constructor
        :param health: Health of the enemy template
        :param surface: Surface of the enemy template
        :param speed: Speed of the enemy template
        """
        self.health = health
        self.surface = surface
        self.speed = speed

    def create_enemy(self, position: Position, direction: DirectionVector) -> Enemy:
        """
        This method creates a new Enemy based on the template
        :param position: Position of the new enemy
        :param direction: Direction in which the enemy should move
        :return: Newly created enemy that is based on the current template
        """
        return Enemy(self.health, position, self.surface, direction, self.speed)
