"""
This module defines the SaveFileManager class
"""
import os

from app.src.playerinfo.player_upgrades import PlayerUpgrades
from app.src.savefilemanager.save_file_info import SaveFileInfo
from app.utils.constants import Constants
from app.utils.difficulty import Difficulty
from app.utils.upgrade import Upgrade


class SaveFileManager:
    """
    This class is responsible for saving and loading the game from save.txt file is the root directory of the game
    """
    def __init__(self):
        """
        Constructor of the SaveFileManager class
        """
        self.file_name: str = os.path.join(Constants.PACKAGE_PATH, Constants.SAVE_FILE_NAME)
        print("Looking for a save file on", self.file_name)

    def save_game(self, save_file_info: SaveFileInfo):
        """
        This method saves the specified save_file_info into file class save.txt
        :param save_file_info: Information about the current game session that should be saved
        """
        try:
            with open(self.file_name, mode="wt", encoding="utf-8") as file:
                file.write(str(save_file_info.round_number) + "\n")
                file.write(str(save_file_info.difficulty.value) + "\n")
                file.write(str(save_file_info.player_health) + "\n")
                for upgrade in save_file_info.upgrades:
                    file.write(str(upgrade.value))
                    if upgrade != save_file_info.upgrades[-1]:
                        file.write(" ")
                file.write("\n")
                file.write(str(save_file_info.best_score) + "\n")
        except (OSError, ValueError, TypeError):
            print("Unable to save the game")

    def load_game(self) -> SaveFileInfo:
        """
        This method loads information about the last game session from the save.txt file
        :return: Information saved in the save.txt file. None if the file doesn't exist or is corrupted in some way.
        """
        try:
            with open(self.file_name, mode="rt", encoding="utf-8") as file:
                round_number: int = int(file.readline())
                difficulty: Difficulty = Difficulty(int(file.readline()))
                player_health: int = int(file.readline())
                upgrades: list[Upgrade] = [Upgrade(int(i)) for i in file.readline().split(' ') if i != "\n"]
                best_score: int = int(file.readline())
                save_file_info: SaveFileInfo = SaveFileInfo(round_number, difficulty, player_health, upgrades,
                                                            best_score)
        except (OSError, ValueError, TypeError) as e:
            # If anything happens during loading of the game, the continue button will be disabled
            print("Exception thrown when trying to load the save file:", e)
            return None
        if not self.__validate_data(save_file_info):
            print("Invalid data in the save file")
            return None
        return save_file_info

    def __validate_data(self, save_file_info: SaveFileInfo) -> bool:
        """
        This method validates all the data loaded from a save file.
        :param save_file_info: Information loaded from the save file
        :return: True if the information seem valid. False otherwise
        """
        max_difficulty_value = max(difficulty.value for difficulty in Difficulty)
        min_difficulty_value = min(difficulty.value for difficulty in Difficulty)

        # Just an arbitrary limit for round_numbers. Not a good practice, but I know noone will play this game for longer than 2 minutes.
        if 1 <= save_file_info.round_number <= 100:
            if min_difficulty_value <= save_file_info.difficulty <= max_difficulty_value:
                if 0 < save_file_info.player_health <= Constants.PLAYER_STARTING_HEALTH:
                    # The limit for best score is taken with relation to the arbitrary limit for round_numbers
                    if 0 <= save_file_info.best_score <= 3 * 100:
                        if self.__validate_upgrades(save_file_info.upgrades, save_file_info.round_number):
                            return True
        return False

    def __validate_upgrades(self, upgrades: list[Upgrade], round_number: int) -> bool:
        """
        This method tests the upgrades that has been loaded from the save file
        :param upgrades: list of loaded upgrades
        :param round_number: round_number loaded from the save file
        :return: True if the upgrades are valid. False otherwise
        """
        max_upgrade_value = max(upgrade.value for upgrade in Upgrade)
        min_upgrade_value = min(upgrade.value for upgrade in Upgrade)
        # The loaded upgrades must be valid
        if PlayerUpgrades.validate_upgrades(upgrades):
            # Number of upgrades must be lower than round number otherwise the player is cheating
            if len(upgrades) < round_number:
                # Upgrades must have valid values
                for upgrade in upgrades:
                    if not min_upgrade_value <= upgrade.value <= max_upgrade_value:
                        return False
                return True
        return False
