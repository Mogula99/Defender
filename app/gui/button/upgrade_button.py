"""
This module defines the UpgradeButton GUI element that is used in menu-like windows to make the player choose one of the upgrades.
"""
from __future__ import annotations

from pygame import Surface

from app.gui.button.button import Button
from app.utils.constants import Constants
from app.utils.position import Position
from app.utils.upgrade import Upgrade


class UpgradeButton(Button):
    """
    This class represents GUI button element that lets player choose an upgrade.
    """
    def __init__(self, position: Position, surface: Surface, button_text: str, upgrade: Upgrade):
        """
        UpgradeButton constructor
        :param position: Position of the center of the button on the screen
        :param surface: Surface of the button
        :param button_text: Text of the button
        :param upgrade: Upgrade associated with the button
        """
        Button.__init__(self, position, surface, button_text)
        self.upgrade: Upgrade = upgrade

    @staticmethod
    def create_upgrade_button(button_text: str, button_position: Position, upgrade: Upgrade) -> UpgradeButton:
        """
        This is static method responsible for creating the UpgradeButton instance
        :param button_text: Text of the button
        :param button_position: Position of the center of the button on the screen
        :param upgrade: Upgrade associated with the button
        :return: Created upgrade button
        """
        button_surface: Surface = Constants.TEXT_FONT.render(button_text, False, Constants.TEXT_COLOR, Constants.TEXT_BACKGROUND_COLOR)
        button: UpgradeButton = UpgradeButton(button_position, button_surface, button_text, upgrade)
        return button
