import random
from typing import Tuple, Any

import numpy as np
import numpy.typing as np_typing

Coordinate = Tuple[int, int]


class Board:
    """A class representing a square game board. Empty squares are represented by a 0."""

    def __init__(self, size: int) -> None:
        """Placeholder docstring"""
        self.size: int = size
        self.state: np_typing.ArrayLike = np.zeros((self.size, self.size), dtype=int)

    def __str__(self) -> str:
        """Placeholder docstring"""
        return '\n'.join(['|'.join([str(mark) for mark in row]) for row in self.state])

    def is_occupied(self, coordinate: Coordinate) -> bool:
        """Placeholder docstring"""
        if self.state[coordinate[0]][coordinate[1]] == 0:
            return False
        else:
            return True

    def place_mark(self, move: Coordinate, active_mark: Any) -> None:
        """Catches out of range input"""
        try:
            if not self.is_occupied(move):
                self.state[move[0]][move[1]] = active_mark
            else:
                raise ValueError("Position is occupied")
        except ValueError as err:
            print(err)
            raise
        except IndexError:
            print("IndexError: Move is out of bounds")
            raise


class Player:
    """Base class for game players."""

    def __init__(self, name: str, symbol: int) -> None:
        self.name: str = name
        self.symbol: int = symbol

    # noinspection PyMethodMayBeStatic
    def make_move(self, board_size: int) -> Coordinate:
        return random.randrange(board_size), random.randrange(board_size)


class PlayerHuman(Player):
    """Class for human player who can choose a move themselves."""

    def make_move(self, board_size: int) -> Coordinate:
        try:
            # noinspection PyTypeChecker
            coordinate: Coordinate = tuple(map(int, input(f'Enter two integers within the bounds: ').split()))[:2]
            # taking tuple[:1] doesn't get the second element for some reason
            print(coordinate)
        except ValueError as err:
            raise ValueError("Integer inputs expected") from err

        return coordinate[1] - 1, coordinate[0] - 1  # converts from human convenient coordinates to flipped index 0
        # coordinates


class PlayerAI(Player):
    """Class for AI player who uses an algorithm to play."""
    pass
