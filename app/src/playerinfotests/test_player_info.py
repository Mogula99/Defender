"""
This module tests the PlayerInfo class
"""
import pygame
import pytest
from pygame import Surface

from app.src.playerinfo.player_info import PlayerInfo
from app.utils.constants import Constants
from app.utils.upgrade import Upgrade


def constants_fixture() -> Surface:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    return screen


@pytest.mark.parametrize(
    'start_hp, damage_amount, expected',
    [
        (5, 3, 2),
        (1, 10, -9),
        (1000, 0, 1000),
        (1234, 1234, 0)
    ])
def test_receive_damage(start_hp: int, damage_amount: int, expected: int):
    """
    This function tests the receive_damage() method of the PlayerInfo class
    :param start_hp: Starting value of health_points of the PlayerInfo object
    :param damage_amount: Damage received
    :param expected: Expected amount of health_points after subtraction
    """
    constants_fixture()
    player_info: PlayerInfo = PlayerInfo(start_hp)
    player_info.receive_damage(damage_amount)
    assert player_info.player_health == expected


def test_choose_three_upgrades():
    """
    This function tests the choose_three_upgrades() method of the PlayerInfo class
    """
    constants_fixture()
    player_info: PlayerInfo = PlayerInfo(10, None)

    available_upgrades: list[Upgrade] = player_info.upgrades.available

    chosen_upgrades: list[Upgrade] = player_info.choose_three_upgrades()

    assert len(chosen_upgrades) == 3
    for upgrade in chosen_upgrades:
        assert upgrade in available_upgrades


def test_apply_upgrade():
    """
    This function tests the apply_upgrade() method of the PlayerInfo class
    """
    constants_fixture()
    player_info: PlayerInfo = PlayerInfo()

    player_info.black_tower_projectile.damage = 0
    player_info.apply_upgrade(Upgrade.BLACK_DMG)
    assert player_info.black_tower_projectile.damage == Constants.BLACK_PROJECTILE_DAMAGE_UPGRADE

    player_info.black_tower_projectile.damage = 0
    player_info.apply_upgrade(Upgrade.BLACK_DMG2)
    assert player_info.black_tower_projectile.damage == Constants.BLACK_PROJECTILE_DAMAGE_UPGRADE

    player_info.black_tower_projectile.cooldown = Constants.BLACK_PROJECTILE_COOLDOWN_UPGRADE
    player_info.apply_upgrade(Upgrade.BLACK_AS)
    assert player_info.black_tower_projectile.cooldown == 0

    player_info.black_tower_projectile.cooldown = Constants.BLACK_PROJECTILE_COOLDOWN_UPGRADE
    player_info.apply_upgrade(Upgrade.BLACK_AS2)
    assert player_info.black_tower_projectile.cooldown == 0

    assert player_info.red_tower is None
    player_info.apply_upgrade(Upgrade.RED_TWR)
    assert player_info.red_tower is not None

    player_info.red_tower_projectile.cooldown = Constants.RED_PROJECTILE_COOLDOWN_UPGRADE
    player_info.apply_upgrade(Upgrade.RED_AS)
    assert player_info.red_tower_projectile.cooldown == 0

    player_info.red_tower_projectile.damage = 0
    player_info.apply_upgrade(Upgrade.RED_DMG)
    assert player_info.red_tower_projectile.damage == Constants.RED_PROJECTILE_DAMAGE_UPGRADE

    player_info.red_tower_projectile.explosion_radius = 0
    player_info.apply_upgrade(Upgrade.RED_RADIUS)
    assert player_info.red_tower_projectile.explosion_radius == Constants.RED_PROJECTILE_RADIUS_UPGRADE

    player_info.red_tower_projectile.explosion_radius = 0
    player_info.apply_upgrade(Upgrade.RED_RADIUS2)
    assert player_info.red_tower_projectile.explosion_radius == Constants.RED_PROJECTILE_RADIUS_UPGRADE


def test_apply_upgrade2():
    """
    This function tests the apply_upgrade() method of the PlayerInfo class
    Had to divide test_apply_upgrade function into 2 functions because pylint didn't like how long it was.
    """
    constants_fixture()
    player_info: PlayerInfo = PlayerInfo()

    assert player_info.green_tower is None
    player_info.apply_upgrade(Upgrade.GREEN_TWR)
    assert player_info.green_tower is not None

    player_info.green_tower_projectile.cooldown = Constants.GREEN_PROJECTILE_COOLDOWN_UPGRADE
    player_info.apply_upgrade(Upgrade.GREEN_AS)
    assert player_info.green_tower_projectile.cooldown == 0

    player_info.green_tower_projectile.damage = 0
    player_info.apply_upgrade(Upgrade.GREEN_DMG)
    assert player_info.green_tower_projectile.damage == Constants.GREEN_PROJECTILE_DAMAGE_UPGRADE

    player_info.green_tower_projectile.bounce_count = 0
    player_info.apply_upgrade(Upgrade.GREEN_BOUNCE)
    assert player_info.green_tower_projectile.bounce_count == Constants.GREEN_PROJECTILE_BOUNCES_UPGRADE

    player_info.green_tower_projectile.bounce_count = 0
    player_info.apply_upgrade(Upgrade.GREEN_BOUNCE2)
    assert player_info.green_tower_projectile.bounce_count == Constants.GREEN_PROJECTILE_BOUNCES_UPGRADE

    assert player_info.blue_tower is None
    player_info.apply_upgrade(Upgrade.BLUE_TWR)
    assert player_info.blue_tower is not None

    player_info.blue_tower_projectile.damage = 0
    player_info.apply_upgrade(Upgrade.BLUE_DMG)
    assert player_info.blue_tower_projectile.damage == Constants.BLUE_PROJECTILE_DAMAGE_UPGRADE

    player_info.blue_tower_projectile.cooldown = Constants.BLUE_PROJECTILE_COOLDOWN_UPGRADE
    player_info.apply_upgrade(Upgrade.BLUE_AS)
    assert player_info.blue_tower_projectile.cooldown == 0

    player_info.blue_tower_projectile.pass_through_count = 0
    player_info.apply_upgrade(Upgrade.BLUE_PASS)
    assert player_info.blue_tower_projectile.pass_through_count == Constants.BLUE_PROJECTILE_PASSES_UPGRADE

    player_info.blue_tower_projectile.pass_through_count = 0
    player_info.apply_upgrade(Upgrade.BLUE_PASS2)
    assert player_info.blue_tower_projectile.pass_through_count == Constants.BLUE_PROJECTILE_PASSES_UPGRADE

    assert player_info.grey_tower is None
    player_info.apply_upgrade(Upgrade.GREY_TWR)
    assert player_info.grey_tower is not None

    player_info.grey_tower_projectile.damage = 0
    player_info.apply_upgrade(Upgrade.GREY_DMG)
    assert player_info.grey_tower_projectile.damage == Constants.BLACK_PROJECTILE_DAMAGE_UPGRADE

    player_info.grey_tower_projectile.damage = 0
    player_info.apply_upgrade(Upgrade.GREY_DMG2)
    assert player_info.grey_tower_projectile.damage == Constants.BLACK_PROJECTILE_DAMAGE_UPGRADE

    player_info.grey_tower_projectile.cooldown = Constants.BLACK_PROJECTILE_COOLDOWN_UPGRADE
    player_info.apply_upgrade(Upgrade.GREY_AS)
    assert player_info.grey_tower_projectile.cooldown == 0

    player_info.grey_tower_projectile.cooldown = Constants.BLACK_PROJECTILE_COOLDOWN_UPGRADE
    player_info.apply_upgrade(Upgrade.GREY_AS2)
    assert player_info.grey_tower_projectile.cooldown == 0
