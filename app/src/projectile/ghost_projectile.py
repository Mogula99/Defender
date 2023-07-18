"""
This module defines GhostProjectile class
"""
from __future__ import annotations
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.projectile.projectile import Projectile
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class GhostProjectile(Projectile):
    """
    This class represent a projectile that will pass through enemies after damaging them so that it can damage the enemies behind them.
    It is the main projectile for blue tower.
    """
    def __init__(self, position: Position, surface: Surface, direction: DirectionVector, speed: float, damage: int, cooldown: float, pass_through_count: int):
        Projectile.__init__(self, position, surface, direction, speed, damage, cooldown)
        self.pass_through_count: int = pass_through_count
        self.ignored_enemies: list[Enemy] = []

    def apply_special_ability(self, enemy_hit: Enemy, all_enemies: list[Enemy]):
        """
        This method applies a special ability of the projectile.
        :param enemy_hit: Enemy that has been hit by the projectile
        :param all_enemies: List of all enemies still alive in the current round
        """
        if enemy_hit not in self.ignored_enemies:
            enemy_hit.receive_damage(self.damage)
            self.__pass_through(enemy_hit)

        # Just pass through enemies and damage other enemies behind them

    def __pass_through(self, ignored_enemy: Enemy):
        self.ignored_enemies.append(ignored_enemy)
        self.pass_through_count -= 1

    def should_destroy(self) -> bool:
        """
        This method decides if the projectile should be destroyed after a collision
        :return: True if the projectile should be destroyed after collision. False otherwise.
        """
        return self.pass_through_count <= 0

    def clone(self) -> GhostProjectile:
        """
        Method that creates a new projectile with the same properties as the current one
        :return: A new projectile with the same properties as the current one
        """
        return GhostProjectile(self.position, self.image, self.direction, self.speed, self.damage, self.cooldown, self.pass_through_count)
