import random
from typing import Tuple, Any

import numpy
import numpy.typing

from game_logic_constants import Tile

Coordinate = Tuple[int, int]


class GameBoard:
    """A class representing a square game board. Empty squares are represented by a 0."""

    def __init__(self, size: int) -> None:
        """Placeholder docstring"""
        self.size: int = size
        self.board: numpy.typing.ArrayLike = numpy.full((self.size, self.size), Tile.EMPTY, dtype=object)

    def __str__(self) -> str:
        """Placeholder docstring"""
        return '\n'.join(['|'.join([str(mark) for mark in row]) for row in self.board])

    def is_occupied(self, coordinate: Coordinate) -> bool:
        """Placeholder docstring"""
        return not self.board[coordinate[0]][coordinate[1]] == Tile.EMPTY

    def place_symbol(self, move: Coordinate, active_symbol: Any) -> None:
        """Catches out of range input"""
        try:
            if not self.is_occupied(move):
                self.board[move[0]][move[1]] = active_symbol
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

    def __init__(self, name: str, symbol: Tile) -> None:
        self.name: str = name
        self.symbol: Tile = symbol

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
