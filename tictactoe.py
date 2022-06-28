import itertools
from typing import Tuple
import random
import sys

import pygame

from game_logic_classes import GameBoard, Player, PlayerHuman, PlayerAI
from game_logic_functions import is_win
from game_logic_constants import Tile
from pygame_classes import Button, Grid
from pygame_functions import draw_grid

Coordinate = Tuple[int, int]


def main() -> None:
    """Placeholder docstring"""

    # game logic variables setup
    game_board_size: int = 3
    game_board: GameBoard = GameBoard(game_board_size)
    player_list = [PlayerHuman("Human", Tile.PLAYER_1), PlayerAI("AI", Tile.PLAYER_2)]
    random.shuffle(player_list)
    player_list = itertools.cycle(player_list)

    # pygame setup
    screen_width = 600
    screen_height = 600

    # pygame initialization starts
    pygame.init()

    screen_surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tic-Tac-Toe")
    screen_surface.fill(pygame.Color("White"))

    draw_grid(screen_surface, screen_height, screen_width, pygame.Color("Black"))

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
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                test_rect_height = test_rect_width = 20
                rect = pygame.Rect(*mouse_position, test_rect_width, test_rect_height)
                rect_outline_thickness = 1
                pygame.draw.rect(screen_surface, pygame.Color("Black"), rect, rect_outline_thickness)

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
            game_board.place_symbol(player_move, player_current.symbol)
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
