"""Main file of the whole game. It makes all the necessary initializations and launches the correct windows"""

import pygame
from pygame import Surface

from app.src.applicationcontroller.controls_window_controller import ControlsWindowController
from app.src.applicationcontroller.menucontroller.main_menu_controller import MainMenuController
from app.utils.constants import Constants


def main():
    """
    This is the main function of the game. It makes all the necessary initializations and launches the correct windows
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

    Constants.load_media()
    pygame.display.set_icon(Constants.EASY_ENEMY_SURFACE)
    pygame.display.set_caption(Constants.APPLICATION_NAME)

    controls: ControlsWindowController = ControlsWindowController(screen)
    controls.run()
    main_menu: MainMenuController = MainMenuController(screen)
    main_menu.run()


if __name__ == "__main__":
    main()
