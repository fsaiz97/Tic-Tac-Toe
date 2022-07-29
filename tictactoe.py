import pygame

from game_logic_functions import is_win
from general_functions import load_tiles, get_graphics_choice
from initialization_functions import initialize_game_window, initialize_game


def main() -> None:
    """Placeholder docstring"""

    pygame.init()
    game = initialize_game()

    # choose between cli game loop and pygame game loop
    graphics_on = get_graphics_choice()

    running = True

    if graphics_on:
        # initialize graphics
        game_window = initialize_game_window(game.get_number_of_partitions())
        tile_set = load_tiles()

        while running:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    grid_pos = game_window.get_grid_pos(mouse_position)
                    cell_start_corner = game_window.get_cell_top_left_point(grid_pos)

                    tile = tile_set.tiles[1]
                    game_window.place_tile(cell_start_corner, tile)

                pygame.display.flip()
    else:
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
