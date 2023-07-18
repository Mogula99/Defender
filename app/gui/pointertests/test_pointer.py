"""
This module tests the Pointer class
"""

import math

import pygame
import pytest
from pygame import Rect, Surface

from app.gui.pointer.pointer import Pointer
from app.utils.constants import Constants


def constants_fixture():
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    return screen


@pytest.mark.parametrize(
    'left, top, width, height',
    [
        (50.50, 50.50, 50.50, 50.50),
        (-500.234, -5000.684, 1234.412, 9876.123456789),
        (0.001, 0.002, 0.003, 0.004),
        (100, 200, 300, 400)
    ])
def test_move_pointer(left: int, top: int, width: int, height: int):
    """
    This function tests the move_pointer() method of the Pointer class
    :param left: left X coordinate of the button's rectangle
    :param top: top Y coordinate of the button's rectangle
    :param width: width of the button's rectangle
    :param height: height of the button's rectangle
    """
    constants_fixture()
    button_rect: Rect = Rect(left, top, width, height)
    created_pointer: Pointer = Pointer.create_pointer(button_rect)

    assert created_pointer.image == Constants.POINTER_SURFACE
    assert created_pointer.offset == -50
    assert created_pointer.rect == button_rect

    created_pointer.move_pointer(button_rect)
    assert created_pointer.image == Constants.POINTER_SURFACE
    assert created_pointer.offset == -50
    assert created_pointer.rect.left == button_rect.left - 50
    assert created_pointer.rect.top == math.ceil(button_rect.top - button_rect.height / 2 + button_rect.height / 8)


@pytest.mark.parametrize(
    'left, top, width, height',
    [
        (50.50, 50.50, 50.50, 50.50),
        (-500.234, -5000.684, 1234.412, 9876.123456789),
        (0.001, 0.002, 0.003, 0.004),
        (100, 200, 300, 400)
    ])
def test_create_pointer(left: int, top: int, width: int, height: int):
    """
    This function tests the create_pointer() method of the Pointer class
    :param left: left X coordinate of the button's rectangle
    :param top: top Y coordinate of the button's rectangle
    :param width: width of the button's rectangle
    :param height: height of the button's rectangle
    """
    constants_fixture()
    button_rect: Rect = Rect(left, top, width, height)
    created_pointer: Pointer = Pointer.create_pointer(button_rect)

    assert created_pointer.image == Constants.POINTER_SURFACE
    assert created_pointer.offset == -50
    assert created_pointer.rect == button_rect
