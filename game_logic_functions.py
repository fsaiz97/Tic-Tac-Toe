import numpy
import numpy.typing

from game_logic_classes import Board
from game_logic_constants import Tile


def check_line(line: numpy.typing.ArrayLike) -> bool:
    """Placeholder docstring"""
    if numpy.all(numpy.equal(line, line[0])):  # checks if all the marks in the line are equal
        if line[0] == Tile.EMPTY:  # since 0 represents an empty square
            return False
        elif line[0] in (Tile.PLAYER_1, Tile.PLAYER_2):
            return True
        else:
            raise ValueError("Impossible symbol on board")


def is_win(game_board: Board) -> bool:
    """Placeholder docstring"""
    # checks for completed rows or columns
    for i in range(game_board.size):
        if check_line(game_board.state[:, i]) or check_line(game_board.state[i, :]):
            return True

    # checks for completed diagonal or anti-diagonal
    if check_line(game_board.state.diagonal()) or check_line(numpy.fliplr(game_board.state).diagonal()):
        return True

    return False  # if no complete lines are found
