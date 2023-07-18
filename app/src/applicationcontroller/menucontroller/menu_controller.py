"""
This module defines MenuController which is an abstract class for controllers responsible for any kind of menu windows.
"""
from abc import ABC, abstractmethod

import pygame
from pygame import Surface
from pygame.sprite import GroupSingle, Sprite, Group

from app.gui.button.button import Button
from app.gui.pointer.pointer import Pointer
from app.gui.text.text import Text
from app.src.applicationcontroller.application_controller import ApplicationController
from app.utils.constants import Constants


class MenuController(ApplicationController, ABC):
    """
    This is abstract class that is responsible for menu-like windows.
    """
    def __init__(self, screen: Surface, texts: list[Text], buttons: list[Button]):
        """
        Constructor of the MenuController
        :param screen: Screen that is used to render the game
        :param texts: All the texts (not buttons) present on the window
        :param buttons: All the button present on the window
        """
        ApplicationController.__init__(self, screen, texts)

        self.buttons_group: Group[Button] = pygame.sprite.Group(buttons)
        self.disabled_buttons: list[Button] = []

        self.focus_index: int = 0
        self.focused_button: Button = self.buttons_group.sprites()[self.focus_index]

        self.pointer: Pointer = Pointer.create_pointer(self.focused_button.rect)
        self.pointer_group: GroupSingle[Pointer] = pygame.sprite.GroupSingle(self.pointer)

    def process_input(self):
        """
        This method is responsible for handling the player input on the current window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_window()
            if event.type == pygame.KEYDOWN:
                self.react_to_key(event.key)

    @abstractmethod
    def close_window(self):
        """
        Abstract method used for closing the current window
        """

    @abstractmethod
    def react_to_key(self, pressed_key: int):
        """
        Abstract method used for handling player input
        :param pressed_key: Key pressed on the current window
        """

    def update_game(self):
        """
        This method is responsible for updating all the things that change on the menu window
        """
        self.move_pointer()

    def render_objects(self):
        """
        This method renders all the objects present on the menu window
        """
        self.screen.fill(Constants.MENU_BACKGROUND_COLOR)
        groups_to_draw: list[Group[Sprite]] = [self.buttons_group, self.texts_group, self.pointer_group]

        for group in groups_to_draw:
            group.draw(self.screen)

        pygame.display.flip()

    def move_pointer(self):
        """
        This method moves the pointer to the currently focused button
        :return:
        """
        self.focused_button: Button = self.buttons_group.sprites()[self.focus_index]
        self.pointer.move_pointer(self.focused_button.rect)

    def change_focus(self, key: int):
        """
        This method changes the focused button based on the key pressed
        :param key: Key pressed while on the menu window
        """
        if key == pygame.K_DOWN:
            self.__increase_focus_index()
        elif key == pygame.K_UP:
            self.__decrease_focus_index()

        self.focused_button: Button = self.buttons_group.sprites()[self.focus_index]

        if self.focused_button in self.disabled_buttons:
            self.change_focus(key)

    def __increase_focus_index(self):
        """
        This method increases the focus index of the window
        """
        self.focus_index += 1
        if self.focus_index >= len(self.buttons_group.sprites()):
            self.focus_index: int = 0

    def __decrease_focus_index(self):
        """
        This method decreases the focus index of the window
        """
        self.focus_index -= 1
        if self.focus_index < 0:
            self.focus_index: int = len(self.buttons_group.sprites())-1

    def disable_button(self, button_to_disable: Button):
        """
        This method disables a button - it makes it grey colored and the player won't be able to focus it
        :param button_to_disable: Button that is to be disabled
        """
        self.disabled_buttons.append(button_to_disable)
        button_to_disable.change_text_color(Constants.DISABLED_BUTTON_COLOR)
        if self.focused_button == button_to_disable:
            self.__increase_focus_index()
            self.focused_button: Button = self.buttons_group.sprites()[self.focus_index]

    def enable_button(self, button_to_enable: Button):
        """
        This method enables the button. It makes it a regular colored and the player will be able to focus it
        :param button_to_enable: Button that is to be enabled
        """
        self.disabled_buttons.remove(button_to_enable)
        button_to_enable.change_text_color(Constants.TEXT_COLOR)
