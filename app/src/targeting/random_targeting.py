"""
This module defines the RandomTargeting class
"""
import random

from app.src.enemy.enemy import Enemy
from app.src.targeting.targeting import Targeting
from app.utils.position import Position


class RandomTargeting(Targeting):
    """
    This class represents one type of picking targets for automatic towers.
    This type will target random enemy that is still alive.
    """
    def select_target(self, tower_position: Position, enemies: list[Enemy]) -> Enemy:
        """
        This method randomly selects an enemy from a list of enemies
        :param tower_position: Position of the player's tower
        :param enemies: List of all enemies still alive in the current round
        :return: Enemy from the specified list that has been chosen randomly
        """
        if len(enemies) <= 0:
            return None
        random_index: int = random.randint(0, len(enemies)-1)
        return enemies[random_index]
