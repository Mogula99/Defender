"""
This module tests the BasicProjectile class
"""
import pygame
from pygame import Surface

from app.src.projectile.basic_projectile import BasicProjectile
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
    This function tests the should_destroy() method of the BasicProjectile class
    """
    screen: Surface = constants_fixture()
    basic_projectile: BasicProjectile = BasicProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0)
    assert basic_projectile.should_destroy() is True


def test_clone():
    """
    This function tests the clone() method of the BasicProjectile class
    """
    screen: Surface = constants_fixture()
    basic_projectile: BasicProjectile = BasicProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0)
    clone: BasicProjectile = basic_projectile.clone()

    assert clone.position.xCoord == basic_projectile.position.xCoord
    assert clone.position.yCoord == basic_projectile.position.yCoord
    assert clone.image == basic_projectile.image
    assert clone.direction.xCoord == basic_projectile.direction.xCoord
    assert clone.direction.yCoord == basic_projectile.direction.yCoord
    assert clone.damage == basic_projectile.damage
    assert clone.cooldown == basic_projectile.cooldown
    assert clone.rect.x == basic_projectile.rect.x
    assert clone.rect.y == basic_projectile.rect.y
