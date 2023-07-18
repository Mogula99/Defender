"""
This module defines the AutomaticTower class
"""
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.projectile.projectile import Projectile
from app.src.targeting.targeting import Targeting
from app.src.tower.tower import Tower
from app.utils.position import Position


class AutomaticTower(Tower):
    """
    AutomaticTower represent a tower that will shoot automatically.
    There are more types of towers that will have different types of projectiles.
    """
    def __init__(self, position: Position, surface: Surface, projectile: Projectile, targeting: Targeting):
        """
        AutomaticTower constructor
        :param position: Position of the center of the tower on the screen
        :param surface: Surface that the tower should have
        :param projectile: Projectile that the tower should fire
        :param targeting: Object responsible for picking targets for the tower
        """
        Tower.__init__(self, position, surface, projectile)
        self.targeting: Targeting = targeting

    def auto_fire(self, enemies: list[Enemy]) -> Projectile:
        """
        This method will fire a projectile on enemy chosen from the specified list
        :param enemies: List of all the enemies still alive in the current round
        :return: Projectile that has been fired
        """
        target: Enemy = self.targeting.select_target(self.position, enemies)
        if target is not None:
            return self.shoot(target.position)
        return None
