"""
This module tests the GameplayController class
"""
import pygame
import pytest
from pygame import Surface

from app.src.applicationcontroller.gameplay_controller import GameplayController
from app.src.enemy.enemy import Enemy
from app.src.projectile.basic_projectile import BasicProjectile
from app.src.projectile.bouncing_projectile import BouncingProjectile
from app.src.projectile.explosive_projectile import ExplosiveProjectile
from app.src.projectile.ghost_projectile import GhostProjectile
from app.src.tower.automatic_tower import AutomaticTower
from app.src.tower.manual_tower import ManualTower
from app.utils.constants import Constants
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position
from app.utils.upgrade import Upgrade


def constants_fixture() -> GameplayController:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    gameplay_controller: GameplayController = GameplayController(screen)
    return gameplay_controller


def test_process_input1():
    """
    This function tests the process_input() method of the GameplayController class
    """
    gameplay_controller: GameplayController = constants_fixture()

    pygame.event.clear()
    pygame.event.post(pygame.event.Event(pygame.QUIT))

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        gameplay_controller.process_input()
    assert pytest_wrapped_e.type == SystemExit


def test_process_input2():
    """
    This function tests the process_input() method of the GameplayController class
    """
    gameplay_controller: GameplayController = constants_fixture()

    pygame.event.clear()
    gameplay_controller.player_info.black_tower.cooldown = 0
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))

    assert len(gameplay_controller.basic_projectiles_group) == 0

    gameplay_controller.process_input()

    assert len(gameplay_controller.basic_projectiles_group) == 1

    pygame.event.clear()
    gameplay_controller.player_info.black_tower.cooldown = 1000
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))

    gameplay_controller.process_input()

    assert len(gameplay_controller.basic_projectiles_group) == 1


def test_process_input3():
    """
    This function tests the process_input() method of the GameplayController class
    """
    gameplay_controller: GameplayController = constants_fixture()

    gameplay_controller.running = True

    pygame.event.clear()
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))

    gameplay_controller.process_input()

    assert gameplay_controller.running is False


def test_update_game1():
    """
    This function tests the update_game() method of the GameplayController class
    """
    gameplay_controller: GameplayController = constants_fixture()

    basic_surface: Surface = Constants.BLACK_PROJECTILE_SURFACE

    basic_projectile: BasicProjectile = BasicProjectile(Position(0, 0), basic_surface, DirectionVector(1, 0), 1, 0, 0)
    explosive_projectile: ExplosiveProjectile = ExplosiveProjectile(Position(0, 0), basic_surface,
                                                                    DirectionVector(0, 1), 1, 0, 0, 0)
    bouncing_projectile: BouncingProjectile = BouncingProjectile(Position(0, 0), basic_surface, DirectionVector(-1, 0),
                                                                 1, 0, 0, 0)
    ghost_projectile: GhostProjectile = GhostProjectile(Position(0, 0), basic_surface, DirectionVector(0, -1), 1, 0, 0,
                                                        0)

    enemy_1: Enemy = Enemy(10, Position(500, 500), basic_surface, DirectionVector(1, 0), 1)
    enemy_2: Enemy = Enemy(10, Position(-500, -500), basic_surface, DirectionVector(0, -1), 1)

    gameplay_controller.basic_projectiles_group.add(basic_projectile)
    gameplay_controller.explosive_projectiles_group.add(explosive_projectile)
    gameplay_controller.bouncing_projectiles_group.add(bouncing_projectile)
    gameplay_controller.ghost_projectiles_group.add(ghost_projectile)
    gameplay_controller.enemies_group.add(enemy_1)
    gameplay_controller.enemies_group.add(enemy_2)

    gameplay_controller.update_game()

    assert basic_projectile.position.xCoord == 1
    assert basic_projectile.position.yCoord == 0
    assert explosive_projectile.position.xCoord == 0
    assert explosive_projectile.position.yCoord == 1
    assert bouncing_projectile.position.xCoord == -1
    assert bouncing_projectile.position.yCoord == 0
    assert ghost_projectile.position.xCoord == 0
    assert ghost_projectile.position.yCoord == -1
    assert enemy_1.position.xCoord == 501
    assert enemy_1.position.yCoord == 500
    assert enemy_2.position.xCoord == -500
    assert enemy_2.position.yCoord == -501


def test_update_game2():
    """
    This function tests the update_game() method of the GameplayController class
    """
    gameplay_controller: GameplayController = constants_fixture()
    basic_surface: Surface = Constants.BLACK_PROJECTILE_SURFACE

    basic_projectile: BasicProjectile = BasicProjectile(Position(0, 0), basic_surface, DirectionVector(1, 0), 10000, 0,
                                                        0)
    explosive_projectile: ExplosiveProjectile = ExplosiveProjectile(Position(0, 0), basic_surface,
                                                                    DirectionVector(0, 1), 10000, 0, 0, 0)
    bouncing_projectile: BouncingProjectile = BouncingProjectile(Position(0, 0), basic_surface, DirectionVector(-1, 0),
                                                                 10000, 0, 0, 0)
    ghost_projectile: GhostProjectile = GhostProjectile(Position(0, 0), basic_surface, DirectionVector(0, -1), 10000, 0,
                                                        0, 0)

    gameplay_controller.basic_projectiles_group.add(basic_projectile)
    gameplay_controller.explosive_projectiles_group.add(explosive_projectile)
    gameplay_controller.bouncing_projectiles_group.add(bouncing_projectile)
    gameplay_controller.ghost_projectiles_group.add(ghost_projectile)

    assert len(gameplay_controller.basic_projectiles_group) == 1
    assert len(gameplay_controller.explosive_projectiles_group) == 1
    assert len(gameplay_controller.bouncing_projectiles_group) == 1
    assert len(gameplay_controller.ghost_projectiles_group) == 1

    gameplay_controller.update_game()

    assert len(gameplay_controller.basic_projectiles_group) == 0
    assert len(gameplay_controller.explosive_projectiles_group) == 0
    assert len(gameplay_controller.bouncing_projectiles_group) == 0
    assert len(gameplay_controller.ghost_projectiles_group) == 0


def test_update_game3():
    """
    This function tests the update_game() method of the GameplayController class
    """
    gameplay_controller: GameplayController = constants_fixture()
    basic_surface: Surface = Constants.BLACK_PROJECTILE_SURFACE

    basic_projectile: BasicProjectile = BasicProjectile(Position(100, 50), basic_surface, DirectionVector(1, 0), 1, 1, 0)
    explosive_projectile: ExplosiveProjectile = ExplosiveProjectile(Position(250, 50), basic_surface, DirectionVector(1, 0), 1, 5, 0, 10)
    bouncing_projectile: BouncingProjectile = BouncingProjectile(Position(450, 50), basic_surface, DirectionVector(1, 0), 1, 3, 0, 10)
    ghost_projectile: GhostProjectile = GhostProjectile(Position(600, 50), basic_surface, DirectionVector(1, 0), 1, 5, 0, 20)

    enemy_1: Enemy = Enemy(2, Position(101, 50), basic_surface, DirectionVector(1, 0), 0)
    enemy_2: Enemy = Enemy(2, Position(251, 50), basic_surface, DirectionVector(1, 0), 0)
    enemy_3: Enemy = Enemy(2, Position(252, 50), basic_surface, DirectionVector(1, 0), 0)
    enemy_4: Enemy = Enemy(2, Position(451, 50), basic_surface, DirectionVector(1, 0), 0)
    enemy_5: Enemy = Enemy(2, Position(601, 50), basic_surface, DirectionVector(1, 0), 0)

    gameplay_controller.basic_projectiles_group.add(basic_projectile)
    gameplay_controller.explosive_projectiles_group.add(explosive_projectile)
    gameplay_controller.bouncing_projectiles_group.add(bouncing_projectile)
    gameplay_controller.ghost_projectiles_group.add(ghost_projectile)
    gameplay_controller.enemies_group.add(enemy_1)
    gameplay_controller.enemies_group.add(enemy_2)
    gameplay_controller.enemies_group.add(enemy_3)
    gameplay_controller.enemies_group.add(enemy_4)
    gameplay_controller.enemies_group.add(enemy_5)

    assert len(gameplay_controller.basic_projectiles_group) == 1
    assert len(gameplay_controller.explosive_projectiles_group) == 1
    assert len(gameplay_controller.bouncing_projectiles_group) == 1
    assert len(gameplay_controller.ghost_projectiles_group) == 1
    assert len(gameplay_controller.enemies_group) == 5

    gameplay_controller.update_game()

    assert len(gameplay_controller.basic_projectiles_group) == 0
    assert enemy_1 in gameplay_controller.enemies_group
    assert len(gameplay_controller.explosive_projectiles_group) == 0
    assert enemy_2 not in gameplay_controller.enemies_group
    assert enemy_3 not in gameplay_controller.enemies_group
    assert len(gameplay_controller.bouncing_projectiles_group) == 1
    assert enemy_4 not in gameplay_controller.enemies_group
    assert len(gameplay_controller.ghost_projectiles_group) == 1
    assert enemy_5 not in gameplay_controller.enemies_group
    assert len(gameplay_controller.enemies_group) == 1


def test_update_game4():
    """
    This function tests the update_game() method of the GameplayController class
    """
    gameplay_controller: GameplayController = constants_fixture()
    basic_surface: Surface = Constants.BLACK_PROJECTILE_SURFACE

    gameplay_controller.player_info.apply_upgrade(Upgrade.RED_TWR)
    gameplay_controller.player_info.apply_upgrade(Upgrade.GREEN_TWR)
    gameplay_controller.player_info.apply_upgrade(Upgrade.BLUE_TWR)
    gameplay_controller.player_info.apply_upgrade(Upgrade.GREY_TWR)

    player_tower: ManualTower = gameplay_controller.player_info.black_tower
    red_tower: AutomaticTower = gameplay_controller.player_info.red_tower
    green_tower: AutomaticTower = gameplay_controller.player_info.green_tower
    blue_tower: AutomaticTower = gameplay_controller.player_info.blue_tower
    grey_tower: AutomaticTower = gameplay_controller.player_info.grey_tower

    gameplay_controller.explosive_tower_group.add(red_tower)
    gameplay_controller.bouncing_tower_group.add(green_tower)
    gameplay_controller.ghost_tower_group.add(blue_tower)
    gameplay_controller.basic_tower_group.add(grey_tower)

    enemy_1: Enemy = Enemy(2, Position(601, 50), basic_surface, DirectionVector(1, 0), 0)
    gameplay_controller.enemies_group.add(enemy_1)

    old_black_value = 1000
    old_red_value = 8000
    old_green_value = 50
    old_blue_value = 123456
    old_grey_value = 0

    player_tower.cooldown = old_black_value
    red_tower.cooldown = old_red_value
    green_tower.cooldown = old_green_value
    blue_tower.cooldown = old_blue_value
    grey_tower.cooldown = old_grey_value

    gameplay_controller.ticks = 20
    gameplay_controller.update_game()

    assert red_tower.cooldown < old_red_value
    assert green_tower.cooldown < old_green_value
    assert blue_tower.cooldown < old_blue_value
    assert grey_tower.cooldown > old_grey_value
    assert gameplay_controller.player_info.black_tower.cooldown < old_black_value


def test_update_game5():
    """
    This function tests the update_game() method of the GameplayController class
    """
    gameplay_controller: GameplayController = constants_fixture()

    gameplay_controller.enemies_left_count = 0
    gameplay_controller.starting_round = True

    gameplay_controller.update_game()

    assert gameplay_controller.enemies_left_count != 0
    assert gameplay_controller.starting_round is not True
