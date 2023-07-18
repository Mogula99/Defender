"""
This module defines the Pointer class that is used in menus to point to chosen buttons
"""
from __future__ import annotations

from pygame import Surface, Rect
from pygame.sprite import Sprite

from app.utils.constants import Constants


class Pointer(Sprite):
    """
    Pointer class represents a GUI element that points to buttons in menu-like windows
    """
    def __init__(self, surface: Surface, rect: Rect, offset: int):
        """
        Constructor of the pointer class
        :param surface: Surface of the pointer
        :param rect: Rectangle of the pointer
        :param offset: offset from the button on the X-axis
        """
        Sprite.__init__(self)
        self.image = surface
        self.rect = rect
        self.offset = offset

    def move_pointer(self, button_rect: Rect) -> None:
        """
        This method moves the pointer to point to another button
        :param button_rect: Rectangle of the button the pointer should point to
        """
        self.rect: Rect = button_rect.copy()
        self.rect.move_ip(self.offset, -button_rect.height/2 + button_rect.height/8)

    @staticmethod
    def create_pointer(button_rect: Rect) -> Pointer:
        """
        This is static method responsible for creating a pointer
        :param button_rect: Rectangle of the button the pointer should point to
        :return: Pointer class instance
        """
        pointer_offset: int = -50
        pointer_surface: Surface = Constants.POINTER_SURFACE
        pointer_rect: Rect = button_rect.copy()
        return Pointer(pointer_surface, pointer_rect, pointer_offset)
