"""
This module defines a GameObject class. It represents everything that will appear on the screen and is not a GUI element.
"""
from pygame.sprite import Sprite
from pygame import Rect, Surface

from app.utils.position import Position


class GameObject(Sprite):
    """
    GameObject is a class that represents every object that will be displayed in the game.
    """
    def __init__(self, position: Position, surface: Surface):
        """
        Constructor of the GameObject class
        :param position: Position of the center of the game object
        :param surface: Surface that should the game object have
        """
        Sprite.__init__(self)
        self.image: Surface = surface
        self.position: Position = position
        self.rect: Rect = self.image.get_rect(center=position.get_tuple())
