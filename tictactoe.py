from typing import Tuple

import pygame

from game_logic_classes import Game
from game_logic_functions import is_win
from pygame_functions import draw_grid

Coordinate = Tuple[int, int]


def main() -> None:
    """Placeholder docstring"""

    game = Game()

    # pygame setup
    display_width = 600
    display_height = 600

    # pygame initialization starts
    pygame.init()

    display_surface = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Tic-Tac-Toe")
    display_surface.fill(pygame.Color("White"))

    draw_grid(display_surface, pygame.Color("Black"))

    pygame.display.flip()
    # pygame initialization ends

    # choose between cli game loop and pygame game loop
    running = True
    running_pygame = False

    # pygame loop
    while running_pygame:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running_pygame = False
            elif event.type == pygame.QUIT:
                running_pygame = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                test_rect_height = test_rect_width = 20
                rect = pygame.Rect(*mouse_position, test_rect_width, test_rect_height)
                rect_outline_thickness = 1
                pygame.draw.rect(display_surface, pygame.Color("Black"), rect, rect_outline_thickness)

            pygame.display.flip()

    # game loop
    while running:
        player_move = game.get_player_move()

        try:
            game.board.place_symbol(player_move, game.player_current.symbol)
        # Throws error if variable move is not set
        except NameError as error:
            print(error)
            exit(-1)
        except (IndexError, ValueError):
            continue

        print("Current State:\n", game.board, sep="")

        game_result: bool = is_win(game.board)
        if game_result:
            print(f"Winner is player {game.player_current.name}")
            running = False

        if running:
            print("turn end")
            game.player_current = game.get_next_player()


if __name__ == '__main__':
    main()
