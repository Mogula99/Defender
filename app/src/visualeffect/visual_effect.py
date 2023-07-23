"""
This module defines the VisualEffect class
"""
from pygame import Surface

from app.src.animator.animator import Animator
from app.src.gameobject.gameobject import GameObject
from app.utils.position import Position


class VisualEffect(GameObject):
    """
    This class is responsible for rendering a visual special effect
    """
    def __init__(self, position: Position, surfaces: list[Surface], animation_speed: int):
        """
        A constructor of the VisualEffect class
        :param position: Position of the visual effect
        :param surfaces: All the sprites that are used for the animation
        :param animation_speed: The number of frames for which the same sprite will be played
        """
        super().__init__(position, surfaces[0])
        self.animator = Animator(surfaces, self, animation_speed)
        self.is_active = True

    def update(self, *args, **kwargs):
        """
        This method is called every frame and is responsible for the animation tied with the special effect
        """
        GameObject.update(self, *args, **kwargs)
        self.animator.update()
        if self.animator.animation_starts_again:
            self.is_active = False
