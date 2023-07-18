"""
This module tests the ControlsWindowController class
"""
import pygame
import pytest
from pygame import Surface

from app.src.applicationcontroller.controls_window_controller import ControlsWindowController
from app.utils.constants import Constants


def constants_fixture() -> ControlsWindowController:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    controls_controller: ControlsWindowController = ControlsWindowController(screen)
    return controls_controller


def test_process_input_1():
    """
    This function tests the process_input() method of the ControlsWindowController class
    """
    controls_controller: ControlsWindowController = constants_fixture()

    pygame.event.clear()
    pygame.event.post(pygame.event.Event(pygame.QUIT))

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        controls_controller.process_input()
    assert pytest_wrapped_e.type == SystemExit


def test_process_input_2():
    """
    This function tests the process_input() method of the ControlsWindowController class
    """
    controls_controller: ControlsWindowController = constants_fixture()

    controls_controller.running = True

    pygame.event.clear()
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN))

    controls_controller.process_input()

    assert controls_controller.running is False
