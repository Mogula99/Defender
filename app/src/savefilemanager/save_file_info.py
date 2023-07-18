"""
This module defines the SaveFileInfo class
"""
from app.utils.difficulty import Difficulty
from app.utils.upgrade import Upgrade


class SaveFileInfo:
    """
    This class contains all the information that is needed to be saved when saving the game
    """
    def __init__(self, round_number: int, difficulty: Difficulty, player_health: int, upgrades: list[Upgrade], best_score: int):
        """
        Constructor for the SaveFileInfo class
        :param round_number: Number of the current round
        :param difficulty: Difficulty chosen by the player
        :param player_health: Current number of player's health points
        :param upgrades: Upgrades chosen by the player in the game
        :param best_score: Best score achieved in the game
        """
        self.round_number: int = round_number
        self.difficulty: Difficulty = difficulty
        self.player_health: int = player_health
        self.upgrades: list[Upgrade] = upgrades
        self.best_score: int = best_score
