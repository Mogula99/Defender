"""
This module defines the BasicProjectile class
"""
from __future__ import annotations

from pygame import Surface
from pygame.sprite import Group

from app.src.enemy.enemy import Enemy
from app.src.projectile.projectile import Projectile
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class BasicProjectile(Projectile):
    """
    This class represents a basic projectile, that will disappear after hitting the enemy and will not have any special effect.
    It will be the main projectile for black and grey tower.
    """
    def __init__(self, position: Position, surface: Surface, direction: DirectionVector, speed: float, damage: int, cooldown: float):
        Projectile.__init__(self, position, surface, direction, speed, damage, cooldown)

    def apply_special_ability(self, enemy_hit: Enemy, all_enemies: list[Enemy], visual_effects: Group):
        """
        This method applies a special ability of the projectile.
        :param enemy_hit: Enemy that has been hit by the projectile
        :param all_enemies: List of all enemies still alive in the current round
        :param visual_effects: A group of all visual effects currently active
        """
        # Not a great polymorphism, but it saved a lot of code repetition while handling collisions
        enemy_hit.receive_damage(self.damage)

    def should_destroy(self) -> bool:
        """
        This method decides if the projectile should be destroyed after a collision
        :return: True if the projectile should be destroyed after collision. False otherwise.
        """
        return True

    def clone(self) -> BasicProjectile:
        """
        Method that creates a new projectile with the same properties as the current one
        :return: A new projectile with the same properties as the current one
        """
        clone: BasicProjectile = BasicProjectile(self.position, self.image, self.direction, self.speed, self.damage, self.cooldown)
        return clone
