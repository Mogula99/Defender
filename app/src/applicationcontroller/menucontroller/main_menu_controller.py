"""
This module defines MainMenuController which is responsible for everything connected with Main Menu window.
"""
import pygame
from pygame import Surface

from app.gui.button.button import Button
from app.gui.text.text import Text
from app.src.applicationcontroller.controls_window_controller import ControlsWindowController
from app.src.applicationcontroller.gameplay_controller import GameplayController
from app.src.applicationcontroller.menucontroller.menu_controller import MenuController
from app.src.playerinfo.player_info import PlayerInfo
from app.src.savefilemanager.save_file_info import SaveFileInfo
from app.src.savefilemanager.save_file_manager import SaveFileManager
from app.utils.constants import Constants
from app.utils.difficulty import Difficulty


class MainMenuController(MenuController):
    """
    This class is responsible for drawing all the buttons and texts in the main menu window.
    It takes player input and refreshes the game screen accordingly.
    """
    def __init__(self, screen: Surface):
        """
        Constructor of the MainMenuController class
        :param screen: Screen that is used to render the game
        """
        self.chosen_difficulty: Difficulty = Difficulty.EASY

        # buttons
        self.continue_button: Button = Button.create_menu_button(Constants.MAIN_MENU_FIRST_BUTTON_TEXT, Constants.FIRST_BUTTON_POSITION)
        self.new_game_button: Button = Button.create_menu_button(Constants.MAIN_MENU_SECOND_BUTTON_TEXT, Constants.SECOND_BUTTON_POSITION)
        self.controls_button: Button = Button.create_menu_button(Constants.MAIN_MENU_THIRD_BUTTON_TEXT, Constants.THIRD_BUTTON_POSITION)
        self.exit_button: Button = Button.create_menu_button(Constants.MAIN_MENU_FOURTH_BUTTON_TEXT, Constants.FOURTH_BUTTON_POSITION)
        buttons: list[Button] = [self.continue_button, self.new_game_button, self.controls_button, self.exit_button]

        # simple texts
        game_name_text: Text = Text.create_title(Constants.MAIN_MENU_TITLE_TEXT, Constants.MAIN_TITLE_POSITION)
        self.best_score_text: Text = Text.create_text(Constants.MAIN_MENU_FIRST_VALUE_TEXT + str(Constants.BEST_SCORE), Constants.FIRST_VALUE_POSITION)
        self.difficulty_text: Text = Text.create_text(Constants.MAIN_MENU_UNDER_TITLE_TEXT + self.chosen_difficulty.name, Constants.UNDER_TITLE_POSITION)
        texts: list[Text] = [game_name_text, self.best_score_text, self.difficulty_text]

        MenuController.__init__(self, screen, texts, buttons)

        self.save_file_manager: SaveFileManager = SaveFileManager()

        self.__load_best_score()

    def __load_best_score(self):
        """
        This method loads best score from the last save file.
        It will deactivate the continue button if the save file does not exist or is corrupted in some way
        """
        saved_info: SaveFileInfo = self.save_file_manager.load_game()
        if saved_info is None:
            # Unable to load last saved game session
            Constants.BEST_SCORE = 0
            self.disable_button(self.continue_button)
        else:
            if Constants.BEST_SCORE < saved_info.best_score:
                Constants.BEST_SCORE = saved_info.best_score
            if self.continue_button in self.disabled_buttons:
                self.enable_button(self.continue_button)

        self.best_score_text.refresh_text(Constants.MAIN_MENU_FIRST_VALUE_TEXT + str(Constants.BEST_SCORE))

    def close_window(self):
        """
        This method is responsible for closing the current window opened by MainMenuController
        """
        self.running: bool = False

    def react_to_key(self, pressed_key: int):
        """
        This method is responsible for handling the player input while on the MainMenu window
        :param pressed_key: Key that has been pressed
        """
        if pressed_key in (pygame.K_DOWN, pygame.K_UP):
            self.change_focus(pressed_key)
        elif pressed_key == pygame.K_RETURN:
            # Enter has been pressed
            if self.focused_button == self.new_game_button:
                # Player chose the new game button
                Constants.DIFFICULTY_MODIFIER = self.chosen_difficulty
                game_controller: GameplayController = GameplayController(self.screen)
                game_controller.run()
                self.__load_best_score()
            elif self.focused_button == self.continue_button:
                # Player chose the continue button
                save_file_info: SaveFileInfo = self.save_file_manager.load_game()
                Constants.DIFFICULTY_MODIFIER = save_file_info.difficulty
                player_info: PlayerInfo = PlayerInfo(save_file_info.player_health, save_file_info.upgrades)
                game_controller: GameplayController = GameplayController(self.screen, player_info,
                                                                         save_file_info.round_number)
                Constants.BEST_SCORE = save_file_info.best_score
                game_controller.run()
            elif self.focused_button == self.controls_button:
                # Player chose the controls button
                controls_window_controller: ControlsWindowController = ControlsWindowController(self.screen)
                controls_window_controller.run()
            elif self.focused_button == self.exit_button:
                # Player chose the exit button
                self.running: bool = False
        elif pressed_key in (pygame.K_LEFT, pygame.K_RIGHT):
            self.__change_difficulty(pressed_key)
        elif pressed_key == pygame.K_ESCAPE:
            self.running: bool = False

    def __change_difficulty(self, key: int):
        """
        This method changes the difficulty chosen by the player
        :param key: Key that has been pressed while on MainMenu window
        """
        if key == pygame.K_RIGHT:
            self.chosen_difficulty += 1
            if self.chosen_difficulty > Difficulty.HARD.value:
                self.chosen_difficulty: int = Difficulty.EASY.value
        elif key == pygame.K_LEFT:
            self.chosen_difficulty -= 1
            if self.chosen_difficulty < Difficulty.EASY.value:
                self.chosen_difficulty: int = Difficulty.HARD.value

        self.chosen_difficulty: Difficulty = Difficulty(self.chosen_difficulty)
        self.difficulty_text.refresh_text(Constants.MAIN_MENU_UNDER_TITLE_TEXT + self.chosen_difficulty.name)
