"""
This module tests the MainMenuController class
"""

import pygame
from pygame import Surface

from app.src.applicationcontroller.menucontroller.main_menu_controller import MainMenuController
from app.utils.constants import Constants
from app.utils.difficulty import Difficulty


def constants_fixture() -> MainMenuController:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    main_menu_controller: MainMenuController = MainMenuController(screen)
    return main_menu_controller


def test_close_window():
    """
    This function tests the close_window() method of the MainMenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    assert main_menu_controller.running is False

    main_menu_controller.running = True

    main_menu_controller.close_window()

    assert main_menu_controller.running is False


def test_react_to_key():
    """
    This function tests the react_to_key() method of the MainMenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    main_menu_controller.focus_index = 1
    main_menu_controller.react_to_key(pygame.K_DOWN)
    assert main_menu_controller.focus_index == 2

    main_menu_controller.react_to_key(pygame.K_UP)
    assert main_menu_controller.focus_index == 1

    main_menu_controller.chosen_difficulty = Difficulty.EASY
    main_menu_controller.react_to_key(pygame.K_LEFT)
    assert main_menu_controller.chosen_difficulty == Difficulty.HARD

    main_menu_controller.chosen_difficulty = Difficulty.EASY
    main_menu_controller.react_to_key(pygame.K_RIGHT)
    assert main_menu_controller.chosen_difficulty == Difficulty.MEDIUM
    main_menu_controller.react_to_key(pygame.K_RIGHT)
    assert main_menu_controller.chosen_difficulty == Difficulty.HARD

    main_menu_controller.focused_button = main_menu_controller.exit_button
    main_menu_controller.react_to_key(pygame.K_RETURN)
    assert main_menu_controller.running is False


def test_react_to_key2():
    """
    This function tests the react_to_key() method of the MainMenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    main_menu_controller.running = True
    main_menu_controller.react_to_key(pygame.K_ESCAPE)
    assert main_menu_controller.running is False
