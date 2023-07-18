"""
This module defines the Button GUI element that is used in menu-like windows.
"""
from __future__ import annotations

from pygame import Surface, Rect, Color
from pygame.sprite import Sprite

from app.utils.constants import Constants
from app.utils.position import Position


class Button(Sprite):
    """
    Button represents a GUI element that is used for letting player choose what he wants in menu-like windows.
    """
    def __init__(self, position: Position, surface: Surface, button_text: str):
        """
        Button constructor
        :param position: Position of the center of the button on the screen
        :param surface: Surface of the button
        :param button_text: Text of the button
        """
        Sprite.__init__(self)
        self.image: Surface = surface
        self.rect: Rect = self.image.get_rect(center=position.get_tuple())
        self.button_text: str = button_text

    def change_text_color(self, new_color: Color) -> None:
        """
        This method changes the color of the text of the button
        :param new_color: New color to change the text color to
        """
        self.image: Surface = Constants.TEXT_FONT.render(self.button_text, False, new_color, Constants.TEXT_BACKGROUND_COLOR)

    @staticmethod
    def create_menu_button(button_text: str, button_position: Position) -> Button:
        """
        This is a static method that is responsible for creating a button
        :param button_text: Text of the button
        :param button_position: Position of the center of the button on the screen
        :return: Button with specified text and position
        """
        button_surface: Surface = Constants.TEXT_FONT.render(button_text, False, Constants.TEXT_COLOR, Constants.TEXT_BACKGROUND_COLOR)
        button: Button = Button(button_position, button_surface, button_text)
        return button
