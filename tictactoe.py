from typing import Tuple
import sys, os

import pygame

from game_logic_classes import Game, PlayerHuman, PlayerAI
from game_logic_constants import Tile
from game_logic_functions import get_game_window_size, is_win
from pygame_classes import TileSet, GameWindow
from pygame_functions import draw_grid, get_grid_pos

Coordinate = Tuple[int, int]

os.chdir(sys._MEIPASS)


def main() -> None:
    """Placeholder docstring"""

    pygame.init()

    player_a = PlayerHuman("Human", Tile.PLAYER_1)
    player_b = PlayerAI("AI", Tile.PLAYER_2)
    game = Game(player_a, player_b)

    # pygame setup
    display_width, display_height = get_game_window_size()
    game_window = GameWindow(display_width, display_height)

    number_of_divisions = 3
    cell_width = display_width // number_of_divisions
    cell_height = display_height // number_of_divisions
    cell_dims = cell_width, cell_height
    file = "tileset.png"
    tile_size = 34
    margin = 1
    tile_set = TileSet(file, tile_size, cell_dims, margin)

    draw_grid(game_window.display_surface, pygame.Color("Black"))

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
                grid_pos = get_grid_pos(cell_width, cell_height, mouse_position)
                cell_start_corner = grid_pos[0]*cell_width, grid_pos[1]*cell_height
                tile = tile_set.tiles[1]
                tile = pygame.transform.scale(tile, cell_dims)
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
