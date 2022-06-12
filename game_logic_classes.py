import random
from typing import Any

import numpy
import numpy.typing

from game_logic_constants import Tile


class Coordinate:
    dimension = 2

    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

    def __str__(self) -> str:
        return '(' + self.x + ', ' + self.y + ')'

    @staticmethod
    def transform_one_based_indexing_to_zero_based_indexing(one_based_coordinate):
        return Coordinate(one_based_coordinate.x - 1, one_based_coordinate.y - 1)

    @staticmethod
    def transform_string_to_coordinate(coordinate_string):
        if len(coordinate_string.split()) != Coordinate.dimension:
            raise ValueError("Expected " + str(Coordinate.dimension) + " inputs")

        try:
            int_input = map(int, coordinate_string.split())
        except ValueError as error:
            raise ValueError("Integer inputs expected") from error

        return Coordinate(*tuple(int_input))


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
        return not self.board[coordinate.y][coordinate.x] == Tile.EMPTY

    def place_symbol(self, move: Coordinate, active_symbol: Any) -> None:
        """Catches out of range input"""
        try:
            if not self.is_occupied(move):
                self.board[move.y][move.x] = active_symbol
            else:
                raise ValueError("Position is occupied")
        except ValueError as error:
            print(error)
            raise
        except IndexError:
            print("IndexError: Move is out of bounds")
            raise

    def get_lines(self):
        lines = []
        lines.extend(self.get_rows())
        lines.extend(self.get_columns())
        lines.extend(self.get_diagonals())

        return lines

    def get_rows(self):
        return [self.board[i, :] for i in range(self.size)]

    def get_columns(self):
        return [self.board[:, i] for i in range(self.size)]

    def get_diagonals(self):
        return [self.board.diagonal(), numpy.fliplr(self.board).diagonal()]


class Player:
    """Base class for game players."""

    def __init__(self, name: str, symbol: Tile) -> None:
        self.name: str = name
        self.symbol: Tile = symbol

    # noinspection PyMethodMayBeStatic
    def make_move(self, board_size: int) -> Coordinate:
        return Coordinate(random.randrange(board_size), random.randrange(board_size))


class PlayerHuman(Player):
    """Class for human player who can choose a move themselves."""

    def get_move_input(self):
        user_input = input(f'Enter two integers within the bounds: ')
        if len(user_input.split()) != Coordinate.dimension:
            raise ValueError("Expected " + str(Coordinate.dimension) + " inputs")

    def make_move(self, board_size: int) -> Coordinate:
        user_input = self.get_move_input()
        coordinate = Coordinate.transform_string_to_coordinate(user_input)

        return Coordinate.transform_one_based_indexing_to_zero_based_indexing(coordinate)


class PlayerAI(Player):
    """Class for AI player who uses an algorithm to play."""
    pass
