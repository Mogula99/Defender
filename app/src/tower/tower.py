"""
This module defines the Tower class
"""

from pygame import Surface

from app.src.gameobject.gameobject import GameObject
from app.src.projectile.projectile import Projectile
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class Tower(GameObject):
    """
    This class represent a tower. It is an object that will shoot projectiles at selected positions.
    """
    def __init__(self, position: Position, surface: Surface, projectile: Projectile):
        """
        Tower class constructor
        :param position: Position of the center of the tower
        :param surface: Surface of the tower
        :param projectile: Projectile that the tower should fire on its enemies
        """
        GameObject.__init__(self, position, surface)
        self.projectile: Projectile = projectile
        self.cooldown: float = 0

    def shoot(self, target_position: Position) -> Projectile:
        """
        This method shoots tower's projectile on specified position
        :param target_position: Position on which the tower should fire
        :return: Fired projectile
        """
        projectile_direction: DirectionVector = DirectionVector.create_vector(self.position, target_position)
        projectile_position: Position = Position(self.position.xCoord, self.position.yCoord)
        new_projectile: Projectile = self.projectile.clone()
        new_projectile.direction = projectile_direction
        new_projectile.position = projectile_position

        self.cooldown += new_projectile.cooldown
        return new_projectile

    def reduce_cooldown(self, reduce_amount: float):
        """
        This method reduces tower's cooldown by a specified amount
        :param reduce_amount: Amount to subtract from the current tower's cooldown
        """
        self.cooldown -= reduce_amount
