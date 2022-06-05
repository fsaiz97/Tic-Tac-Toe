import itertools

import pygame
from pygame.locals import (
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_ESCAPE,
    QUIT,
)

from game_classes import *
from game_functions import *
from pygame_classes import Button, Grid
from pygame_functions import draw_grid

Coordinate = Tuple[int, int]


def main() -> None:
    """Placeholder docstring"""

    # game logic variables setup
    board_size: int = 3
    game_board: Board = Board(board_size)
    player_list = [PlayerHuman("Human", 1), PlayerAI("AI", 2)]
    random.shuffle(player_list)
    player_list = itertools.cycle(player_list)

    # pygame setup
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    # colour variables for pygame
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # pygame initialization starts
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(WHITE)

    draw_grid(screen, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK)

    # button = Button(100, 100, pygame.Color("Red"))
    # button.draw(screen, (SCREEN_HEIGHT//2, SCREEN_WIDTH//2))

    grid = Grid(3, 3, 300, 300)
    grid.draw(screen, (SCREEN_WIDTH - grid.image.get_width() // 2, SCREEN_HEIGHT - grid.image.get_height() // 2))

    pygame.display.flip()
    # pygame initialization ends

    # choose between cli game loop and pygame game loop
    running = False
    runningPygame = True

    # pygame loop
    while runningPygame:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    runningPygame = False
            elif event.type == QUIT:
                runningPygame = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                rect = pygame.Rect(*mouse_pos, 20, 20)
                pygame.draw.rect(screen, BLACK, rect, 1)

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
