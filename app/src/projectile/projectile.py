"""
This module defines the Projectile class
"""
from abc import ABC, abstractmethod
from pygame import Surface
from pygame.sprite import Group

from app.src.enemy.enemy import Enemy
from app.src.gameobject.movable_gameobject import MovableGameObject
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class Projectile(MovableGameObject, ABC):
    """
    Projectile is an abstract class representing a projectile that will be launched in some direction
    """
    def __init__(self, position: Position, surface: Surface, direction: DirectionVector, speed: float, damage: int, cooldown: float):
        MovableGameObject.__init__(self, position, surface, direction, speed)
        self.damage: int = damage
        self.cooldown: float = cooldown

    @abstractmethod
    def apply_special_ability(self, enemy_hit: Enemy, all_enemies: list[Enemy], visual_effects: Group):
        """
        Abstract method applies a special ability of the projectile.
        :param enemy_hit: Enemy that has been hit by the projectile
        :param all_enemies: List of all enemies still alive in the current round
        :param visual_effects: A group of visual effects currently active
        """

    @abstractmethod
    def should_destroy(self) -> bool:
        """
        Abstract method that decides if the projectile should be destroyed after a collision
        :return: True if the projectile should be destroyed after collision. False otherwise.
        """

    @abstractmethod
    def clone(self):
        """
        Abstract method that creates a new projectile with the same properties as the current one
        :return: A new projectile with the same properties as the current one
        """
