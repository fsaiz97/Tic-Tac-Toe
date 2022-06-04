import itertools

import pygame

from classes import *
from functions import *

Coordinate = Tuple[int, int]


def main() -> None:
    """Placeholder docstring"""
    board_size: int = 3
    game_board: Board = Board(board_size)

    player_list = [PlayerHuman("Human", 1), PlayerAI("AI", 2)]
    random.shuffle(player_list)
    player_list = itertools.cycle(player_list)

    pygame.init()

    # screen variables for pygame
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Current State:\n", game_board, sep="")

    player_current: Player = next(player_list)

    running = True

    # game loop
    while running:
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
            running = False

        if running:
            print("turn end")
            player_current: Player = next(player_list)


if __name__ == '__main__':
    main()
