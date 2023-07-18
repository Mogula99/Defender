"""
This module tests the PlayerUpgrades class
"""
import pytest

from app.src.playerinfo.player_upgrades import PlayerUpgrades
from app.utils.upgrade import Upgrade


def test_choose_three():
    """
    This function tests the choose_three() method of the PlayerUpgrades class
    """
    player_upgrades: PlayerUpgrades = PlayerUpgrades()

    chosen_upgrades: list[Upgrade] = player_upgrades.choose_three()

    assert len(chosen_upgrades) == 3
    for upgrade in chosen_upgrades:
        assert upgrade in player_upgrades.available

    player_upgrades.bought = list(Upgrade)
    player_upgrades.available = []
    chosen_upgrades: list[Upgrade] = player_upgrades.choose_three()

    assert len(chosen_upgrades) == 0

    player_upgrades.bought = [upgrade for upgrade in Upgrade if upgrade != Upgrade.GREY_DMG]
    player_upgrades.available = [Upgrade.GREY_DMG]
    chosen_upgrades: list[Upgrade] = player_upgrades.choose_three()
    assert len(chosen_upgrades) == 1
    assert chosen_upgrades[0] == Upgrade.GREY_DMG


def test_apply_upgrade():
    """
    This function tests the choose_three() method of the PlayerUpgrades class
    """
    player_upgrades: PlayerUpgrades = PlayerUpgrades()

    assert Upgrade.RED_TWR not in player_upgrades.bought
    assert Upgrade.RED_AS not in player_upgrades.bought
    assert Upgrade.RED_DMG not in player_upgrades.bought
    assert Upgrade.RED_RADIUS not in player_upgrades.bought
    assert Upgrade.RED_RADIUS2 not in player_upgrades.bought
    assert Upgrade.GREY_AS not in player_upgrades.bought
    assert Upgrade.BLUE_DMG not in player_upgrades.bought
    assert Upgrade.GREEN_BOUNCE not in player_upgrades.bought

    assert Upgrade.RED_TWR in player_upgrades.available
    assert Upgrade.RED_AS not in player_upgrades.available
    assert Upgrade.RED_DMG not in player_upgrades.available
    assert Upgrade.RED_RADIUS not in player_upgrades.available
    assert Upgrade.RED_RADIUS2 not in player_upgrades.available
    assert Upgrade.GREY_AS not in player_upgrades.available
    assert Upgrade.BLUE_DMG not in player_upgrades.available
    assert Upgrade.GREEN_BOUNCE not in player_upgrades.available

    player_upgrades.apply_upgrade(Upgrade.RED_TWR)

    assert Upgrade.RED_TWR in player_upgrades.bought
    assert Upgrade.RED_AS not in player_upgrades.bought
    assert Upgrade.RED_DMG not in player_upgrades.bought
    assert Upgrade.RED_RADIUS not in player_upgrades.bought
    assert Upgrade.RED_RADIUS2 not in player_upgrades.bought
    assert Upgrade.GREY_AS not in player_upgrades.bought
    assert Upgrade.BLUE_DMG not in player_upgrades.bought
    assert Upgrade.GREEN_BOUNCE not in player_upgrades.bought

    assert Upgrade.RED_AS in player_upgrades.available
    assert Upgrade.RED_DMG in player_upgrades.available
    assert Upgrade.RED_RADIUS in player_upgrades.available
    assert Upgrade.RED_RADIUS2 in player_upgrades.available
    assert Upgrade.GREY_AS not in player_upgrades.available
    assert Upgrade.BLUE_DMG not in player_upgrades.available
    assert Upgrade.GREEN_BOUNCE not in player_upgrades.available


@pytest.mark.parametrize(
    'upgrades, expected_result',
    [
        ([Upgrade.RED_AS, Upgrade.RED_DMG, Upgrade.RED_RADIUS, Upgrade.RED_RADIUS2, Upgrade.RED_TWR], True),
        ([Upgrade.RED_AS, Upgrade.RED_DMG, Upgrade.RED_RADIUS, Upgrade.RED_RADIUS2], False),
        ([Upgrade.GREY_AS, Upgrade.BLUE_DMG, Upgrade.GREEN_BOUNCE, Upgrade.BLACK_DMG], False),
        ([Upgrade.GREY_TWR, Upgrade.BLUE_TWR, Upgrade.GREEN_TWR, Upgrade.RED_TWR], True),
        ([Upgrade.RED_DMG, Upgrade.RED_TWR, Upgrade.BLUE_PASS, Upgrade.BLUE_TWR, Upgrade.GREEN_TWR, Upgrade.GREEN_BOUNCE2], True),
        (list(Upgrade), True),
        ([], True)
    ])
def test_validate_upgrades(upgrades: list[Upgrade], expected_result: bool):
    """
    This function tests the validate_upgrades() method of the PlayerUpgrades class
    :param upgrades: list of upgrades to validate
    :param expected_result: Expected result of the validation process
    """
    assert PlayerUpgrades.validate_upgrades(upgrades) == expected_result
