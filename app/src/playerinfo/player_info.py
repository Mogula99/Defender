"""
This module defines the PlayerInfo class
"""
from app.src.playerinfo.player_upgrades import PlayerUpgrades
from app.src.projectile.basic_projectile import BasicProjectile
from app.src.projectile.bouncing_projectile import BouncingProjectile
from app.src.projectile.explosive_projectile import ExplosiveProjectile
from app.src.projectile.ghost_projectile import GhostProjectile
from app.src.targeting.closest_targeting import ClosestTargeting
from app.src.targeting.random_targeting import RandomTargeting
from app.src.tower.automatic_tower import AutomaticTower
from app.src.tower.manual_tower import ManualTower
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position
from app.utils.upgrade import Upgrade
from app.utils.constants import Constants


class PlayerInfo:
    """
    This class represents all the important info regarding the player itself.
    """
    def __init__(self, player_health: int = None, upgrades: list[Upgrade] = None):
        """
        Constructor for the PlayerInfo class
        :param player_health: Health points of the player
        :param upgrades: List of all the upgrades the player has
        """
        if player_health is not None:
            self.player_health: int = player_health
        else:
            self.player_health: int = Constants.PLAYER_STARTING_HEALTH

        self.black_tower: ManualTower = None
        self.black_tower_projectile: BasicProjectile = None
        self.__create_black_tower()

        self.red_tower_projectile: ExplosiveProjectile = None
        self.red_tower: AutomaticTower = None

        self.green_tower_projectile: BouncingProjectile = None
        self.green_tower: AutomaticTower = None

        self.blue_tower_projectile: GhostProjectile = None
        self.blue_tower: AutomaticTower = None

        self.grey_tower_projectile: BasicProjectile = None
        self.grey_tower: AutomaticTower = None

        self.upgrades = PlayerUpgrades()
        if upgrades is not None:
            for upgrade in upgrades:
                self.apply_upgrade(upgrade)

    def receive_damage(self, damage_amount: int):
        """
        This method subtracts specified amount from the current health points of the player
        :param damage_amount: Damage that the player received. How many points of health should be subtracted
        """
        self.player_health -= damage_amount

    def choose_three_upgrades(self) -> list[Upgrade]:
        """
        This method returns 3 random upgrades that should be presented to the player on the upgrade window
        :return: List of 3 random upgrades available to the player
        """
        return self.upgrades.choose_three()

    def __create_black_tower(self):
        """
        This method creates a black tower with its associated projectile
        """
        self.black_tower_projectile: BasicProjectile = BasicProjectile(Position(0, 0),
                                                                       Constants.BLACK_PROJECTILE_SURFACE,
                                                                       DirectionVector(0, 0),
                                                                       Constants.BLACK_PROJECTILE_SPEED,
                                                                       Constants.BLACK_PROJECTILE_DAMAGE,
                                                                       Constants.BLACK_PROJECTILE_COOLDOWN)
        self.black_tower: ManualTower = ManualTower(Constants.BLACK_TOWER_POSITION, Constants.BLACK_TOWER_SURFACE,
                                                    self.black_tower_projectile)

    def __create_red_tower(self):
        """
        This method creates a red tower with its associated projectile
        """
        self.red_tower_projectile: ExplosiveProjectile = ExplosiveProjectile(Position(0, 0),
                                                                             Constants.RED_PROJECTILE_SURFACE,
                                                                             DirectionVector(0, 0),
                                                                             Constants.RED_PROJECTILE_SPEED,
                                                                             Constants.RED_PROJECTILE_DAMAGE,
                                                                             Constants.RED_PROJECTILE_COOLDOWN,
                                                                             Constants.RED_PROJECTILE_RADIUS)
        self.red_tower: AutomaticTower = AutomaticTower(Constants.RED_TOWER_POSITION, Constants.RED_TOWER_SURFACE,
                                                        self.red_tower_projectile, RandomTargeting())

    def __create_green_tower(self):
        """
        This method creates a green tower with its associated projectile
        """
        self.green_tower_projectile: BouncingProjectile = BouncingProjectile(Position(0, 0),
                                                                             Constants.GREEN_PROJECTILE_SURFACE,
                                                                             DirectionVector(0, 0),
                                                                             Constants.GREEN_PROJECTILE_SPEED,
                                                                             Constants.GREEN_PROJECTILE_DAMAGE,
                                                                             Constants.GREEN_PROJECTILE_COOLDOWN,
                                                                             Constants.GREEN_PROJECTILE_BOUNCES)
        self.green_tower: AutomaticTower = AutomaticTower(Constants.GREEN_TOWER_POSITION, Constants.GREEN_TOWER_SURFACE,
                                                          self.green_tower_projectile, RandomTargeting())

    def __create_blue_tower(self):
        """
        This method creates a blue tower with its associated projectile
        """
        self.blue_tower_projectile: GhostProjectile = GhostProjectile(Position(0, 0),
                                                                      Constants.BLUE_PROJECTILE_SURFACE,
                                                                      DirectionVector(0, 0),
                                                                      Constants.BLUE_PROJECTILE_SPEED,
                                                                      Constants.BLUE_PROJECTILE_DAMAGE,
                                                                      Constants.BLUE_PROJECTILE_COOLDOWN,
                                                                      Constants.BLUE_PROJECTILE_PASSES)
        self.blue_tower: AutomaticTower = AutomaticTower(Constants.BLUE_TOWER_POSITION, Constants.BLUE_TOWER_SURFACE,
                                                         self.blue_tower_projectile, ClosestTargeting())

    def __create_grey_tower(self):
        """
        This method creates a grey tower with its associated projectile
        """
        self.grey_tower_projectile: BasicProjectile = BasicProjectile(Position(0, 0),
                                                                      Constants.BLACK_PROJECTILE_SURFACE,
                                                                      DirectionVector(0, 0),
                                                                      Constants.BLACK_PROJECTILE_SPEED,
                                                                      Constants.BLACK_PROJECTILE_DAMAGE,
                                                                      Constants.BLACK_PROJECTILE_COOLDOWN)
        self.grey_tower: AutomaticTower = AutomaticTower(Constants.GREY_TOWER_POSITION, Constants.GREY_TOWER_SURFACE,
                                                         self.grey_tower_projectile, RandomTargeting())

    def apply_upgrade(self, upgrade: Upgrade):
        """
        This method applies the specified upgrade to the player's statistics.
        :param upgrade: Upgrade to apply to player's statistics
        """
        self.upgrades.apply_upgrade(upgrade)

        match upgrade:
            case Upgrade.BLACK_DMG:
                self.black_tower_projectile.damage += Constants.BLACK_PROJECTILE_DAMAGE_UPGRADE
            case Upgrade.BLACK_DMG2:
                self.black_tower_projectile.damage += Constants.BLACK_PROJECTILE_DAMAGE_UPGRADE
            case Upgrade.BLACK_AS:
                self.black_tower_projectile.cooldown -= Constants.BLACK_PROJECTILE_COOLDOWN_UPGRADE
            case Upgrade.BLACK_AS2:
                self.black_tower_projectile.cooldown -= Constants.BLACK_PROJECTILE_COOLDOWN_UPGRADE
            case Upgrade.RED_TWR:
                self.__create_red_tower()
            case Upgrade.RED_AS:
                self.red_tower_projectile.cooldown -= Constants.RED_PROJECTILE_COOLDOWN_UPGRADE
            case Upgrade.RED_DMG:
                self.red_tower_projectile.damage += Constants.RED_PROJECTILE_DAMAGE_UPGRADE
            case Upgrade.RED_RADIUS:
                self.red_tower_projectile.explosion_radius += Constants.RED_PROJECTILE_RADIUS_UPGRADE
            case Upgrade.RED_RADIUS2:
                self.red_tower_projectile.explosion_radius += Constants.RED_PROJECTILE_RADIUS_UPGRADE

            case Upgrade.GREEN_TWR:
                self.__create_green_tower()
            case Upgrade.GREEN_DMG:
                self.green_tower_projectile.damage += Constants.GREEN_PROJECTILE_DAMAGE_UPGRADE
            case Upgrade.GREEN_AS:
                self.green_tower_projectile.cooldown -= Constants.GREEN_PROJECTILE_COOLDOWN_UPGRADE
            case Upgrade.GREEN_BOUNCE:
                self.green_tower_projectile.bounce_count += Constants.GREEN_PROJECTILE_BOUNCES_UPGRADE
            case Upgrade.GREEN_BOUNCE2:
                self.green_tower_projectile.bounce_count += Constants.GREEN_PROJECTILE_BOUNCES_UPGRADE

            case Upgrade.BLUE_TWR:
                self.__create_blue_tower()
            case Upgrade.BLUE_DMG:
                self.blue_tower_projectile.damage += Constants.BLUE_PROJECTILE_DAMAGE_UPGRADE
            case Upgrade.BLUE_AS:
                self.blue_tower_projectile.cooldown -= Constants.BLUE_PROJECTILE_COOLDOWN_UPGRADE
            case Upgrade.BLUE_PASS:
                self.blue_tower_projectile.pass_through_count += Constants.BLUE_PROJECTILE_PASSES_UPGRADE
            case Upgrade.BLUE_PASS2:
                self.blue_tower_projectile.pass_through_count += Constants.BLUE_PROJECTILE_PASSES_UPGRADE

            case Upgrade.GREY_TWR:
                self.__create_grey_tower()

            case Upgrade.GREY_DMG:
                self.grey_tower_projectile.damage += Constants.BLACK_PROJECTILE_DAMAGE_UPGRADE
            case Upgrade.GREY_DMG2:
                self.grey_tower_projectile.damage += Constants.BLACK_PROJECTILE_DAMAGE_UPGRADE
            case Upgrade.GREY_AS:
                self.grey_tower_projectile.cooldown -= Constants.BLACK_PROJECTILE_COOLDOWN_UPGRADE
            case Upgrade.GREY_AS2:
                self.grey_tower_projectile.cooldown -= Constants.BLACK_PROJECTILE_COOLDOWN_UPGRADE
