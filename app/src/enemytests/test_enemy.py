"""
This module tests the Enemy class
"""
import pygame
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.utils.constants import Constants
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


def constants_fixture() -> Enemy:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    enemy: Enemy = Enemy(10, Position(0, 0), [screen], DirectionVector(0, 0), 1)
    return enemy


def test_receive_damage():
    """
    This function tests the receive_damage() method of the Enemy class
    """
    enemy: Enemy = constants_fixture()

    assert enemy.health == 10
    enemy.receive_damage(5)
    assert enemy.health == 5
    enemy.receive_damage(10000)
    assert enemy.health == -9995
