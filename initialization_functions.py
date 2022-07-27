from pygame_classes import GameWindow
from pygame_functions import get_game_window_size
from game_logic_classes import PlayerHuman, PlayerAI, Game
from game_logic_constants import Tile


def initialize_game_window(number_of_partitions):
    display_width, display_height = get_game_window_size()
    cell_width = display_width // number_of_partitions
    cell_height = display_height // number_of_partitions
    return GameWindow(display_width, display_height, cell_width, cell_height)


def initialize_game():
    player_a = PlayerHuman("Human", Tile.PLAYER_1)
    player_b = PlayerAI("AI", Tile.PLAYER_2)

    return Game(player_a, player_b)
