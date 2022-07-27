import random
from typing import Any
import itertools

import numpy
import numpy.typing
# import inquirer

from game_logic_constants import Tile, BOARD_SIZE


class Coordinate:
    dimension = 2

    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

    def __str__(self) -> str:
        return '(' + self.x + ', ' + self.y + ')'

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return False

    @staticmethod
    def transform_one_based_indexing_to_zero_based_indexing(one_based_coordinate):
        return Coordinate(one_based_coordinate.x - 1, one_based_coordinate.y - 1)

    @staticmethod
    def transform_string_to_coordinate(coordinate_string):
        try:
            int_input = map(int, coordinate_string.split())
        except ValueError:
            raise

        return Coordinate(*tuple(int_input))


class GameBoard:
    """A class representing a square game board. Empty squares are represented by a 0."""

    def __init__(self, size: int) -> None:
        """Placeholder docstring"""
        self.size: int = size
        self.board: numpy.typing.ArrayLike = numpy.full((self.size, self.size), Tile.EMPTY, dtype=object)

    def __str__(self) -> str:
        """Placeholder docstring"""
        return '\n'.join(['|'.join([str(mark.value) for mark in row]) for row in self.board])

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
        except ValueError:
            raise
        except IndexError as error:
            raise IndexError("IndexError: Move is out of bounds") from error

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
    def make_move(self) -> Coordinate:
        pass

    def get_move(self):
        return self.make_move()


class PlayerHuman(Player):
    """Class for human player who can choose a move themselves."""

    @staticmethod
    def get_move_input():
        user_input = input(f'Enter two integers within the bounds: ')
        if len(user_input.split()) != Coordinate.dimension:
            raise ValueError("Expected " + str(Coordinate.dimension) + " inputs")

        return user_input

    def get_move(self):
        player_command = PlayerHuman.get_human_command()
        # move input loop
        if player_command == 'm':
            while True:
                try:
                    player_move: Coordinate = self.make_move()
                except ValueError as error:
                    print(error)
                else:
                    break
        elif player_command == 'q':
            exit("Quitting game...")
        return player_move

    def make_move(self) -> Coordinate:
        user_input = self.get_move_input()
        coordinate = Coordinate.transform_string_to_coordinate(user_input)

        return Coordinate.transform_one_based_indexing_to_zero_based_indexing(coordinate)

    @staticmethod
    def get_human_command():
        # command loop
        while True:
            try:
                # question = [
                #     inquirer.List('command', message="Choose a command", choices=["Make a move", "Quit"])
                # ]
                # player_command: str = inquirer.prompt(question)
                # print(player_command)
                # exit()
                player_command: str = input("Enter a command ('m' for move or 'q' to quit): ")
                if player_command not in ['m', 'q']:
                    raise ValueError("Invalid player_command")
            except ValueError as error:
                print(error)
            else:
                break
        return player_command


class PlayerAI(Player):
    """Class for AI player who uses an algorithm to play."""
    def make_move(self) -> Coordinate:
        return Coordinate(random.randrange(BOARD_SIZE), random.randrange(BOARD_SIZE))


class Game:
    """Represents individual game rounds, storing all information about that round."""

    def __init__(self, player_1: Player, player_2: Player, board_size: int = 3):
        # Initializes a game board
        self.board = GameBoard(board_size)
        # Initializes players
        self.player_list = [player_1, player_2]
        self.player_order = self.set_player_order()
        self.player_current = self.get_next_player()

    def get_number_of_partitions(self):
        return self.board.size

    def set_player_order(self):
        random.shuffle(self.player_list)
        return itertools.cycle(self.player_list)

    def get_next_player(self):
        return next(self.player_order)
