from typing import Tuple

import pygame

from game_logic_functions import is_win
from pygame_functions import get_grid_pos
from general_functions import load_tiles
from initialization_functions import initialize_game_window, initialize_game

Coordinate = Tuple[int, int]


def main() -> None:
    """Placeholder docstring"""

    # initialize game, display and players
    pygame.init()
    game = initialize_game()
    game_window = initialize_game_window(game.get_number_of_partitions())
    tile_set = load_tiles()
    # start game
    # event loop: react to mouse clicks, exit on clicking exit button or closing window
    # clean up game

    pygame.display.flip()

    # choose between cli game loop and pygame game loop
    running = False
    running_pygame = True

    # pygame loop
    while running_pygame:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running_pygame = False
            elif event.type == pygame.QUIT:
                running_pygame = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                grid_pos = get_grid_pos(game_window.cell_width, game_window.cell_height, mouse_position)
                cell_start_corner = grid_pos[0]*game_window.cell_width, grid_pos[1]*game_window.cell_height
                tile = tile_set.tiles[1]
                cell_size = (game_window.cell_width, game_window.cell_height)
                tile = pygame.transform.scale(tile, cell_size)
                game_window.display_surface.blit(tile, cell_start_corner)

            pygame.display.flip()

    # game loop
    while running:
        player_move = game.player_current.get_move()

        try:
            game.board.place_symbol(player_move, game.player_current.symbol)
        # Throws error if variable move is not set
        except NameError as error:
            print(error)
            exit(-1)
        except (IndexError, ValueError) as error:
            print(error)
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
