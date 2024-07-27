# DEFENDER

![Screenshot ze hry](./media/game_gif.GIF)

## Game Description

Defender is a tower defence game in which the player controls a tower and shoots at enemies. After every completed round, the player can choose one of three possible upgrades. The upgrade either upgrades the player (his black tower), allows the player to build one of the automated towers, or upgrades those automated towers.

When the game starts, the player is informed about how the game is controlled (Controls window). The player is then taken to the MainMenu window, where they can choose the difficulty and start a new game or continue with the last saved game.

During the game, enemies come towards the player from the sides of the screen, and his task is to kill them with projectiles fired from his tower. After killing all the enemies, the player is presented with an Upgrade window where the player gets to choose between 3 upgrades.

For each completed round, the player's score increases. The score is further affected by the chosen difficulty. After completing a round (and selecting an upgrade), the game is always saved so the player can reload it after shutting it down.

There are four tower types in the game:

- Red - Fires projectiles that explode upon collision with the enemy and injure nearby enemies.
- Green - Fires projectiles that bounce towards another enemy after colliding.
- Blue - Fires projectiles that pass through enemies, allowing them to wound multiple enemies at once.
- Grey - Fires regular projectiles but fires them quickly.

All towers except the blue tower aim at random enemies. The blue tower aims at the nearest enemy.

There are also three types of enemies in the game, which, besides appearance, differ in the number of health points and movement speed.

Most of this game was developed in my personal repository - https://gitlab.fit.cvut.cz/machaj52/python-semestralka.

## Launch Description

### Dependencies

1, python3 - version at least 3.10 - `sudo apt install python3`

2, pygame ‒ `python3 -m pip install -U pygame --user`

### Running

1, Install the necessary dependencies

2, Download the directory from this repository

3, Run the game - `python3 -m <directory_name>`

### Testing

1, Install pytest - `pip install -U pytest`

2, Run the tests - `pytest <directory_name>` - Do not be startled by windows running while testing. Pygame requires you to run a window before loading images from directories.

3, Install pylint - `pip install -U pytest`

4, Run pylint - `pylint <directory_name> --disable=C0103,C0301,C0413,R0801,R0902,R0903,R0913`

## Used Graphic Assets

- Game background - https://cainos.itch.io/pixel-art-top-down-basic
- Towers - https://merchant-shade.itch.io/16x16-mini-world-sprites
- Enemies - https://anokolisa.itch.io/dungeon-crawler-pixel-art-asset-pack
- Game font - https://www.1001fonts.com/fff-forward-font.html
- Menu pointer - https://opengameart.org/content/rpg-gui-selection-arrow
