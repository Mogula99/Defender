from pygame import Surface

from app.src.gameobject.gameobject import GameObject


class Animator:
    def __init__(self, surfaces: list[Surface], game_object: GameObject, animation_speed: int):
        self.surfaces = surfaces
        self.game_object = game_object
        self.sprite_number = 0
        self.current_frames_cnt = 0
        self.change_sprite_cnt = animation_speed

    def update(self):
        self.current_frames_cnt += 1
        if self.current_frames_cnt >= self.change_sprite_cnt:
            self.sprite_number += 1
            if self.sprite_number >= len(self.surfaces):
                self.sprite_number = 0
            self.current_frames_cnt = 0

        self.game_object.image = self.surfaces[int(self.sprite_number)]
        self.game_object.rect = self.game_object.image.get_rect(center=self.game_object.position.get_tuple())
