"""
This module tests the GameOverWindowController class
"""
import pygame
import pytest
from pygame import Surface

from app.src.applicationcontroller.menucontroller.game_over_window_controller import GameOverWindowController
from app.utils.constants import Constants


def constants_fixture() -> GameOverWindowController:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    game_over_menu_controller: GameOverWindowController = GameOverWindowController(screen)
    return game_over_menu_controller


def test_close_window():
    """
    This function tests the close_window() method of the GameOverWindowController class
    """
    game_over_menu_controller: GameOverWindowController = constants_fixture()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        game_over_menu_controller.close_window()
    assert pytest_wrapped_e.type == SystemExit


def test_react_to_key():
    """
    This function tests the react_to_key() method of the GameOverWindowController class
    """
    game_over_menu_controller: GameOverWindowController = constants_fixture()

    game_over_menu_controller.focus_index = 1
    game_over_menu_controller.react_to_key(pygame.K_DOWN)
    assert game_over_menu_controller.focus_index == 0

    game_over_menu_controller.react_to_key(pygame.K_UP)
    assert game_over_menu_controller.focus_index == 1

    game_over_menu_controller.running = True
    game_over_menu_controller.focused_button = game_over_menu_controller.return_button
    game_over_menu_controller.react_to_key(pygame.K_RETURN)
    assert game_over_menu_controller.running is False

    game_over_menu_controller.running = True
    game_over_menu_controller.react_to_key(pygame.K_ESCAPE)
    assert game_over_menu_controller.running is False

    game_over_menu_controller.running = True
    game_over_menu_controller.focused_button = game_over_menu_controller.exit_button
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        game_over_menu_controller.react_to_key(pygame.K_RETURN)
    assert pytest_wrapped_e.type == SystemExit
