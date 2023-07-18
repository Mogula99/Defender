"""
This module defines MovableGameObject class
"""
from pygame import Surface, Rect

from app.src.gameobject.gameobject import GameObject
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class MovableGameObject(GameObject):
    """
    MovableGameObject is a subclass of GameObject. It is a GameObject that will move every frame.
    """
    def __init__(self, position: Position, surface: Surface, direction: DirectionVector, speed: float):
        """
        Constructor of the MovableGameObject class
        :param position: Position of the center of the movable game object on the screen
        :param surface: Surface that the movable game object should have
        :param direction: Direction in which the movable game object should move
        :param speed: Movement speed of the movable game object
        """
        GameObject.__init__(self, position, surface)
        self.direction: DirectionVector = direction
        self.speed: float = speed

    def update(self, *args, **kwargs):
        """
        Method responsible for updating (moving) the movable game object
        """
        self.__move()

    def __update_rect(self):
        """
        This method updates the rectangle of the current movable game object based on its position
        """
        self.rect: Rect = self.image.get_rect(center=self.position.get_tuple())

    def __move(self):
        """
        This method moves the movable game object in his direction
        """
        displacement_x: float = self.direction.xCoord * self.speed
        displacement_y: float = self.direction.yCoord * self.speed

        self.position.xCoord += displacement_x
        self.position.yCoord += displacement_y

        self.__update_rect()
