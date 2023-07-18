"""
This module defines Text GUI element used for any kind of text rendered on screen.
"""

from __future__ import annotations

from pygame import Surface, Rect
from pygame.color import Color
from pygame.sprite import Sprite

from app.utils.constants import Constants
from app.utils.position import Position


class Text(Sprite):
    """
    This class represent Text GUI element used for rendering text on game screen
    """
    def __init__(self, surface: Surface, rect: Rect, text_color: Color, background_color: Color):
        """
        Constructor of the Text class
        :param surface: Surface of the text
        :param rect: Rectangle of the text
        :param text_color: Color of the text
        :param background_color: Background color of the text
        """
        Sprite.__init__(self)
        self.image: Surface = surface
        self.rect: Rect = rect
        self.text_color = text_color
        self.background_color = background_color

    def refresh_text(self, new_text: str) -> None:
        """
        This method creates new surface for the text instance. The surface contains the text passed as argument
        :param new_text: New text of the Text class instance
        """
        self.image: Surface = Constants.TEXT_FONT.render(new_text, False, self.text_color, self.background_color)

    @staticmethod
    def create_text(text_string: str, position: Position, text_color: Color = Constants.TEXT_COLOR, background_color: Color = None) -> Text:
        """
        This is static method responsible for creating Text class with regular text.
        :param text_string: Text that should be visible on the screen
        :param position: Position of the center of the text object on the screen
        :param text_color: Color of the text
        :param background_color: Color of the text background
        :return: Text object with specified properties
        """
        text_surface: Surface = Constants.TEXT_FONT.render(text_string, True, text_color, background_color)
        text_rect: Rect = text_surface.get_rect(center=position.get_tuple())
        return Text(text_surface, text_rect, text_color, background_color)

    @staticmethod
    def create_title(text_string: str, position: Position = Constants.MAIN_TITLE_POSITION, text_color: Color = Constants.TITLE_COLOR, background_color: Color = Constants.TEXT_BACKGROUND_COLOR) -> Text:
        """
        This is static method responsible for creating Text class with text used for titles and important information.
        :param text_string: Text that should be visible on the screen
        :param position: Position of the center of the text object on the screen
        :param text_color: Color of the text
        :param background_color: Color of the text background
        :return: Text object with specified properties
        """
        title_surface: Surface = Constants.TITLE_FONT.render(text_string, False, text_color, background_color)
        title_rect: Rect = title_surface.get_rect(center=position.get_tuple())
        return Text(title_surface, title_rect, text_color, background_color)
