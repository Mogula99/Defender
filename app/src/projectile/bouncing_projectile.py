"""
This module defines BouncingProjectile class
"""
from __future__ import annotations

import random

from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.projectile.projectile import Projectile
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class BouncingProjectile(Projectile):
    """
    This class represents a projectile that will bounce in direction of another enemy after hitting an enemy.
    It will be the main projectile for green tower.
    """
    def __init__(self, position: Position, surface: Surface, direction: DirectionVector, speed: float, damage: int, cooldown: float, bounce_count: int):
        Projectile.__init__(self, position, surface, direction, speed, damage, cooldown)
        self.bounce_count: int = bounce_count
        self.ignore_enemy: Enemy = None

    def apply_special_ability(self, enemy_hit: Enemy, all_enemies: list[Enemy]):
        """
        This method applies a special ability of the projectile.
        :param enemy_hit: Enemy that has been hit by the projectile
        :param all_enemies: List of all enemies still alive in the current round
        """
        if enemy_hit != self.ignore_enemy:
            enemy_hit.receive_damage(self.damage)
            free_enemies: list[Enemy] = [enemy for enemy in all_enemies if enemy != enemy_hit]
            # Bounce in a direction of some random enemy
            if len(free_enemies) != 0:
                random_index: int = random.randint(0, len(free_enemies) - 1)
                new_enemy: Enemy = free_enemies[random_index]
                new_direction: DirectionVector = DirectionVector.create_vector(self.position, new_enemy.position)
                self.__bounce(new_direction, enemy_hit)

    def __bounce(self, new_direction: DirectionVector, ignored_enemy: Enemy):
        self.direction: DirectionVector = new_direction
        self.bounce_count -= 1
        self.ignore_enemy: Enemy = ignored_enemy

    def should_destroy(self) -> bool:
        """
        This method decides if the projectile should be destroyed after a collision
        :return: True if the projectile should be destroyed after collision. False otherwise.
        """
        return self.bounce_count <= 0

    def clone(self) -> BouncingProjectile:
        """
        Method that creates a new projectile with the same properties as the current one
        :return: A new projectile with the same properties as the current one
        """
        return BouncingProjectile(self.position, self.image, self.direction, self.speed, self.damage, self.cooldown, self.bounce_count)
