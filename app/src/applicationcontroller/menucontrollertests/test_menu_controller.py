"""
This module tests the MenuController class
"""
import pygame
from pygame import Surface

from app.gui.button.button import Button
from app.src.applicationcontroller.menucontroller.main_menu_controller import MainMenuController
from app.utils.constants import Constants
from app.utils.position import Position


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


def test_update_game():
    """
    This function tests the update_game() method of the MenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    old_ptr_position: Position = Position(main_menu_controller.pointer.rect.centerx,
                                          main_menu_controller.pointer.rect.centery)
    main_menu_controller.focus_index += 1

    main_menu_controller.update_game()

    new_ptr_position: Position = Position(main_menu_controller.pointer.rect.centerx,
                                          main_menu_controller.pointer.rect.centery)

    assert old_ptr_position != new_ptr_position


def test_move_pointer():
    """
    This function tests the move_pointer() method of the MenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    old_ptr_position: Position = Position(main_menu_controller.pointer.rect.centerx,
                                          main_menu_controller.pointer.rect.centery)

    main_menu_controller.focus_index += 1
    main_menu_controller.move_pointer()

    new_ptr_position: Position = Position(main_menu_controller.pointer.rect.centerx,
                                          main_menu_controller.pointer.rect.centery)

    assert old_ptr_position != new_ptr_position


def test_change_focus():
    """
    This function tests the change_focus() method of the MenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    main_menu_controller.focus_index = 1

    old_focus_index = main_menu_controller.focus_index
    old_focused_button = main_menu_controller.focused_button

    disabled_button: Button = main_menu_controller.buttons_group.sprites()[old_focus_index + 1]
    main_menu_controller.disable_button(disabled_button)

    main_menu_controller.change_focus(pygame.K_DOWN)

    new_focus_index = main_menu_controller.focus_index
    new_focused_button = main_menu_controller.focused_button

    assert old_focus_index != new_focus_index
    assert old_focused_button != new_focused_button
    assert new_focused_button != disabled_button


def test_change_focus2():
    """
    This function tests the change_focus() method of the MenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    main_menu_controller.focus_index = 1
    main_menu_controller.focused_button = main_menu_controller.buttons_group.sprites()[1]
    main_menu_controller.disabled_buttons = []

    old_focus_index = main_menu_controller.focus_index
    old_focused_button = main_menu_controller.focused_button

    main_menu_controller.change_focus(pygame.K_UP)

    new_focus_index = main_menu_controller.focus_index
    new_focused_button = main_menu_controller.focused_button

    assert len(main_menu_controller.disabled_buttons) == 0
    assert old_focus_index != new_focus_index
    assert old_focused_button != new_focused_button
    assert old_focus_index == 1
    assert new_focus_index == 0
    assert new_focused_button == main_menu_controller.buttons_group.sprites()[0]


def test_disable_button():
    """
    This function tests the disable_button() method of the MenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    assert len(main_menu_controller.disabled_buttons) == 0

    button_to_disable: Button = main_menu_controller.buttons_group.sprites()[1]

    main_menu_controller.focus_index = 1
    main_menu_controller.focused_button = button_to_disable

    old_button_surface: Surface = button_to_disable.image

    main_menu_controller.disable_button(button_to_disable)

    assert len(main_menu_controller.disabled_buttons) == 1
    assert main_menu_controller.disabled_buttons[0] == button_to_disable
    assert old_button_surface != button_to_disable.image
    assert main_menu_controller.focused_button != button_to_disable
    assert main_menu_controller.focus_index == 2


def test_enable_button():
    """
    This function tests the enable_button() method of the MenuController class
    """
    main_menu_controller: MainMenuController = constants_fixture()

    assert len(main_menu_controller.disabled_buttons) == 0

    button_to_disable: Button = main_menu_controller.buttons_group.sprites()[1]

    main_menu_controller.focus_index = 1
    main_menu_controller.focused_button = button_to_disable

    main_menu_controller.disable_button(button_to_disable)

    old_button_surface: Surface = button_to_disable.image

    assert len(main_menu_controller.disabled_buttons) == 1
    assert main_menu_controller.disabled_buttons[0] == button_to_disable
    assert main_menu_controller.focused_button != button_to_disable
    assert main_menu_controller.focus_index == 2

    main_menu_controller.enable_button(button_to_disable)

    assert len(main_menu_controller.disabled_buttons) == 0
    assert old_button_surface != button_to_disable.image
    assert main_menu_controller.focused_button != button_to_disable
    assert main_menu_controller.focus_index == 2
