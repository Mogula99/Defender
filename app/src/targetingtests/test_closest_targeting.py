"""
This module tests the ClosestTargeting class
"""
import pygame
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.targeting.closest_targeting import ClosestTargeting
from app.utils.constants import Constants
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


def constants_fixture() -> Surface:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    return screen


def test_select_target():
    """
    This function tests the select_target() method of the ClosestTargeting class
    """
    screen: Surface = constants_fixture()
    targeting: ClosestTargeting = ClosestTargeting()

    tower_position: Position = Position(0, 0)

    enemy1: Enemy = Enemy(10, Position(5, 0), screen, DirectionVector(0, 0), 1)
    enemy2: Enemy = Enemy(10, Position(-5, 0), screen, DirectionVector(0, 0), 1)
    enemy3: Enemy = Enemy(10, Position(50, 50), screen, DirectionVector(0, 0), 1)
    enemies: list[Enemy] = [enemy1, enemy2, enemy3]

    target: Enemy = targeting.select_target(tower_position, enemies)
    assert target in (enemy1, enemy2)


def test_select_target2():
    """
    This function tests the select_target() method of the ClosestTargeting class
    """
    constants_fixture()
    targeting: ClosestTargeting = ClosestTargeting()

    tower_position: Position = Position(0, 0)

    enemies: list[Enemy] = []

    target: Enemy = targeting.select_target(tower_position, enemies)
    assert target is None
