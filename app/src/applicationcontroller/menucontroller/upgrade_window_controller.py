"""
This module defines UpgradeWindowController which is responsible for everything connected with Upgrade window.
"""
import sys

import pygame
from pygame import Surface

from app.gui.button.upgrade_button import UpgradeButton
from app.gui.text.text import Text
from app.src.applicationcontroller.menucontroller.menu_controller import MenuController
from app.src.playerinfo.player_info import PlayerInfo
from app.utils.constants import Constants
from app.utils.position import Position
from app.utils.upgrade import Upgrade


class UpgradeWindowController(MenuController):
    """
    This class is responsible rendering all the buttons and texts in the upgrade window.
    It takes player input and refreshes the game screen accordingly.
    """
    def __init__(self, screen: Surface, player_info: PlayerInfo):
        """
        Constructor of the UpgradeWindowController class
        :param screen: Screen that is used to render the game
        :param player_info: Information about the current player
        """
        title_text: Text = Text.create_text(Constants.UPGRADE_TITLE_TEXT, Constants.MAIN_TITLE_POSITION)
        texts: list[Text] = [title_text]

        random_upgrades: list[Upgrade] = player_info.choose_three_upgrades()
        buttons: list[UpgradeButton] = self.__create_upgrade_buttons(random_upgrades)

        MenuController.__init__(self, screen, texts, buttons)
        self.player_info: PlayerInfo = player_info

    def __create_upgrade_buttons(self, random_upgrades: list[Upgrade]) -> list[UpgradeButton]:
        """
        This method is responsible for creating upgrade buttons
        :param random_upgrades: List of upgrades that we want to render on the screen
        :return: List of upgrade buttons with their associated upgrades
        """
        buttons: list[UpgradeButton] = []
        button_positions: list[Position] = [Constants.FIRST_BUTTON_POSITION, Constants.SECOND_BUTTON_POSITION, Constants.THIRD_BUTTON_POSITION]

        for button_index, upgrade in enumerate(random_upgrades):
            if len(random_upgrades) > button_index:
                upgrade_button: UpgradeButton = UpgradeButton.create_upgrade_button(upgrade.to_button_string(), button_positions[button_index], upgrade)
                buttons.append(upgrade_button)
        return buttons

    def close_window(self):
        """
        This method is responsible for closing the current window
        """
        sys.exit()

    def react_to_key(self, pressed_key: int):
        """
        This method is responsible for handling the player input
        :param pressed_key: Key pressed by the player while on current screen
        """
        if pressed_key in (pygame.K_UP, pygame.K_DOWN):
            # Player is choosing upgrades with UP and DOWN arrows
            self.change_focus(pressed_key)
        if pressed_key == pygame.K_RETURN:
            self.player_info.apply_upgrade(self.focused_button.upgrade)
            self.running: bool = False
        if pressed_key == pygame.K_ESCAPE:
            self.running: bool = False
