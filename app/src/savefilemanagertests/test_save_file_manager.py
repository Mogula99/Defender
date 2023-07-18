"""
This module tests the SaveFileManager class
"""
import os

from app.src.savefilemanager.save_file_info import SaveFileInfo
from app.src.savefilemanager.save_file_manager import SaveFileManager
from app.utils.constants import Constants
from app.utils.difficulty import Difficulty
from app.utils.upgrade import Upgrade


def test_save_game():
    """
    This function tests the save_game() method of the SaveFileManager class
    """
    save_file_manager: SaveFileManager = SaveFileManager()
    save_file_manager.file_name = os.path.join(Constants.PACKAGE_PATH, "testsave.txt")

    save_file_info: SaveFileInfo = SaveFileInfo(2, Difficulty.EASY, 10, [Upgrade.BLACK_AS], 1)
    save_file_manager.save_game(save_file_info)

    loaded_save_file_info: SaveFileInfo = save_file_manager.load_game()

    assert loaded_save_file_info.round_number == save_file_info.round_number
    assert loaded_save_file_info.difficulty == save_file_info.difficulty
    assert loaded_save_file_info.player_health == save_file_info.player_health
    assert loaded_save_file_info.upgrades == save_file_info.upgrades
    assert loaded_save_file_info.best_score == save_file_info.best_score

    os.remove(save_file_manager.file_name)


def test_load_game():
    """
    This function tests the load_game() method of the SaveFileManager class
    """
    save_file_manager: SaveFileManager = SaveFileManager()
    save_file_manager.file_name = os.path.join(Constants.PACKAGE_PATH, "testsave.txt")

    save_file_info: SaveFileInfo = SaveFileInfo(2, Difficulty.EASY, 10, [Upgrade.BLACK_AS], 1)
    save_file_manager.save_game(save_file_info)

    with open(save_file_manager.file_name, 'r+', encoding="utf-8") as f:
        content = f.read()
        f.seek(0, 0)
        f.write("BRAMBORA" + '\n' + content)

    loaded_save_file_info: SaveFileInfo = save_file_manager.load_game()

    assert loaded_save_file_info is None

    os.remove(save_file_manager.file_name)


def test_load_game2():
    """
    This function tests the load_game() method of the SaveFileManager class
    """
    save_file_manager: SaveFileManager = SaveFileManager()
    save_file_manager.file_name = os.path.join(Constants.PACKAGE_PATH, "testsave.txt")

    save_file_info: SaveFileInfo = SaveFileInfo(2, Difficulty.EASY, 999999, [Upgrade.GREEN_AS], 1000000)
    save_file_manager.save_game(save_file_info)

    loaded_save_file_info: SaveFileInfo = save_file_manager.load_game()

    assert loaded_save_file_info is None

    os.remove(save_file_manager.file_name)
