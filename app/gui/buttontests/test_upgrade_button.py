"""
This module tests the UpgradeButton class
"""
import pygame
import pytest

from app.gui.button.upgrade_button import UpgradeButton
from app.utils.constants import Constants
from app.utils.position import Position
from app.utils.upgrade import Upgrade


def constants_fixture():
    """
    This function makes all the necessary preparations co that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()


@pytest.mark.parametrize(
    'button_text, button_position, upgrade',
    [
        ("ASSERT", Position(100, 100), Upgrade.RED_TWR),
        ("NOT AN UPGRADE", Position(-6000, -6000), Upgrade.BLUE_DMG),
        ("UPGRADE", Position(10000, 20000), Upgrade.BLACK_AS),
        ("THIS IS A LONG TEXT FOR AN UPGRADE BUTTON", Position(0, 0), Upgrade.GREY_AS2)
    ])
def test_create_upgrade_button(button_text: str, button_position: Position, upgrade: Upgrade):
    """
    This function tests the create_upgrade_button() method of the UpgradeButton class
    :param button_text: Text of the button
    :param button_position: Position of the button
    :param upgrade: Upgrade associated with the button
    """
    constants_fixture()
    created_button: UpgradeButton = UpgradeButton.create_upgrade_button(button_text, button_position, upgrade)

    assert created_button.button_text == button_text
    assert created_button.rect.centerx == button_position.xCoord
    assert created_button.rect.centery == button_position.yCoord
    assert created_button.image.get_rect(center=button_position.get_tuple()).centerx == button_position.xCoord
    assert created_button.image.get_rect(center=button_position.get_tuple()).centery == button_position.yCoord
    assert created_button.upgrade == upgrade
