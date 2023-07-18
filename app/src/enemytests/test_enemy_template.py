"""
This module tests the EnemyTemplate class
"""
import pygame
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.enemy.enemy_template import EnemyTemplate
from app.utils.constants import Constants
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


def constants_fixture() -> EnemyTemplate:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    enemy_template: EnemyTemplate = EnemyTemplate(15, screen, 15)
    return enemy_template


def test_create_enemy():
    """
    This function tests the create_enemy() method of the EnemyTemplate class
    """
    enemy_template: EnemyTemplate = constants_fixture()

    created_enemy: Enemy = enemy_template.create_enemy(Position(0, 0), DirectionVector(0, 0))

    assert created_enemy.health == enemy_template.health
    assert created_enemy.position.xCoord == 0
    assert created_enemy.position.yCoord == 0
    assert created_enemy.speed == enemy_template.speed
    assert created_enemy.image == enemy_template.surface
    assert created_enemy.direction.xCoord == 0
    assert created_enemy.direction.yCoord == 0
