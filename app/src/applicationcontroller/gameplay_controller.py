"""
This module defines GameplayController which is responsible for everything connected with main game window.
"""
import sys

import pygame
from pygame import Surface
from pygame.sprite import Group, Sprite, GroupSingle

from app.gui.text.text import Text
from app.src.applicationcontroller.application_controller import ApplicationController
from app.src.applicationcontroller.menucontroller.game_over_window_controller import GameOverWindowController
from app.src.applicationcontroller.menucontroller.upgrade_window_controller import UpgradeWindowController
from app.src.enemy.enemy import Enemy
from app.src.enemyspawner.enemy_spawner import EnemySpawner
from app.src.gameobject.gameobject import GameObject
from app.src.playerinfo.player_info import PlayerInfo
from app.src.projectile.basic_projectile import BasicProjectile
from app.src.projectile.bouncing_projectile import BouncingProjectile
from app.src.projectile.explosive_projectile import ExplosiveProjectile
from app.src.projectile.ghost_projectile import GhostProjectile
from app.src.projectile.projectile import Projectile
from app.src.savefilemanager.save_file_info import SaveFileInfo
from app.src.savefilemanager.save_file_manager import SaveFileManager
from app.src.tower.automatic_tower import AutomaticTower
from app.src.tower.manual_tower import ManualTower
from app.src.visualeffect.visual_effect import VisualEffect
from app.utils.constants import Constants
from app.utils.position import Position


class GameplayController(ApplicationController):
    """
    This class is responsible for rendering object in the main game window.
    It also contains all the most important game logic.
    It takes player input, updates all the objects on the window and renders them again.
    """
    def __init__(self, screen: Surface, player_info: PlayerInfo = None, round_number: int = 1):
        """
        Constructor of the GameplayController class
        :param screen: Screen that is used to render the window
        :param player_info: Information about the current player
        :param round_number: Number of the round that should be started
        """
        # Texts in the current window
        self.remaining_health_text: Text = Text.create_text(Constants.GAMEPLAY_HEALTH_TEXT,
                                                            Constants.FIRST_VALUE_POSITION,
                                                            Constants.GAMEPLAY_TEXT_COLOR)
        self.current_score_text: Text = Text.create_text(Constants.GAMEPLAY_SCORE_TEXT, Constants.SECOND_VALUE_POSITION,
                                                         Constants.GAMEPLAY_TEXT_COLOR)
        self.current_round_text: Text = Text.create_text(Constants.GAMEPLAY_ROUND_TEXT, Constants.THIRD_VALUE_POSITION,
                                                         Constants.GAMEPLAY_TEXT_COLOR)
        self.enemies_left_text: Text = Text.create_text(Constants.GAMEPLAY_ENEMIES_LEFT_TEXT,
                                                        Constants.FOURTH_VALUE_POSITION, Constants.GAMEPLAY_TEXT_COLOR)
        texts: list[Text] = [self.remaining_health_text, self.current_score_text, self.current_round_text,
                             self.enemies_left_text]

        ApplicationController.__init__(self, screen, texts)

        # class variables initialization
        self.current_score: int = 0
        self.round_number: int = round_number
        self.enemies_left_count: int = 0

        self.enemy_spawner: EnemySpawner = EnemySpawner()

        # pygame groups used in the current window
        self.player_group: GroupSingle[ManualTower] = pygame.sprite.GroupSingle()

        self.explosive_tower_group: GroupSingle[AutomaticTower] = pygame.sprite.GroupSingle()
        self.bouncing_tower_group: GroupSingle[AutomaticTower] = pygame.sprite.GroupSingle()
        self.ghost_tower_group: GroupSingle[AutomaticTower] = pygame.sprite.GroupSingle()
        self.basic_tower_group: GroupSingle[AutomaticTower] = pygame.sprite.GroupSingle()

        self.explosive_projectiles_group: Group[ExplosiveProjectile] = pygame.sprite.Group()
        self.bouncing_projectiles_group: Group[BouncingProjectile] = pygame.sprite.Group()
        self.ghost_projectiles_group: Group[GhostProjectile] = pygame.sprite.Group()
        self.basic_projectiles_group: Group[BasicProjectile] = pygame.sprite.Group()

        if player_info is None:
            self.player_info = PlayerInfo()
        else:
            self.player_info = player_info
            self.__update_score(self.round_number - 1)
        self.__refresh_towers()

        self.enemies_group: Group[Enemy] = pygame.sprite.Group()

        # making the texts show current values
        self.remaining_health_text.refresh_text(Constants.GAMEPLAY_HEALTH_TEXT + str(self.player_info.player_health))
        self.current_score_text.refresh_text(Constants.GAMEPLAY_SCORE_TEXT + str(self.current_score))
        self.current_round_text.refresh_text(Constants.GAMEPLAY_ROUND_TEXT + str(self.round_number))
        self.enemies_left_text.refresh_text(Constants.GAMEPLAY_ENEMIES_LEFT_TEXT + str(self.enemies_left_count))

        self.player_group.add(self.player_info.black_tower)

        self.ticks: int = pygame.time.get_ticks()

        self.starting_round: bool = True

        self.save_manager: SaveFileManager = SaveFileManager()

        self.visual_effects_group: Group[VisualEffect] = pygame.sprite.Group()

    def process_input(self):
        """
        Method responsible for handling the player's input
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Player has clicked somewhere in the window screen
                if self.player_info.black_tower.cooldown <= 0:
                    mouse_click_position: Position = Position(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    projectile: Projectile = self.player_info.black_tower.shoot(mouse_click_position)
                    self.basic_projectiles_group.add(projectile)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running: bool = False

    def update_game(self):
        """
        Method the updates all the objects that change while the current window is on
        """
        groups_to_update: list[Group[GameObject]] = [self.basic_projectiles_group, self.enemies_group,
                                                     self.explosive_projectiles_group, self.bouncing_projectiles_group,
                                                     self.ghost_projectiles_group, self.visual_effects_group]

        # Update the positions of all the moving objects on the screen
        for group in groups_to_update:
            group.update()

        self.__check_out_of_bounds()
        self.__check_collisions()
        self.__update_cooldown()
        self.__fire_towers()
        self.__check_finished_visual_effects()

        # Handle the situation when there are no more enemies in the current round
        self.__update_enemies_count(len(self.enemies_group))
        if self.enemies_left_count == 0:
            if not self.starting_round:
                if len(self.player_info.upgrades.available) != 0:
                    self.__offer_upgrade()
                self.__update_score(self.round_number)
                self.__update_round(self.round_number + 1)
                self.__save_game()
                print("Game saved")
            self.__start_round()
            self.starting_round: bool = False

    def __update_round(self, new_amount: int):
        """
        This method updates the current round to a new value
        :param new_amount: New round_number value
        """
        self.round_number: int = new_amount
        self.current_round_text.refresh_text(Constants.GAMEPLAY_ROUND_TEXT + str(self.round_number))

    def __update_score(self, last_completed_round: int):
        """
        This method updates the current score to a new value
        :param last_completed_round: New value for the current_score variable
        """
        self.current_score: int = last_completed_round * Constants.DIFFICULTY_MODIFIER
        self.current_score_text.refresh_text(Constants.GAMEPLAY_SCORE_TEXT + str(self.current_score))
        if self.current_score > Constants.BEST_SCORE:
            Constants.BEST_SCORE = self.current_score

    def __update_enemies_count(self, new_count: int):
        """
        This method updates the current count of the enemies on the screen to a new value
        :param new_count: New value for the enemies_left_count variable
        """
        self.enemies_left_count: int = new_count
        self.enemies_left_text.refresh_text(Constants.GAMEPLAY_ENEMIES_LEFT_TEXT + str(self.enemies_left_count))

    def __update_player_health(self, new_amount: int):
        """
        This method updates the current health points of the player to a new value
        :param new_amount: New value of the player_health variable
        :return:
        """
        self.player_info.receive_damage(self.player_info.player_health - new_amount)
        self.remaining_health_text.refresh_text(Constants.GAMEPLAY_HEALTH_TEXT + str(self.player_info.player_health))

    def __save_game(self):
        """
        This method saves the current game
        """
        save_file_info: SaveFileInfo = SaveFileInfo(self.round_number, Constants.DIFFICULTY_MODIFIER,
                                                    self.player_info.player_health, self.player_info.upgrades.bought,
                                                    Constants.BEST_SCORE)
        self.save_manager.save_game(save_file_info)

    def __offer_upgrade(self):
        """
        This method launches the upgrade window which will offer 3 upgrades for the player
        """
        upgrade_window_controller: UpgradeWindowController = UpgradeWindowController(self.screen, self.player_info)
        upgrade_window_controller.run()
        self.__refresh_towers()

        # So that the cooldown of towers will not decrease by the time spent choosing upgrades
        self.ticks: int = pygame.time.get_ticks()

    def __start_round(self):
        """
        This method spawns new enemies on the start of the round
        """
        current_enemies: list[Enemy] = self.enemy_spawner.spawn_enemies(self.screen, self.player_info.black_tower.position,
                                                                        self.round_number)
        self.__update_enemies_count(len(current_enemies))
        for x in current_enemies:
            self.enemies_group.add(x)
        print("Round", self.round_number)

    def render_objects(self):
        """
        This method is responsible for drawing all the object on the current screen.
        Object to render are grouped up into groups that are being iterated over and drawn.
        """
        self.screen.blit(Constants.BACKGROUND_SURFACE, (0, 0))
        groups_to_draw: list[Group[Sprite]] = [self.player_group, self.enemies_group,
                                               self.explosive_projectiles_group, self.bouncing_projectiles_group,
                                               self.ghost_projectiles_group, self.basic_projectiles_group,
                                               self.explosive_tower_group, self.bouncing_tower_group,
                                               self.ghost_tower_group, self.basic_tower_group, self.visual_effects_group,
                                               self.texts_group]

        # draw all the objects on the screen
        for group in groups_to_draw:
            group.draw(self.screen)

        pygame.display.flip()

    def __check_out_of_bounds(self):
        """
        This method checks if all the projectiles are on the current screen and if they're not, they are destroyed.
        """
        projectile_groups: list[Group[Projectile]] = [self.basic_projectiles_group, self.explosive_projectiles_group,
                                                      self.bouncing_projectiles_group, self.ghost_projectiles_group]

        # Delete out-of-bounds projectiles
        for group in projectile_groups:
            for projectile in group:
                if not self.screen.get_rect().collidepoint(projectile.rect.center):
                    group.remove(projectile)

    def __check_collisions(self):
        """
        This method checks for collision between projectiles and enemies but also for collision between the enemies and the player's tower.
        """
        projectile_groups: list[Group[Projectile]] = [self.explosive_projectiles_group, self.bouncing_projectiles_group,
                                                      self.ghost_projectiles_group, self.basic_projectiles_group]

        # Check all the collision between projectiles and enemies
        for projectile_group in projectile_groups:
            for projectile in projectile_group:
                for enemy in self.enemies_group:
                    if enemy.rect.colliderect(projectile.rect):
                        # Not that great projectile polymorphism saved a lot of code repetition in this method
                        projectile.apply_special_ability(enemy, self.enemies_group, self.visual_effects_group)
                        self.__check_enemy_health(enemy)
                        if projectile.should_destroy():
                            projectile_group.remove(projectile)

        for enemy in self.enemies_group:
            self.__check_enemy_health(enemy)

        # Check collision of the enemies with the player
        for enemy in self.enemies_group:
            if enemy.rect.colliderect(self.player_info.black_tower.rect):
                self.__update_player_health(self.player_info.player_health - enemy.health)
                if self.player_info.player_health <= 0:
                    game_over_controller = GameOverWindowController(self.screen)
                    game_over_controller.run()
                    self.running: bool = False
                self.enemies_group.remove(enemy)
                continue

    def __check_enemy_health(self, enemy: Enemy):
        """
        This method checks the health of the enemy and destroys it if the health is lower than 0
        :param enemy: Enemy that should have its health points checked
        """
        if enemy.health <= 0:
            self.enemies_group.remove(enemy)
            self.__update_enemies_count(self.enemies_left_count - 1)

    def __update_cooldown(self):
        """
        This method updates cooldowns of all the towers
        """
        current_ticks: int = pygame.time.get_ticks()
        delta_time: int = current_ticks - self.ticks
        self.ticks: int = current_ticks

        # update cooldowns of all the automatic towers
        for tower in self.__get_all_automatic_towers():
            if tower.cooldown > 0:
                tower.reduce_cooldown(delta_time)

        # update cooldown of the player's tower
        if self.player_info.black_tower.cooldown > 0:
            self.player_info.black_tower.reduce_cooldown(delta_time)

        # set cursor when waiting for cooldown
        if self.player_info.black_tower.cooldown > 20:
            pygame.mouse.set_cursor(pygame.cursors.diamond)
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)

    def __get_all_automatic_towers(self) -> list[AutomaticTower]:
        """
        This method just returns a list of all the towers that are not operated by the player
        :return: List of all the towers that are not operated by the player
        """
        towers: list[AutomaticTower] = []
        for tower in self.explosive_tower_group.sprites():
            towers.append(tower)
        for tower in self.bouncing_tower_group.sprites():
            towers.append(tower)
        for tower in self.ghost_tower_group.sprites():
            towers.append(tower)
        for tower in self.basic_tower_group.sprites():
            towers.append(tower)
        return towers

    def __refresh_towers(self):
        """
        This method makes sure that all the towers are present in their respective groups
        """
        self.__refresh_tower(self.player_info.red_tower, self.explosive_tower_group)
        self.__refresh_tower(self.player_info.green_tower, self.bouncing_tower_group)
        self.__refresh_tower(self.player_info.blue_tower, self.ghost_tower_group)
        self.__refresh_tower(self.player_info.grey_tower, self.basic_tower_group)

    def __refresh_tower(self, tower: AutomaticTower, tower_group: GroupSingle):
        """
        This method makes sure that the specified tower is present in its respective group
        :param tower: Tower to check
        :param tower_group: Group that is associated with the tower
        """
        if tower not in tower_group and tower is not None:
            tower_group.add(tower)

    def __fire_towers(self):
        """
        This method tries to fire all the towers that are not operated by the player
        """
        self.__fire_tower(self.explosive_tower_group, self.explosive_projectiles_group)
        self.__fire_tower(self.bouncing_tower_group, self.bouncing_projectiles_group)
        self.__fire_tower(self.ghost_tower_group, self.ghost_projectiles_group)
        self.__fire_tower(self.basic_tower_group, self.basic_projectiles_group)

    def __fire_tower(self, tower_group: GroupSingle, projectile_group: Group):
        """
        This method tries to fire all towers in a specified group. If the tower's cooldown is lower than 0, it will fire.
        :param tower_group: Group of all the towers that should fire
        :param projectile_group: Group of projectiles of the same type as the one fired by specified tower_group
        """
        for tower in tower_group:
            if tower.cooldown <= 0:
                fired_projectile: Projectile = tower.auto_fire(self.enemies_group.sprites())
                if fired_projectile is not None:
                    projectile_group.add(fired_projectile)

    def __check_finished_visual_effects(self):
        for visual_effect in self.visual_effects_group:
            if not visual_effect.is_active:
                self.visual_effects_group.remove(visual_effect)
