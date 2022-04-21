import sys
import numpy as np
import random


def check_line(line):
    if np.all(np.equal(line, line[0])):  # checks if all the marks in the line are equal
        if line[0] == 0:  # since 0 represents an empty square
            return False
        elif line[0] in (1, 2):
            return True
        else:
            raise ValueError("Impossible symbol on board")


def is_win(game_board, board_size):
    for i in range(board_size):
        if check_line(game_board[:, i]) or check_line(game_board[i, :]):  # checks for completed row or column
            return True

    if check_line(game_board.diagonal()) or check_line(np.fliplr(game_board).diagonal()):  # checks for completed
        # diagonal or anti-diagonal
        return True

    return False  # if no full lines are found


def get_move(board_size):
    try:
        coordinate = tuple(map(int, input(f'Enter two integers between 1 and {board_size}: ').split()))
    except ValueError as err:
        raise ValueError("Integer inputs expected") from err

    for component in coordinate:
        if not (1 <= component <= board_size):
            raise ValueError("Input is outside the expected range")

    return coordinate[1] - 1, coordinate[0] - 1  # converts from human convenient coordinates to flipped index 0
    # coordinates


def main():
    board_size = 3
    game_board = np.zeros((board_size, board_size), dtype=int)
    print("Current State:\n", game_board)

    player_current = 1

    while True:  # game loop
        if player_current == 1:
            # code for processing human player input
            while True:  # command loop
                try:
                    command = input(f' Enter m to make a move or enter q to quit: ')
                    if command not in ['m', 'q']:
                        raise ValueError("Invalid command")
                except ValueError as err:
                    print(err, file=sys.stderr)
                else:
                    break

            if command == 'm':
                while True:  # move input loop
                    try:
                        move = get_move(board_size)
                        if game_board[move[0]][move[1]] != 0:
                            raise ValueError("Board position already filled")
                    except ValueError as err:
                        print(err, file=sys.stderr)
                    else:
                        break
            elif command == 'q':
                exit("Quitting game...")

        else:
            # code for processing AI player input
            while True:
                move = (random.randrange(board_size), random.randrange(board_size))
                if game_board[move[0]][move[1]] == 0:
                    break

        try:  # Places mark at chosen position
            game_board[move[0]][move[1]] = player_current
        except NameError as err:  # Throws error if variable move is not set
            print(err)
            exit(-1)

        print("Current State:\n", game_board)

        result = is_win(game_board, board_size)
        if result:
            print(f"Winner is player {player_current}")
            break

        print("turn end")
        player_current = 2 if player_current == 1 else 1


if __name__ == '__main__':
    main()
