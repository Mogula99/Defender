"""
This module defines the Animator class
"""

from pygame import Surface

from app.src.gameobject.gameobject import GameObject


class Animator:
    """
    This is a class responsible for changing the sprites of a game object
    """
    def __init__(self, surfaces: list[Surface], game_object: GameObject, animation_speed: int):
        """
        The constructor of the Animator class
        :param surfaces: All the sprites that are used for the animation
        :param game_object: The game object that is being animated
        :param animation_speed: The number of frames for which the same sprite will be played
        """
        self.surfaces = surfaces
        self.game_object = game_object
        self.sprite_number = 0
        self.current_frames_cnt = 0
        self.change_sprite_cnt = animation_speed
        self.animation_starts_again = False

    def update(self) -> None:
        """
        This method is called every frame, and it calculates when will the next sprite be changed.
        """
        self.current_frames_cnt += 1
        if self.current_frames_cnt >= self.change_sprite_cnt:
            self.sprite_number += 1
            if self.sprite_number >= len(self.surfaces):
                self.sprite_number = 0
                self.animation_starts_again = True
            self.current_frames_cnt = 0

        self.game_object.image = self.surfaces[int(self.sprite_number)]
        self.game_object.rect = self.game_object.image.get_rect(center=self.game_object.position.get_tuple())
