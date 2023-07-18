"""
This module contains the Constants class.
"""
import os.path

import pygame
from pygame import Surface, Color
from pygame.font import Font

from app.utils.position import Position


class Constants:
    """
    Constants is a class storing global variables. It is also used as a single point that will load data as images and fonts.
    """
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600

    # POSITIONS OF OBJECTS ON SCREEN
    FIRST_BUTTON_POSITION: Position = Position(SCREEN_WIDTH/2, 300)
    SECOND_BUTTON_POSITION: Position = Position(SCREEN_WIDTH/2, 350)
    THIRD_BUTTON_POSITION: Position = Position(SCREEN_WIDTH/2, 400)
    FOURTH_BUTTON_POSITION: Position = Position(SCREEN_WIDTH/2, 450)
    FIFTH_BUTTON_POSITION: Position = Position(SCREEN_WIDTH/2, 500)

    MAIN_TITLE_POSITION: Position = Position(SCREEN_WIDTH/2, 150)
    UNDER_TITLE_POSITION: Position = Position(SCREEN_WIDTH/2, 200)

    FIRST_VALUE_POSITION: Position = Position(100, 50)
    SECOND_VALUE_POSITION: Position = Position(100, 80)
    THIRD_VALUE_POSITION: Position = Position(100, 110)
    FOURTH_VALUE_POSITION: Position = Position(100, 140)

    # TEXTS
    GAME_OVER_TITLE_TEXT: str = "GAME OVER"
    GAME_OVER_FIRST_BUTTON_TEXT: str = "RETURN TO MAIN MENU"
    GAME_OVER_SECOND_BUTTON_TEXT: str = "EXIT"

    MAIN_MENU_TITLE_TEXT: str = "DEFENDER"
    MAIN_MENU_FIRST_VALUE_TEXT: str = "BEST SCORE: "
    MAIN_MENU_UNDER_TITLE_TEXT: str = "DIFFICULTY: "
    MAIN_MENU_FIRST_BUTTON_TEXT: str = "CONTINUE"
    MAIN_MENU_SECOND_BUTTON_TEXT: str = "NEW GAME"
    MAIN_MENU_THIRD_BUTTON_TEXT: str = "CONTROLS"
    MAIN_MENU_FOURTH_BUTTON_TEXT: str = "EXIT"

    UPGRADE_TITLE_TEXT: str = "CHOOSE AN UPGRADE"

    CONTROLS_TITLE_TEXT: str = "CONTROLS"
    CONTROLS_UNDER_TITLE_TEXT: str = "PRESS ANY BUTTON TO CONTINUE"
    CONTROLS_FIRST_BUTTON_TEXT: str = "KEY UP, KEY DOWN: Choosing menu items"
    CONTROLS_SECOND_BUTTON_TEXT: str = "LEFT KEY, RIGHT KEY: Selecting difficulty in the main menu"
    CONTROLS_THIRD_BUTTON_TEXT: str = "ENTER: Confirm selection"
    CONTROLS_FOURTH_BUTTON_TEXT: str = "LEFT MOUSE BUTTON: Fire projectile"
    CONTROLS_FIFTH_BUTTON_TEXT: str = "ESC: Close the current window"

    GAMEPLAY_HEALTH_TEXT: str = "HEALTH: "
    GAMEPLAY_SCORE_TEXT: str = "SCORE: "
    GAMEPLAY_ROUND_TEXT: str = "ROUND: "
    GAMEPLAY_ENEMIES_LEFT_TEXT: str = "ENEMIES LEFT: "

    # PATHS AND NAMES

    PACKAGE_PATH: str = ""
    IMAGES_PATH: str = os.path.join("media", "images", "")
    FONTS_PATH: str = os.path.join("media", "fonts", "")
    SAVE_FILE_NAME: str = "save.txt"
    APPLICATION_NAME: str = "Defender"

    # COLORS

    HIGHLIGHT_COLOR: Color = pygame.Color("Aqua")
    GAMEPLAY_TEXT_BACKGROUND_COLOR: Color = pygame.Color("White")
    GAMEPLAY_TEXT_COLOR: Color = pygame.Color("Black")
    MENU_BACKGROUND_COLOR: Color = pygame.Color("Black")
    TEXT_BACKGROUND_COLOR: Color = pygame.Color("Black")
    TEXT_COLOR: Color = pygame.Color("White")
    TITLE_COLOR: Color = pygame.Color("Yellow")
    DISABLED_BUTTON_COLOR: Color = pygame.Color("Grey")

    # GAME CONSTANTS

    # Number of health points the player will start with
    PLAYER_STARTING_HEALTH: int = 15

    # Base number of enemies. This number is used to count the real number of enemies in every round
    BASE_ENEMIES_CNT: int = 1

    # Modifier saying how difficult the game is. Based on this modifier the number of enemies in every round is counted
    # It also says how many score points the player will get after beating one round
    DIFFICULTY_MODIFIER: int = 1

    # Constant saying the best score achieved. It is modified when a save file is loaded
    BEST_SCORE: int = 0

    # ENEMY ATTRIBUTES

    EASY_ENEMY_HEALTH: int = 1
    EASY_ENEMY_SPEED: float = 0.8
    NORMAL_ENEMY_HEALTH: int = 3
    NORMAL_ENEMY_SPEED: float = 0.6
    BOSS_ENEMY_HEALTH: int = 5
    BOSS_ENEMY_SPEED: float = 0.5

    # TOWER ATTRIBUTES

    BLACK_TOWER_POSITION: Position = Position(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    RED_TOWER_POSITION: Position = Position(500, 400)
    GREEN_TOWER_POSITION: Position = Position(300, 400)
    BLUE_TOWER_POSITION: Position = Position(300, 200)
    GREY_TOWER_POSITION: Position = Position(500, 200)

    BLACK_PROJECTILE_SPEED: float = 2
    BLACK_PROJECTILE_DAMAGE: int = 1
    BLACK_PROJECTILE_DAMAGE_UPGRADE: int = 1
    BLACK_PROJECTILE_COOLDOWN: int = 450
    BLACK_PROJECTILE_COOLDOWN_UPGRADE: int = 150

    RED_PROJECTILE_SPEED: float = 1
    RED_PROJECTILE_DAMAGE: int = 3
    RED_PROJECTILE_DAMAGE_UPGRADE: int = 1
    RED_PROJECTILE_COOLDOWN: int = 3000
    RED_PROJECTILE_COOLDOWN_UPGRADE: int = 1000
    RED_PROJECTILE_RADIUS: int = 100
    RED_PROJECTILE_RADIUS_UPGRADE: int = 50

    GREEN_PROJECTILE_SPEED: float = 2
    GREEN_PROJECTILE_DAMAGE: int = 1
    GREEN_PROJECTILE_DAMAGE_UPGRADE: int = 1
    GREEN_PROJECTILE_COOLDOWN: int = 3000
    GREEN_PROJECTILE_COOLDOWN_UPGRADE: int = 1500
    GREEN_PROJECTILE_BOUNCES: int = 3
    GREEN_PROJECTILE_BOUNCES_UPGRADE: int = 1

    BLUE_PROJECTILE_SPEED: float = 1.3
    BLUE_PROJECTILE_DAMAGE: int = 3
    BLUE_PROJECTILE_DAMAGE_UPGRADE: int = 1
    BLUE_PROJECTILE_COOLDOWN: int = 3000
    BLUE_PROJECTILE_COOLDOWN_UPGRADE: int = 1000
    BLUE_PROJECTILE_PASSES: int = 2
    BLUE_PROJECTILE_PASSES_UPGRADE: int = 1

    # SURFACES AND FONTS

    BACKGROUND_SURFACE: Surface = None

    BLACK_TOWER_SURFACE: Surface = None
    BLACK_PROJECTILE_SURFACE: Surface = None
    RED_TOWER_SURFACE: Surface = None
    RED_PROJECTILE_SURFACE: Surface = None
    GREEN_TOWER_SURFACE: Surface = None
    GREEN_PROJECTILE_SURFACE: Surface = None
    BLUE_TOWER_SURFACE: Surface = None
    BLUE_PROJECTILE_SURFACE: Surface = None
    GREY_TOWER_SURFACE: Surface = None

    EASY_ENEMY_SURFACE: Surface = None
    NORMAL_ENEMY_SURFACE: Surface = None
    BOSS_ENEMY_SURFACE: Surface = None

    POINTER_SURFACE = None

    TITLE_FONT: pygame.font.Font = None
    TEXT_FONT: pygame.font.Font = None

    @staticmethod
    def load_media():
        """
        This method will load all the necessary images and fonts
        """

        Constants.BACKGROUND_SURFACE = Constants.__load_image("background.png")

        Constants.BLACK_TOWER_SURFACE = Constants.__load_image("black_tower.png")
        Constants.BLACK_PROJECTILE_SURFACE = Constants.__load_image("black_projectile.png")
        Constants.RED_TOWER_SURFACE = Constants.__load_image("red_tower.png")
        Constants.RED_PROJECTILE_SURFACE = Constants.__load_image("red_projectile.png")
        Constants.GREEN_TOWER_SURFACE = Constants.__load_image("green_tower.png")
        Constants.GREEN_PROJECTILE_SURFACE = Constants.__load_image("green_projectile.png")
        Constants.BLUE_TOWER_SURFACE = Constants.__load_image("blue_tower.png")
        Constants.BLUE_PROJECTILE_SURFACE = Constants.__load_image("blue_projectile.png")
        Constants.GREY_TOWER_SURFACE = Constants.__load_image("grey_tower.png")
        Constants.GREY_PROJECTILE_SURFACE = Constants.BLACK_PROJECTILE_SURFACE

        Constants.EASY_ENEMY_SURFACE = Constants.__load_image("easy_enemy.png")
        Constants.NORMAL_ENEMY_SURFACE = Constants.__load_image("normal_enemy.png")
        Constants.BOSS_ENEMY_SURFACE = Constants.__load_image("boss_enemy.png")
        Constants.POINTER_SURFACE = Constants.__load_image("pointer.png")

        # Constants.TITLE_FONT = pygame.fonts.Font(None, 50)
        # Constants.TEXT_FONT = pygame.fonts.Font(None, 30)
        Constants.TITLE_FONT = Constants.__load_font("FFFFORWA.TTF", 40)
        Constants.TEXT_FONT = Constants.__load_font("FFFFORWA.TTF", 14)

    @staticmethod
    def __load_image(image_name: str) -> Surface:
        """
        This method loads an image with a specified name
        :param image_name: Name of the image to load
        :return: Surface created from the image that has been loaded
        """
        file_path: str = os.path.join(Constants.PACKAGE_PATH, Constants.IMAGES_PATH, image_name)
        return pygame.image.load(file_path).convert_alpha()

    @staticmethod
    def __load_font(font_name: str, font_size: int) -> Font:
        """
        This method loads a font with specified name and creates an internal font object with specified font size
        :param font_name: Name of the font to be loaded
        :param font_size: Size of the font
        :return: Font with specified size created from the loaded font
        """
        file_path: str = os.path.join(Constants.PACKAGE_PATH, Constants.FONTS_PATH, font_name)
        return pygame.font.Font(file_path, font_size)
