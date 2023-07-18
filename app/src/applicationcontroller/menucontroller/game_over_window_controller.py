"""
This module defines GameOverWindowController which is responsible for everything connected with Game Over window.
"""
import sys

import pygame
from pygame import Surface

from app.gui.button.button import Button
from app.gui.text.text import Text
from app.src.applicationcontroller.menucontroller.menu_controller import MenuController
from app.utils.constants import Constants


class GameOverWindowController(MenuController):
    """
    This class is responsible for the Game Over window. It renders all the texts and buttons there.
    It takes player input and refreshes the window accordingly.
    """
    def __init__(self, screen: Surface):
        """
        Constructor of the GameOverWindowController class
        :param screen: Screen that is used to render the game
        """
        title_text: Text = Text.create_title(Constants.GAME_OVER_TITLE_TEXT, Constants.MAIN_TITLE_POSITION)
        self.texts: list[Text] = [title_text]

        self.return_button: Button = Button.create_menu_button(Constants.GAME_OVER_FIRST_BUTTON_TEXT, Constants.FIRST_BUTTON_POSITION)
        self.exit_button: Button = Button.create_menu_button(Constants.GAME_OVER_SECOND_BUTTON_TEXT, Constants.SECOND_BUTTON_POSITION)
        self.buttons: list[Button] = [self.return_button, self.exit_button]

        MenuController.__init__(self, screen, self.texts, self.buttons)

    def close_window(self):
        """
        This method closes the window opened by GameOverWindowController
        """
        sys.exit()

    def react_to_key(self, pressed_key: int):
        """
        This method handles the key pressed while the window is up
        :param pressed_key: Key pressed
        """
        if pressed_key in (pygame.K_UP, pygame.K_DOWN):
            self.change_focus(pressed_key)
        elif pressed_key == pygame.K_RETURN:
            # Enter has been pressed
            if self.focused_button == self.return_button:
                self.running: bool = False
            elif self.focused_button == self.exit_button:
                sys.exit()
        elif pressed_key == pygame.K_ESCAPE:
            self.running: bool = False
