"""
This module defines the ExplosiveProjectile class
"""
from __future__ import annotations
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.projectile.projectile import Projectile
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class ExplosiveProjectile(Projectile):
    """
    This class represent a projectile that will explode after colliding with an enemy.
    It will hurt another enemies in vicinity of the explosion.
    It is the main projectile for red tower.
    """
    def __init__(self, position: Position, surface: Surface, direction: DirectionVector, speed: float, damage: int, cooldown: float, explosion_radius: float):
        Projectile.__init__(self, position, surface, direction, speed, damage, cooldown)
        self.explosion_radius: float = explosion_radius

    def apply_special_ability(self, enemy_hit: Enemy, all_enemies: list[Enemy]):
        """
        This method applies a special ability of the projectile.
        :param enemy_hit: Enemy that has been hit by the projectile
        :param all_enemies: List of all enemies still alive in the current round
        """
        enemy_hit.receive_damage(self.damage)
        # Explode and damage all the enemies nearby
        for enemy in all_enemies:
            if self.position.count_distance(enemy.position) <= self.explosion_radius:
                enemy.receive_damage(self.damage)

    def should_destroy(self) -> bool:
        """
        This method decides if the projectile should be destroyed after a collision
        :return: True if the projectile should be destroyed after collision. False otherwise.
        """
        return True

    def clone(self) -> ExplosiveProjectile:
        """
        Method that creates a new projectile with the same properties as the current one
        :return: A new projectile with the same properties as the current one
        """
        return ExplosiveProjectile(self.position, self.image, self.direction, self.speed, self.damage, self.cooldown, self.explosion_radius)
