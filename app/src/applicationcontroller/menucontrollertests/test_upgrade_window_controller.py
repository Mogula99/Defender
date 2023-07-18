"""
This module tests the UpgradeWindowController class
"""
import pygame
import pytest
from pygame import Surface

from app.gui.button.upgrade_button import UpgradeButton
from app.src.applicationcontroller.menucontroller.upgrade_window_controller import UpgradeWindowController
from app.src.playerinfo.player_info import PlayerInfo
from app.utils.constants import Constants
from app.utils.position import Position
from app.utils.upgrade import Upgrade


def constants_fixture() -> UpgradeWindowController:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    player_info: PlayerInfo = PlayerInfo()

    upgrade_window_controller: UpgradeWindowController = UpgradeWindowController(screen, player_info)
    return upgrade_window_controller


def test_close_window():
    """
    This function tests the close_window() function of the UpgradeWindowController class
    """
    upgrade_window_controller: UpgradeWindowController = constants_fixture()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        upgrade_window_controller.close_window()
    assert pytest_wrapped_e.type == SystemExit


def test_react_to_key():
    """
    This function tests the react_to_key() function of the UpgradeWindowController class
    """
    upgrade_window_controller: UpgradeWindowController = constants_fixture()

    upgrade_window_controller.focus_index = 2
    upgrade_window_controller.react_to_key(pygame.K_DOWN)
    assert upgrade_window_controller.focus_index == 0

    upgrade_window_controller.focus_index = 0
    upgrade_window_controller.react_to_key(pygame.K_UP)
    assert upgrade_window_controller.focus_index == 2

    upgrade_window_controller.running = True
    upgrade_window_controller.react_to_key(pygame.K_ESCAPE)
    assert upgrade_window_controller.running is False


def test_react_to_key2():
    """
    This function tests the react_to_key() function of the UpgradeWindowController class
    """
    upgrade_window_controller: UpgradeWindowController = constants_fixture()

    upgrade_window_controller.running = True

    assert Upgrade.RED_TWR in upgrade_window_controller.player_info.upgrades.available
    upgrade_window_controller.focused_button = UpgradeButton.create_upgrade_button("TEST", Position(0, 0), Upgrade.RED_TWR)
    upgrade_window_controller.react_to_key(pygame.K_RETURN)

    assert Upgrade.RED_TWR not in upgrade_window_controller.player_info.upgrades.available
    assert Upgrade.RED_TWR in upgrade_window_controller.player_info.upgrades.bought
    assert upgrade_window_controller.running is False
