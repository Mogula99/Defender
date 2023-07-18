"""
This module defines ApplicationController which is an abstract class for any type of window controllers.
"""
from abc import ABC, abstractmethod

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.sprite import Group

from app.gui.text.text import Text
from app.utils.constants import Constants


class ApplicationController(ABC):
    """
    This is abstract class that declares all the important methods and variables that are needed in window controllers.
    These methods are basically all parts of the classic "game-loop architecture"
    """
    def __init__(self, screen: Surface, texts: list[Text]):
        """
        Constructor of the ApplicationController class
        :param screen: Screen that is used to render the game
        :param texts: All the texts (not button) present in the current window
        """
        self.screen = screen
        self.running: bool = False

        self.texts_group = Group(texts)

    def run(self):
        """
        Game loop method. This method will launch the window that is defined by the controller
        """
        clock: Clock = Clock()

        self.running = True
        while self.running:
            self.process_input()
            self.update_game()
            self.render_objects()

            clock.tick(60)

    @abstractmethod
    def process_input(self):
        """
        Abstract method that is responsible for handling the player's input
        """

    @abstractmethod
    def update_game(self):
        """
        Abstract method that is responsible for updating all the objects that change while the current window is on
        """

    def render_objects(self):
        """
        Method responsible for drawing all the objects that are present on the current window
        """
        self.screen.fill(Constants.MENU_BACKGROUND_COLOR)
        self.texts_group.draw(self.screen)
        pygame.display.flip()
