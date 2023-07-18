"""
This module defines ClosestTargeting class
"""
from app.src.enemy.enemy import Enemy
from app.src.targeting.targeting import Targeting
from app.utils.position import Position


class ClosestTargeting(Targeting):
    """
    This class represents one type of picking targets for automatic towers.
    This type will target the enemies closest to the tower
    """
    def select_target(self, tower_position: Position, enemies: list[Enemy]) -> Enemy:
        """
        This method selects the nearest target from a specified list of enemies.
        :param tower_position: Position of the player's tower
        :param enemies: List of all the enemies still alive in the current round
        :return: Nearest enemy that has been selected
        """
        if len(enemies) == 0:
            return None

        min_distance: float = None
        closest_enemy: Enemy = enemies[0]

        # count distance for all the enemies and pick the nearest
        for enemy in enemies:
            distance: float = tower_position.count_distance(enemy.position)
            if min_distance is None or min_distance > distance:
                min_distance: float = distance
                closest_enemy: Enemy = enemy

        return closest_enemy
