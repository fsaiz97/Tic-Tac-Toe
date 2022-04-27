import random
from typing import Tuple, Any
import itertools

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


def main() -> None:
    """Placeholder docstring"""
    board_size: int = 3
    game_board: Board = Board(board_size)
    player_list = [PlayerHuman("Human", 1), PlayerAI("AI", 2)]
    random.shuffle(player_list)
    player_list = itertools.cycle(player_list)
    print("Current State:\n", game_board, sep="")

    player_current: Player = next(player_list)

    # game loop
    while True:
        # code for processing human player input
        if isinstance(player_current, PlayerHuman):
            # command loop
            while True:
                try:
                    command: str = input(f' Enter m to make a move or enter q to quit: ')
                    if command not in ['m', 'q']:
                        raise ValueError("Invalid command")
                except ValueError as err:
                    print(err)
                else:
                    break

            # move input loop
            if command == 'm':
                while True:
                    try:
                        move: Coordinate = player_current.make_move(game_board.size)
                    except ValueError as err:
                        print(err)
                    else:
                        break
            elif command == 'q':
                exit("Quitting game...")

        else:
            # code for processing AI player input
            while True:
                move: Coordinate = player_current.make_move(game_board.size)
                if not game_board.is_occupied(move):
                    break

        try:
            game_board.place_mark(move, player_current.symbol)
        # Throws error if variable move is not set
        except NameError as err:
            print(err)
            exit(-1)
        except (IndexError, ValueError):
            continue

        print("Current State:\n", game_board, sep="")

        result: bool = is_win(game_board)
        if result:
            print(f"Winner is player {player_current.name}")
            break

        print("turn end")
        player_current: Player = next(player_list)


if __name__ == '__main__':
    main()
