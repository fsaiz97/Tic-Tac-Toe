from enum import Enum


class Tile(Enum):
    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2


BOARD_SIZE = 3  # sets number of rows and columns for the game board
