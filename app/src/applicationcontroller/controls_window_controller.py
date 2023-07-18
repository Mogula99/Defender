"""
This module defines ControlsWindowController which is responsible for everything connected with Controls window.
"""
import sys

import pygame

from app.gui.text.text import Text
from app.src.applicationcontroller.application_controller import ApplicationController
from app.utils.constants import Constants


class ControlsWindowController(ApplicationController):
    """
    This class is responsible for rendering all the texts in the Controls window.
    It takes the player input and reacts accordingly.
    """
    def __init__(self, screen: pygame.surface.Surface):
        """
        Constructor of the ControlsWindowController class
        :param screen: Screen that is used to render the window
        """
        title_text: Text = Text.create_title(Constants.CONTROLS_TITLE_TEXT, Constants.MAIN_TITLE_POSITION)
        hint_text: Text = Text.create_text(Constants.CONTROLS_UNDER_TITLE_TEXT, Constants.UNDER_TITLE_POSITION, Constants.HIGHLIGHT_COLOR)
        first_tip_text: Text = Text.create_text(Constants.CONTROLS_FIRST_BUTTON_TEXT, Constants.FIRST_BUTTON_POSITION)
        second_tip_text: Text = Text.create_text(Constants.CONTROLS_SECOND_BUTTON_TEXT, Constants.SECOND_BUTTON_POSITION)
        third_tip_text: Text = Text.create_text(Constants.CONTROLS_THIRD_BUTTON_TEXT, Constants.THIRD_BUTTON_POSITION)
        fourth_tip_text: Text = Text.create_text(Constants.CONTROLS_FOURTH_BUTTON_TEXT, Constants.FOURTH_BUTTON_POSITION)
        fifth_tip_text: Text = Text.create_text(Constants.CONTROLS_FIFTH_BUTTON_TEXT, Constants.FIFTH_BUTTON_POSITION)

        texts: list[Text] = [title_text, hint_text, first_tip_text, second_tip_text, third_tip_text, fourth_tip_text, fifth_tip_text]

        ApplicationController.__init__(self, screen, texts)

    def process_input(self):
        """
        Method responsible for handling the player's input
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.running = False

    def update_game(self):
        """
        Method that is used to update all the objects on the window's screen
        """
