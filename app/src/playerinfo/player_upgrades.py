"""
This module defines a PlayerUpgrades class
"""
import random

from app.utils.upgrade import Upgrade


class PlayerUpgrades:
    """
    This class represents all the upgrades that the player may choose or already have chosen.
    """
    def __init__(self):
        self.available: list[Upgrade] = [Upgrade.BLACK_DMG, Upgrade.BLACK_DMG2, Upgrade.BLACK_AS, Upgrade.BLACK_AS2,
                                         Upgrade.GREY_TWR, Upgrade.RED_TWR, Upgrade.BLUE_TWR, Upgrade.GREEN_TWR]
        self.bought: list[Upgrade] = []

    def choose_three(self) -> list[Upgrade]:
        """
        This method chooses three random upgrades out of the list of available upgrades
        :return: List of 3 random upgrades available to the player
        """
        chosen_upgrades: list[Upgrade] = []

        if len(self.available) <= 3:
            return self.available

        while len(chosen_upgrades) != 3:
            random_index: int = random.randint(0, len(self.available)-1)
            random_upgrade: Upgrade = self.available[random_index]
            if random_upgrade not in chosen_upgrades:
                chosen_upgrades.append(random_upgrade)

        return chosen_upgrades

    def apply_upgrade(self, upgrade: Upgrade):
        """
        This method updates the lists of available and bought upgrades based on the upgrade that the player chose
        :param upgrade: Upgrade that the player chose on the upgrade window
        """
        self.available.remove(upgrade)
        self.bought.append(upgrade)

        if upgrade == Upgrade.RED_TWR:
            self.available.append(Upgrade.RED_AS)
            self.available.append(Upgrade.RED_DMG)
            self.available.append(Upgrade.RED_RADIUS)
            self.available.append(Upgrade.RED_RADIUS2)
        elif upgrade == Upgrade.GREEN_TWR:
            self.available.append(Upgrade.GREEN_AS)
            self.available.append(Upgrade.GREEN_DMG)
            self.available.append(Upgrade.GREEN_BOUNCE)
            self.available.append(Upgrade.GREEN_BOUNCE2)
        elif upgrade == Upgrade.BLUE_TWR:
            self.available.append(Upgrade.BLUE_AS)
            self.available.append(Upgrade.BLUE_DMG)
            self.available.append(Upgrade.BLUE_PASS)
            self.available.append(Upgrade.BLUE_PASS2)
        elif upgrade == Upgrade.GREY_TWR:
            self.available.append(Upgrade.GREY_AS)
            self.available.append(Upgrade.GREY_AS2)
            self.available.append(Upgrade.GREY_DMG)
            self.available.append(Upgrade.GREY_DMG2)

    @staticmethod
    def validate_upgrades(upgrades: list[Upgrade]) -> bool:
        """
        This method checks if it is possible to have a specified list of upgrades applied to the player at one time
        :param upgrades: List of upgrades to check
        :return True if it is possible to have these upgrades at one time. False otherwise.
        """
        if Upgrade.RED_AS in upgrades or Upgrade.RED_DMG in upgrades or Upgrade.RED_RADIUS in upgrades or Upgrade.RED_RADIUS2 in upgrades:
            if Upgrade.RED_TWR not in upgrades:
                return False

        if Upgrade.GREEN_AS in upgrades or Upgrade.GREEN_DMG in upgrades or Upgrade.GREEN_BOUNCE in upgrades or Upgrade.GREEN_BOUNCE2 in upgrades:
            if Upgrade.GREEN_TWR not in upgrades:
                return False

        if Upgrade.BLUE_AS in upgrades or Upgrade.BLUE_DMG in upgrades or Upgrade.BLUE_PASS in upgrades or Upgrade.BLUE_PASS2 in upgrades:
            if Upgrade.BLUE_TWR not in upgrades:
                return False

        if Upgrade.GREY_AS in upgrades or Upgrade.GREY_AS2 in upgrades or Upgrade.GREY_DMG in upgrades or Upgrade.GREY_DMG2 in upgrades:
            if Upgrade.GREY_TWR not in upgrades:
                return False

        return True
