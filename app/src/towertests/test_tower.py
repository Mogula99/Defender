"""
This module tests the ManualTower class
"""
import pygame
from pygame import Surface

from app.src.projectile.basic_projectile import BasicProjectile
from app.src.projectile.projectile import Projectile
from app.src.tower.manual_tower import ManualTower
from app.src.tower.tower import Tower
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


def test_shoot():
    """
    This function tests the shoot() method of the ManualTower class
    """
    screen: Surface = constants_fixture()
    tower: Tower = ManualTower(Position(100, 0), screen, BasicProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0))

    assert tower.cooldown == 0

    fired_projectile: Projectile = tower.shoot(Position(100, 100))
    assert tower.cooldown == fired_projectile.cooldown
    assert isinstance(fired_projectile, BasicProjectile)
    assert fired_projectile.position.xCoord == tower.position.xCoord
    assert fired_projectile.position.yCoord == tower.position.yCoord
    assert fired_projectile.direction.xCoord == 0
    assert fired_projectile.direction.yCoord == 1
    assert fired_projectile.cooldown == tower.projectile.cooldown
    assert fired_projectile.damage == tower.projectile.damage
    assert fired_projectile.image == tower.projectile.image


def test_reduce_cooldown():
    """
    This function tests the reduce_cooldown() method of the ManualTower class
    """
    screen: Surface = constants_fixture()
    tower: Tower = ManualTower(Position(100, 0), screen, BasicProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0))

    assert tower.cooldown == 0
    tower.cooldown = 500

    tower.reduce_cooldown(50)
    assert tower.cooldown == 450
