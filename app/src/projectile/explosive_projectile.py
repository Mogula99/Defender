"""
This module defines the ExplosiveProjectile class
"""
from __future__ import annotations
from pygame import Surface
from pygame.sprite import Group

from app.src.enemy.enemy import Enemy
from app.src.projectile.projectile import Projectile
from app.src.visualeffect.visual_effect import VisualEffect
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position
from app.utils.constants import Constants


class ExplosiveProjectile(Projectile):
    """
    This class represent a projectile that will explode after colliding with an enemy.
    It will hurt another enemies in vicinity of the explosion.
    It is the main projectile for red tower.
    """
    def __init__(self, position: Position, surface: Surface, direction: DirectionVector, speed: float, damage: int, cooldown: float, explosion_radius: float):
        Projectile.__init__(self, position, surface, direction, speed, damage, cooldown)
        self.explosion_radius: float = explosion_radius

    def apply_special_ability(self, enemy_hit: Enemy, all_enemies: list[Enemy], visual_effects: Group):
        """
        This method applies a special ability of the projectile.
        :param enemy_hit: Enemy that has been hit by the projectile
        :param all_enemies: List of all enemies still alive in the current round
        :param visual_effects: A group of all visual effects currently active
        """
        enemy_hit.receive_damage(self.damage)
        explosion: VisualEffect = VisualEffect(self.position, self.__determine_size(), 1)
        visual_effects.add(explosion)
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

    def __determine_size(self) -> list[Surface]:
        if self.explosion_radius == Constants.RED_PROJECTILE_RADIUS:
            return Constants.SMALL_EXPLOSION_SURFACES
        if self.explosion_radius == Constants.RED_PROJECTILE_RADIUS + Constants.RED_PROJECTILE_RADIUS_UPGRADE:
            return Constants.MEDIUM_EXPLOSION_SURFACES
        return Constants.LARGE_EXPLOSION_SURFACES
