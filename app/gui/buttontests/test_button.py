"""
This module tests the Button class
"""

import pygame
import pytest
from pygame import Surface

from app.gui.button.button import Button
from app.utils.position import Position
from app.utils.constants import Constants


def constants_fixture():
    """
    This function makes all the necessary preparations co that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()


@pytest.mark.parametrize(
    'button_text, button_position',
    [
        ("HELLO", Position(50, 50)),
        ("TEST", Position(-600, -600)),
        ("WORLD", Position(1000, 2000)),
        ("THIS IS A LONG TEXT FOR A BUTTON", Position(0, 0))
    ])
def test_change_color(button_text: str, button_position: Position):
    """
    This function tests the change_color() method of the button class
    :param button_text: Text of the button
    :param button_position: Position of the button
    """
    constants_fixture()
    created_button = Button.create_menu_button(button_text, button_position)
    old_surface: Surface = created_button.image
    assert created_button.button_text == button_text
    assert created_button.rect.centerx == button_position.xCoord
    assert created_button.rect.centery == button_position.yCoord
    assert created_button.image.get_rect(center=button_position.get_tuple()).centerx == button_position.xCoord
    assert created_button.image.get_rect(center=button_position.get_tuple()).centery == button_position.yCoord

    created_button.change_text_color(pygame.color.Color("Pink"))

    assert created_button.button_text == button_text
    assert created_button.rect.centerx == button_position.xCoord
    assert created_button.rect.centery == button_position.yCoord
    assert created_button.image.get_rect(center=button_position.get_tuple()).centerx == button_position.xCoord
    assert created_button.image.get_rect(center=button_position.get_tuple()).centery == button_position.yCoord
    assert old_surface != created_button.image


@pytest.mark.parametrize(
    'button_text, button_position',
    [
        ("HELLO", Position(50, 50)),
        ("TEST", Position(-600, -600)),
        ("WORLD", Position(1000, 2000)),
        ("THIS IS A LONG TEXT FOR A BUTTON", Position(0, 0))
    ])
def test_create_menu_button(button_text: str, button_position: Position):
    """
    This function tests the create_menu_button() function of the Button class
    :param button_text: Text of the button
    :param button_position: Position of the button
    """
    constants_fixture()
    created_button: Button = Button.create_menu_button(button_text, button_position)

    assert created_button.button_text == button_text
    assert created_button.rect.centerx == button_position.xCoord
    assert created_button.rect.centery == button_position.yCoord
    assert created_button.image.get_rect(center=button_position.get_tuple()).centerx == button_position.xCoord
    assert created_button.image.get_rect(center=button_position.get_tuple()).centery == button_position.yCoord
