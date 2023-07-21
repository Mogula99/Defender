"""
This module tests the AutomaticTower class
"""
import pygame
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.projectile.basic_projectile import BasicProjectile
from app.src.projectile.projectile import Projectile
from app.src.targeting.closest_targeting import ClosestTargeting
from app.src.tower.automatic_tower import AutomaticTower
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


def test_auto_fire():
    """
    This function tests the auto_fire() method of the AutomaticTower class
    """
    screen: Surface = constants_fixture()
    tower: AutomaticTower = AutomaticTower(Position(100, 0), screen, BasicProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0), ClosestTargeting())

    tower.cooldown = 0

    near_enemy: Enemy = Enemy(10, Position(100, 100), [screen], DirectionVector(0, 0), 1)
    far_enemy: Enemy = Enemy(10, Position(1000, 1000), [screen], DirectionVector(0, 0), 1)
    enemies: list[Enemy] = [near_enemy, far_enemy]

    fired_projectile: Projectile = tower.auto_fire(enemies)

    assert tower.cooldown == fired_projectile.cooldown
    assert isinstance(fired_projectile, BasicProjectile)
    assert fired_projectile.position.xCoord == tower.position.xCoord
    assert fired_projectile.position.yCoord == tower.position.yCoord
    assert fired_projectile.direction.xCoord == 0
    assert fired_projectile.direction.yCoord == 1
    assert fired_projectile.cooldown == tower.projectile.cooldown
    assert fired_projectile.damage == tower.projectile.damage
    assert fired_projectile.image == tower.projectile.image


def test_auto_fire2():
    """
    This function tests the auto_fire() method of the AutomaticTower class
    """
    screen: Surface = constants_fixture()
    tower: AutomaticTower = AutomaticTower(Position(100, 0), screen, BasicProjectile(Position(0, 0), screen, DirectionVector(0, 0), 0, 0, 0), ClosestTargeting())

    tower.cooldown = 0

    enemies: list[Enemy] = []

    fired_projectile: Projectile = tower.auto_fire(enemies)
    assert fired_projectile is None
    assert tower.cooldown == 0
