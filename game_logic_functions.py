import numpy
import numpy.typing

from game_logic_classes import GameBoard
from game_logic_constants import Tile


def get_game_window_size():
    display_width = 600
    display_height = 600

    return display_width, display_height


def is_line_empty(line_element):
    return line_element == Tile.EMPTY


def is_line_win(line: numpy.typing.ArrayLike) -> bool:
    """Placeholder docstring"""
    if numpy.all(numpy.equal(line, line[0])):  # checks if all the marks in the line are equal
        return not is_line_empty(line[0])


def is_win(game_board: GameBoard) -> bool:
    """Placeholder docstring"""

    for line in game_board.get_lines():
        if is_line_win(line):
            return True

    return False  # if no complete lines are found
