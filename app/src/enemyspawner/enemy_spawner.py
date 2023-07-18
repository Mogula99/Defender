"""
This module defines the EnemySpawner class
"""
import random

from pygame import Surface

from app.src.enemy.enemy import Enemy
from app.src.enemy.enemy_template import EnemyTemplate
from app.utils.constants import Constants
from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


class EnemySpawner:
    """
    This class is responsible for spawning all the enemies in the game. The number of enemies increases with every round.
    """
    def __init__(self):
        """
        Constructor of the EnemySpawner class
        """
        self.easy_enemy_template: EnemyTemplate = EnemyTemplate(Constants.EASY_ENEMY_HEALTH, Constants.EASY_ENEMY_SURFACE, Constants.EASY_ENEMY_SPEED)
        self.normal_enemy_template: EnemyTemplate = EnemyTemplate(Constants.NORMAL_ENEMY_HEALTH, Constants.NORMAL_ENEMY_SURFACE, Constants.NORMAL_ENEMY_SPEED)
        self.boss_enemy_template: EnemyTemplate = EnemyTemplate(Constants.BOSS_ENEMY_HEALTH, Constants.BOSS_ENEMY_SURFACE, Constants.BOSS_ENEMY_SPEED)
        self.screen_offset_increase: int = 100

    def __count_enemies(self, round_number: int) -> int:
        """
        Method that returns a number of enemies that should be present in the specified round.
        :param round_number: Round for which the number of enemies should be counter
        :return: Number of enemies in the specified round
        """
        return Constants.BASE_ENEMIES_CNT + (2 * Constants.DIFFICULTY_MODIFIER) + (round_number * (4 + Constants.DIFFICULTY_MODIFIER))

    def __count_increase_offset_change(self, enemies_on_the_offset: int) -> float:
        """
        Method that counts the chance that the offset will be increase with the next enemy spawned
        :param enemies_on_the_offset: Number of enemies that have already been spawned on this offset
        :return: Chance of increasing offset this time
        """
        increase_offset_chance: float = (0.20 - (0.03 * Constants.DIFFICULTY_MODIFIER)) + (0.01 * enemies_on_the_offset)
        return increase_offset_chance

    def spawn_enemies(self, screen: Surface, player_position: Position, round_number: int) -> list[Enemy]:
        """
        This method creates enemies on random locations around the screen and returns a list of them
        :param screen: Screen that is used to render the game
        :param player_position: Position of the player's tower
        :param round_number: Round for which the enemies should be spawned
        :return: List of spawned enemies
        """
        # counts numbers of different enemies
        enemies_to_spawn: int = self.__count_enemies(round_number)
        boss_enemies_to_spawn: int = enemies_to_spawn // 10
        normal_enemies_to_spawn: int = enemies_to_spawn // 5

        # Distance saying how far away from the screen the enemy should be spawned. It will increase when the enemies will spawn
        screen_offset: int = 50
        enemies_on_this_offset: int = 0

        spawned_enemies: list[Enemy] = []

        for enemy_index in range(enemies_to_spawn):
            # Find a random position for enemy
            enemy_position: Position = self.__create_spawn_position(screen_offset, screen.get_width(), screen.get_height())

            # From time to time increase the offset
            should_increase: float = random.random()
            if should_increase <= self.__count_increase_offset_change(enemies_on_this_offset):
                screen_offset += self.screen_offset_increase
                enemies_on_this_offset: int = 0
            else:
                enemies_on_this_offset += 1

            # Create the new enemy
            enemy_direction: DirectionVector = DirectionVector.create_vector(enemy_position, player_position)
            if enemy_index < boss_enemies_to_spawn:
                enemy: Enemy = self.boss_enemy_template.create_enemy(enemy_position, enemy_direction)
            elif enemy_index < boss_enemies_to_spawn + normal_enemies_to_spawn:
                enemy: Enemy = self.normal_enemy_template.create_enemy(enemy_position, enemy_direction)
            else:
                enemy: Enemy = self.easy_enemy_template.create_enemy(enemy_position, enemy_direction)
            spawned_enemies.append(enemy)

        return spawned_enemies

    def __create_spawn_position(self, screen_offset: int, screen_width: int, screen_height: int) -> Position:
        """
        This method creates a spawn position of an enemy
        :param screen_offset: Distance saying how far away from the screen the enemy should be spawned
        :param screen_width: The width of the screen
        :param screen_height: The height of the screen
        :return: New random position for the enemy
        """
        # On which side of the screen the enemy should be spawned
        random_side: int = random.randint(0, 3)
        # 0 - left
        # 1 - bottom
        # 2 - right
        # 3 - top

        if random_side == 0:
            spawn_x: int = 0 - screen_offset
            spawn_y: int = random.randint(0 - screen_offset, screen_height + screen_offset)
        elif random_side == 1:
            spawn_x: int = random.randint(0 - screen_offset, screen_width + screen_offset)
            spawn_y: int = screen_height + screen_offset
        elif random_side == 2:
            spawn_x: int = screen_width + screen_offset
            spawn_y: int = random.randint(0 - screen_offset, screen_height + screen_offset)
        else:
            spawn_x: int = random.randint(0 - screen_offset, screen_width + screen_offset)
            spawn_y: int = 0 - screen_offset

        return Position(spawn_x, spawn_y)
