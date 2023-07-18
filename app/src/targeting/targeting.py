"""
This module defines the Targeting class
"""
from abc import ABC, abstractmethod

from app.src.enemy.enemy import Enemy
from app.utils.position import Position


class Targeting(ABC):
    """
    This is an abstract class representing different types of choosing enemies for towers.
    The towers will then shoot on chosen enemies.
    """
    @abstractmethod
    def select_target(self, tower_position: Position, enemies: list[Enemy]) -> Enemy:
        """
        Abstract method that chooses an enemy from a specified list
        :param tower_position: Position of the player's tower
        :param enemies: List of all enemies still alive in the current round
        :return: Enemy chosen from the list
        """
        return ...
