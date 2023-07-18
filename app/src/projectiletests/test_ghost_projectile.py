"""
This module tests the GhostProjectile class
"""
import pygame
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.projectile.ghost_projectile import GhostProjectile
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
    This function tests the should_destroy() method of the GhostProjectile class
    """
    screen: Surface = constants_fixture()
    ghost_projectile: GhostProjectile = GhostProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0, 0)

    assert ghost_projectile.pass_through_count == 0
    assert ghost_projectile.should_destroy() is True

    ghost_projectile.pass_through_count = 1
    assert ghost_projectile.should_destroy() is False

    ghost_projectile.pass_through_count = 10000
    assert ghost_projectile.should_destroy() is False

    ghost_projectile.pass_through_count = -1
    assert ghost_projectile.should_destroy() is True


def test_apply_special_ability():
    """
    This function tests the apply_special_ability() method of the GhostProjectile class
    """
    screen: Surface = constants_fixture()
    ghost_projectile: GhostProjectile = GhostProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0, 0)

    ghost_projectile.pass_through_count = 3

    enemy_hit: Enemy = Enemy(0, Position(0, 0), screen, DirectionVector(0, 0), 0)
    enemy1: Enemy = Enemy(0, Position(0, 5), screen, DirectionVector(0, 0), 0)
    enemy2: Enemy = Enemy(0, Position(-6, 0), screen, DirectionVector(0, 0), 0)

    enemies: list[Enemy] = [enemy_hit, enemy1, enemy2]

    for enemy in enemies:
        assert enemy not in ghost_projectile.ignored_enemies

    ghost_projectile.apply_special_ability(enemy_hit, enemies)

    assert ghost_projectile.pass_through_count == 2
    assert enemy_hit in ghost_projectile.ignored_enemies
    assert enemy1 not in ghost_projectile.ignored_enemies
    assert enemy2 not in ghost_projectile.ignored_enemies


def test_clone():
    """
    This function tests the clone() method of the GhostProjectile class
    """
    screen: Surface = constants_fixture()
    ghost_projectile: GhostProjectile = GhostProjectile(Position(1, 2), screen, DirectionVector(3, 4), 5, 6, 7, 8)
    clone: GhostProjectile = ghost_projectile.clone()

    assert clone.position.xCoord == ghost_projectile.position.xCoord
    assert clone.position.yCoord == ghost_projectile.position.yCoord
    assert clone.image == ghost_projectile.image
    assert clone.direction.xCoord == ghost_projectile.direction.xCoord
    assert clone.direction.yCoord == ghost_projectile.direction.yCoord
    assert clone.damage == ghost_projectile.damage
    assert clone.cooldown == ghost_projectile.cooldown
    assert clone.ignored_enemies == ghost_projectile.ignored_enemies
    assert clone.pass_through_count == ghost_projectile.pass_through_count
    assert clone.rect.x == ghost_projectile.rect.x
    assert clone.rect.y == ghost_projectile.rect.y
