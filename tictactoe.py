import itertools
from typing import Tuple
import random

import pygame

from game_logic_classes import Board, Player, PlayerHuman, PlayerAI
from game_logic_functions import is_win
from pygame_classes import Button, Grid
from pygame_functions import draw_grid

Coordinate = Tuple[int, int]


def main() -> None:
    """Placeholder docstring"""

    # game logic variables setup
    game_board_size: int = 3
    game_board: Board = Board(game_board_size)
    player_list = [PlayerHuman("Human", 1), PlayerAI("AI", 2)]
    random.shuffle(player_list)
    player_list = itertools.cycle(player_list)

    # pygame setup
    screen_width = 600
    screen_height = 600

    # pygame initialization starts
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(pygame.Color("White"))

    # draw_grid(screen, screen_height, screen_width, pygame.Color("Black"))

    # button = Button(100, 100, pygame.Color("Red"))
    # button.draw(screen, (screen_height//2, screen_width//2))

    grid = Grid(3, 3, 300, 300)
    grid.draw(screen, (screen_width - grid.image.get_width() // 2, screen_height - grid.image.get_height() // 2))

    pygame.display.flip()
    # pygame initialization ends

    # choose between cli game loop and pygame game loop
    running = False
    running_pygame = True

    # pygame loop
    while running_pygame:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_pygame = False
            elif event.type == pygame.QUIT:
                running_pygame = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                rect = pygame.Rect(*mouse_position, 20, 20)
                pygame.draw.rect(screen, pygame.Color("Black"), rect, 1)

            pygame.display.flip()

    # player_current: Player = next(player_list)
    # print("Current State:\n", game_board, sep="")

    # game loop
    while running:
        # code for processing human player input
        if isinstance(player_current, PlayerHuman):
            # command loop
            while True:
                try:
                    player_command: str = input(f' Enter m to make a move or enter q to quit: ')
                    if player_command not in ['m', 'q']:
                        raise ValueError("Invalid player_command")
                except ValueError as error:
                    print(error)
                else:
                    break

            # move input loop
            if player_command == 'm':
                while True:
                    try:
                        player_move: Coordinate = player_current.make_move(game_board.size)
                    except ValueError as error:
                        print(error)
                    else:
                        break
            elif player_command == 'q':
                exit("Quitting game...")

        else:
            # code for processing AI player input
            while True:
                player_move: Coordinate = player_current.make_move(game_board.size)
                if not game_board.is_occupied(player_move):
                    break

        try:
            game_board.place_mark(player_move, player_current.symbol)
        # Throws error if variable move is not set
        except NameError as error:
            print(error)
            exit(-1)
        except (IndexError, ValueError):
            continue

        print("Current State:\n", game_board, sep="")

        game_result: bool = is_win(game_board)
        if game_result:
            print(f"Winner is player {player_current.name}")
            running = False

        if running:
            print("turn end")
            player_current: Player = next(player_list)


if __name__ == '__main__':
    main()
