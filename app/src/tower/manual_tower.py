"""
This module defines the ManualTower class
"""
from pygame import Surface

from app.src.projectile.projectile import Projectile
from app.src.tower.tower import Tower
from app.utils.position import Position


class ManualTower(Tower):
    """
    This class represent the tower that will be controlled manually by the player.
    """
    def __init__(self, position: Position, surface: Surface, projectile: Projectile):
        """
        Constructor of the ManualTower class
        :param position: Position of the center of the tower
        :param surface: Surface that the tower should have
        :param projectile: Projectile that the tower should fire at enemies
        """
        Tower.__init__(self, position, surface, projectile)
