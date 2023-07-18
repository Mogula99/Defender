"""
This module tests the BouncingProjectile class
"""
import pygame
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.projectile.bouncing_projectile import BouncingProjectile
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
    This function tests the should_destroy() method of the BouncingProjectile class
    """
    screen: Surface = constants_fixture()
    bouncing_projectile: BouncingProjectile = BouncingProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0, 0)

    bouncing_projectile.bounce_count = 0
    assert bouncing_projectile.should_destroy() is True

    bouncing_projectile.bounce_count = -1
    assert bouncing_projectile.should_destroy() is True

    bouncing_projectile.bounce_count = -51265
    assert bouncing_projectile.should_destroy() is True

    bouncing_projectile.bounce_count = 1
    assert bouncing_projectile.should_destroy() is False

    bouncing_projectile.bounce_count = 123456
    assert bouncing_projectile.should_destroy() is False


def test_apply_special_ability():
    """
    This function tests the apply_special_ability() method of the BouncingProjectile class
    """
    screen: Surface = constants_fixture()
    bouncing_projectile: BouncingProjectile = BouncingProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0, 0)

    bouncing_projectile.bounce_count = 10

    enemy_hit: Enemy = Enemy(0, Position(0, 0), screen, DirectionVector(0, 0), 0)
    enemy1: Enemy = Enemy(0, Position(50, 50), screen, DirectionVector(0, 0), 0)
    enemy2: Enemy = Enemy(0, Position(-50, -50), screen, DirectionVector(0, 0), 0)

    enemies: list[Enemy] = [enemy_hit, enemy1, enemy2]

    assert bouncing_projectile.bounce_count == 10
    assert bouncing_projectile.direction.xCoord == 0
    assert bouncing_projectile.direction.yCoord == 0
    assert bouncing_projectile.ignore_enemy is None

    bouncing_projectile.apply_special_ability(enemy_hit, enemies)

    assert bouncing_projectile.bounce_count == 9
    assert bouncing_projectile.direction.xCoord != 0
    assert bouncing_projectile.direction.yCoord != 0
    assert bouncing_projectile.ignore_enemy == enemy_hit


def test_clone():
    """
    This function tests the clone() method of the BouncingProjectile class
    """
    screen: Surface = constants_fixture()
    bouncing_projectile: BouncingProjectile = BouncingProjectile(Position(1, 2), screen, DirectionVector(3, 4), 5, 6, 7, 8)
    clone: BouncingProjectile = bouncing_projectile.clone()

    assert clone.position.xCoord == bouncing_projectile.position.xCoord
    assert clone.position.yCoord == bouncing_projectile.position.yCoord
    assert clone.image == bouncing_projectile.image
    assert clone.direction.xCoord == bouncing_projectile.direction.xCoord
    assert clone.direction.yCoord == bouncing_projectile.direction.yCoord
    assert clone.damage == bouncing_projectile.damage
    assert clone.cooldown == bouncing_projectile.cooldown
    assert clone.bounce_count == bouncing_projectile.bounce_count
    assert clone.ignore_enemy == bouncing_projectile.ignore_enemy
    assert clone.rect.x == bouncing_projectile.rect.x
    assert clone.rect.y == bouncing_projectile.rect.y
