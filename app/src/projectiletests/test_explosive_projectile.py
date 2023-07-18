"""
This module tests the ExplosiveProjectile class
"""
import pygame
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.projectile.explosive_projectile import ExplosiveProjectile
from app.utils.constants import Constants
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


def constants_fixture() -> Surface:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    return screen


def test_should_destroy():
    """
    This function tests the should_destroy() method of the ExplosiveProjectile class
    """
    screen: Surface = constants_fixture()
    explosive_projectile: ExplosiveProjectile = ExplosiveProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0, 0)
    assert explosive_projectile.should_destroy() is True


def test_apply_special_ability():
    """
    This function tests the apply_special_ability() method of the ExplosiveProjectile class
    """
    screen: Surface = constants_fixture()
    explosive_projectile: ExplosiveProjectile = ExplosiveProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 42, 0, 0)

    explosive_projectile.explosion_radius = 5

    enemy_hit: Enemy = Enemy(0, Position(0, 0), screen, DirectionVector(0, 0), 0)
    enemy1: Enemy = Enemy(0, Position(0, 5), screen, DirectionVector(0, 0), 0)
    enemy2: Enemy = Enemy(0, Position(-6, 0), screen, DirectionVector(0, 0), 0)

    enemies: list[Enemy] = [enemy_hit, enemy1, enemy2]

    assert enemy_hit.health == 0
    assert enemy1.health == 0
    assert enemy2.health == 0

    explosive_projectile.apply_special_ability(enemy_hit, enemies)

    assert enemy_hit.health == -84
    assert enemy1.health == -42
    assert enemy2.health == 0


def test_clone():
    """
    This function tests the clone() method of the ExplosiveProjectile class
    """
    screen: Surface = constants_fixture()
    explosive_projectile: ExplosiveProjectile = ExplosiveProjectile(Position(1, 2), screen, DirectionVector(3, 4), 5, 6, 7, 8)
    clone: ExplosiveProjectile = explosive_projectile.clone()

    assert clone.position.xCoord == explosive_projectile.position.xCoord
    assert clone.position.yCoord == explosive_projectile.position.yCoord
    assert clone.image == explosive_projectile.image
    assert clone.direction.xCoord == explosive_projectile.direction.xCoord
    assert clone.direction.yCoord == explosive_projectile.direction.yCoord
    assert clone.damage == explosive_projectile.damage
    assert clone.cooldown == explosive_projectile.cooldown
    assert clone.explosion_radius == explosive_projectile.explosion_radius
    assert clone.rect.x == explosive_projectile.rect.x
    assert clone.rect.y == explosive_projectile.rect.y
