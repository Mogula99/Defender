"""
This module tests the MovableGameObject class
"""
import pygame
from pygame import Surface

from app.src.gameobject.movable_gameobject import MovableGameObject
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


def test_update():
    """
    This function tests the test_update() method of the MovableGameObject class
    """
    screen: Surface = constants_fixture()
    movable: MovableGameObject = MovableGameObject(Position(0, 0), screen, DirectionVector(1, 0), 1)

    assert movable.rect.left == -400
    assert movable.rect.top == -300

    movable.update()

    assert movable.position.xCoord == 1
    assert movable.position.yCoord == 0

    assert movable.rect.left == -399
    assert movable.rect.top == -300
