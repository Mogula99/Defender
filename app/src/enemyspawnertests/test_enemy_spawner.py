"""
This module tests the EnemySpawner class
"""
import pygame
from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.enemyspawner.enemy_spawner import EnemySpawner
from app.utils.constants import Constants
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


def constants_fixture() -> Surface:
    """
    This function makes all the necessary preparations so that the tests can proceed.
    It was previously a fixture, but Pylint didn't like that very much
    """
    pygame.init()
    screen: Surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Constants.load_media()
    return screen


def test_spawn_enemies():
    """
    This function tests the spawn_enemies() method of the EnemySpawner class
    """
    screen: Surface = constants_fixture()
    player_position: Position = Position(0, 0)
    round_number: int = 25
    enemy_spawner: EnemySpawner = EnemySpawner()

    expected_enemies_count: int = Constants.BASE_ENEMIES_CNT + (2 * Constants.DIFFICULTY_MODIFIER) + (round_number * (4 + Constants.DIFFICULTY_MODIFIER))

    enemies: list[Enemy] = enemy_spawner.spawn_enemies(screen, player_position, round_number)

    assert len(enemies) == expected_enemies_count

    expected_boss_enemies = expected_enemies_count // 10
    expected_normal_enemies = expected_enemies_count // 5
    expected_easy_enemies = expected_enemies_count - expected_boss_enemies - expected_normal_enemies

    easy_enemies_cnt: int = 0
    normal_enemies_cnt: int = 0
    boss_enemies_cnt: int = 0
    for enemy in enemies:
        assert not enemy.rect.colliderect(screen.get_rect())
        assert enemy.direction.xCoord == DirectionVector.create_vector(enemy.position, player_position).xCoord
        assert enemy.direction.yCoord == DirectionVector.create_vector(enemy.position, player_position).yCoord

        if enemy.image == Constants.BOSS_ENEMY_SURFACES[0]:
            boss_enemies_cnt += 1
        elif enemy.image == Constants.NORMAL_ENEMY_SURFACES[0]:
            normal_enemies_cnt += 1
        else:
            easy_enemies_cnt += 1

    assert easy_enemies_cnt == expected_easy_enemies
    assert normal_enemies_cnt == expected_normal_enemies
    assert boss_enemies_cnt == expected_boss_enemies
