import numpy
import numpy.typing

from game_logic_classes import GameBoard
from game_logic_constants import Tile


def check_line_for_win(line: numpy.typing.ArrayLike) -> bool:
    """Placeholder docstring"""
    if numpy.all(numpy.equal(line, line[0])):  # checks if all the marks in the line are equal
        if line[0] == Tile.EMPTY:  # since 0 represents an empty square
            return False
        elif line[0] in (Tile.PLAYER_1, Tile.PLAYER_2):
            return True
        else:
            raise ValueError("Impossible symbol on board")


def is_win(game_board: GameBoard) -> bool:
    """Placeholder docstring"""
    # checks for completed rows or columns
    for i in range(game_board.size):
        if check_line_for_win(game_board.board[:, i]) or check_line_for_win(game_board.board[i, :]):
            return True

    # checks for completed diagonal or anti-diagonal
    if check_line_for_win(game_board.board.diagonal()) or check_line_for_win(numpy.fliplr(game_board.board).diagonal()):
        return True

    return False  # if no complete lines are found
