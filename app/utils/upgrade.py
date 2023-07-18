"""
This module contains the Upgrade enum class
"""

from __future__ import annotations
from enum import Enum


class Upgrade(Enum):
    """
    Upgrade is an enum class representing all the upgrade that are possible to get in this game.
    It does have a method called to_button_string() that will return a string representation of the upgrade
    that can be used for button text in the game
    """
    BLACK_DMG = 0
    BLACK_DMG2 = 1
    BLACK_AS = 2
    BLACK_AS2 = 3
    GREEN_TWR = 4
    GREEN_DMG = 5
    GREEN_AS = 6
    GREEN_BOUNCE = 7
    GREEN_BOUNCE2 = 8
    RED_TWR = 9
    RED_DMG = 10
    RED_AS = 11
    RED_RADIUS = 12
    RED_RADIUS2 = 13
    BLUE_TWR = 14
    BLUE_DMG = 15
    BLUE_AS = 16
    BLUE_PASS = 17
    BLUE_PASS2 = 18
    GREY_TWR = 19
    GREY_DMG = 20
    GREY_DMG2 = 21
    GREY_AS = 22
    GREY_AS2 = 23

    def to_button_string(self) -> str:
        """
        This method returns a string representation of an upgrade that will be used on upgrade window
        :return: String representation of an upgrade
        """
        result: str = ""
        match self:
            case Upgrade.BLACK_DMG:
                result: str = "Increase damage of black tower"
            case Upgrade.BLACK_DMG2:
                result: str = "Increase damage of black tower"
            case Upgrade.BLACK_AS:
                result: str = "Increase attack speed of black tower"
            case Upgrade.BLACK_AS2:
                result: str = "Increase attack speed of black tower"
            case Upgrade.GREEN_TWR:
                result: str = "Green tower"
            case Upgrade.GREEN_DMG:
                result: str = "Increase damage of green tower"
            case Upgrade.GREEN_AS:
                result: str = "Increase attack speed of green tower"
            case Upgrade.GREEN_BOUNCE:
                result: str = "Increase number of bounces of green projectiles"
            case Upgrade.GREEN_BOUNCE2:
                result: str = "Increase number of bounces of green projectiles"
            case Upgrade.RED_TWR:
                result: str = "Red tower"
            case Upgrade.RED_DMG:
                result: str = "Increase damage of red tower"
            case Upgrade.RED_AS:
                result: str = "Increase attack speed of red tower"
            case Upgrade.RED_RADIUS:
                result: str = "Increase explosion radius of red tower"
            case Upgrade.RED_RADIUS2:
                result: str = "Increase explosion radius of red tower"
            case Upgrade.BLUE_TWR:
                result: str = "Blue tower"
            case Upgrade.BLUE_DMG:
                result: str = "Increase damage of blue tower"
            case Upgrade.BLUE_AS:
                result: str = "Increase attack speed of blue tower"
            case Upgrade.BLUE_PASS:
                result: str = "Increase number of passes of blue projectiles"
            case Upgrade.BLUE_PASS2:
                result: str = "Increase number of passes of blue projectiles"
            case Upgrade.GREY_TWR:
                result: str = "Grey tower"
            case Upgrade.GREY_DMG:
                result: str = "Increase damage of grey tower"
            case Upgrade.GREY_DMG2:
                result: str = "Increase damage of grey tower"
            case Upgrade.GREY_AS:
                result: str = "Increase attack speed of grey tower"
            case Upgrade.GREY_AS2:
                result: str = "Increase attack speed of grey tower"
        return result
