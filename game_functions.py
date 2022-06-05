import numpy as np
import numpy.typing as np_typing

from game_classes import Board


def check_line(line: np_typing.ArrayLike) -> bool:
    """Placeholder docstring"""
    if np.all(np.equal(line, line[0])):  # checks if all the marks in the line are equal
        if line[0] == 0:  # since 0 represents an empty square
            return False
        elif line[0] in (1, 2):
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
    if check_line(game_board.state.diagonal()) or check_line(np.fliplr(game_board.state).diagonal()):
        return True

    return False  # if no complete lines are found
