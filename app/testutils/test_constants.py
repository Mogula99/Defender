"""
This module tests the Constants class
"""
import pygame

from app.utils.constants import Constants


def test_load_media():
    """
    This test tests the load_media() function of the Constants class
    """
    pygame.init()
    pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()

    assert Constants.BLACK_PROJECTILE_SURFACE is not None
    assert Constants.BLACK_TOWER_SURFACE is not None
    assert Constants.RED_PROJECTILE_SURFACE is not None
    assert Constants.RED_TOWER_SURFACE is not None
    assert Constants.GREEN_TOWER_SURFACE is not None
    assert Constants.GREEN_PROJECTILE_SURFACE is not None
    assert Constants.BLUE_TOWER_SURFACE is not None
    assert Constants.BLUE_PROJECTILE_SURFACE is not None
    assert Constants.GREY_TOWER_SURFACE is not None
    assert Constants.EASY_ENEMY_SURFACES == []
    assert Constants.NORMAL_ENEMY_SURFACES == []
    assert Constants.BOSS_ENEMY_SURFACES == []
    assert Constants.POINTER_SURFACE is not None
    assert Constants.TITLE_FONT is not None
    assert Constants.TEXT_FONT is not None
