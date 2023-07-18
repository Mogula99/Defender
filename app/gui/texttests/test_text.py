"""
This module tests the Text class
"""
import pygame
import pytest
from pygame import Surface
from pygame.color import Color

from app.gui.text.text import Text
from app.utils.constants import Constants
from app.utils.position import Position


def constants_fixture():
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()


@pytest.mark.parametrize(
    'text_string, position, text_color, background_color',
    [
        ("HELLO", Position(50, 50), Color("Pink"), Color("Aqua")),
        ("HELLO WORLD", Position(1234, 5678), Color("CYAN"), Color("red")),
        ("THIS IS KINDA LONG TEXT EVEN FOR A TEXT CLASS, BUT TO MAKE IT EVEN A BIT LONGER IM ADDING ANOTHER TEXT", Position(-5000, 0), Color("gREEN"), Color("purple")),
        ("", Position(0, 0), Color("Pink"), Color("Aqua"))
    ])
def test_create_text(text_string: str, position: Position, text_color: pygame.color.Color,
                     background_color: pygame.color.Color):
    """
    This function tests the create_text() method of the Text class.
    :param text_string: String with the text of the Text object
    :param position: Position of the text object
    :param text_color: Color of the text
    :param background_color: Background color of the text object
    """
    constants_fixture()
    text: Text = Text.create_text(text_string, position, text_color, background_color)

    assert text.text_color == text_color
    assert text.background_color == background_color
    assert text.image != Text.create_text(text_string, position)
    assert text.image != Text.create_title(text_string, position, text_color, background_color)
    assert text.rect.centerx == position.xCoord
    assert text.rect.centery == position.yCoord


@pytest.mark.parametrize(
    'text_string, position, text_color, background_color',
    [
        ("HELLO", Position(50, 50), Color("Pink"), Color("Aqua")),
        ("TITLE NAME", Position(1234, 5678), Color("CYAN"), Color("red")),
        ("THIS IS KINDA LONG TEXT EVEN FOR A TEXT CLASS, BUT TO MAKE IT EVEN A BIT LONGER IM ADDING ANOTHER TEXT BEHIND IT", Position(-5000, 0), Color("gREEN"), Color("purple")),
        ("", Position(0, 0), Color("Pink"), Color("Aqua"))
    ])
def test_create_title(text_string: str, position: Position, text_color: pygame.color.Color,
                      background_color: pygame.color.Color):
    """
    This function tests the create_title() method of the Text class
    :param text_string: String with the text of the Text object
    :param position: Position of the Text object
    :param text_color: Color of the Text object
    :param background_color: Background of the Text object
    """
    constants_fixture()
    text: Text = Text.create_title(text_string, position, text_color, background_color)

    assert text.text_color == text_color
    assert text.background_color == background_color
    assert text.image != Text.create_text(text_string, position, text_color, background_color)
    assert text.image != Text.create_title(text_string, position)
    assert text.rect.centerx == position.xCoord
    assert text.rect.centery == position.yCoord


@pytest.mark.parametrize(
    'text_string, position, text_color, background_color, new_text',
    [
        ("HELLO", Position(50, 50), Color("Pink"), Color("Aqua"), "WORLD"),
        ("TITLE NAME", Position(1234, 5678), Color("CYAN"), Color("red"), "SOME NEW TEXT"),
        ("THIS IS KINDA LONG TEXT EVEN FOR A TEXT CLASS, BUT TO MAKE IT EVEN A BIT LONGER IM ADDING ANOTHER TEXT BEHIND IT",
         Position(-5000, 0), Color("gREEN"), Color("purple"), ""),
        ("", Position(0, 0), Color("Pink"), Color("Aqua"), "AND THIS NEW TEXT IS NOT SHORTER THAN THE PREVIOUS LONG TEXT, IT IS DEFINITELY LONGER THAN THE PREVIOUS ONE")
    ])
def test_refresh_text(text_string: str, position: Position, text_color: pygame.color.Color,
                      background_color: pygame.color.Color, new_text: str):
    """
    This function tests the refresh_text() method of the Text class
    :param text_string: String with a text of the Text object
    :param position: Position of the Text object
    :param text_color: Color of the Text
    :param background_color: Background color of the Text object
    :param new_text: New text that should appear in the Text object
    """
    constants_fixture()
    title: Text = Text.create_title(text_string, position, text_color, background_color)
    text: Text = Text.create_text(text_string, position, text_color, background_color)

    assert title.text_color == text_color
    assert title.background_color == background_color
    assert title.image != Text.create_text(text_string, position, text_color, background_color)
    assert title.image != Text.create_title(text_string, position)
    assert title.rect.centerx == position.xCoord
    assert title.rect.centery == position.yCoord

    assert text.text_color == text_color
    assert text.background_color == background_color
    assert text.image != Text.create_text(text_string, position, text_color, background_color)
    assert text.image != Text.create_title(text_string, position)
    assert text.rect.centerx == position.xCoord
    assert text.rect.centery == position.yCoord

    previous_text_image: Surface = text.image
    previous_title_image: Surface = title.image

    text.refresh_text(new_text)
    title.refresh_text(new_text)

    assert title.text_color == text_color
    assert title.background_color == background_color
    assert title.image != previous_title_image
    assert title.rect.centerx == position.xCoord
    assert title.rect.centery == position.yCoord

    assert text.text_color == text_color
    assert text.background_color == background_color
    assert text.image != previous_text_image
    assert text.rect.centerx == position.xCoord
    assert text.rect.centery == position.yCoord
