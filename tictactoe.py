import numpy as np
import random


class Board:
    """A class representing a game board"""

    def __init__(self, width, height=0):
        self.width = width
        if height != 0:
            self.height = height
        else:
            self.height = width

        self.state = np.zeros((self.height, self.width), dtype=int)

    def __str__(self):
        return '\n'.join(['|'.join([str(mark) for mark in row]) for row in self.state])

    def is_occupied(self, coordinate):
        if self.state[coordinate[0]][coordinate[1]] == 0:
            return False
        else:
            return True

    def place_mark(self, move, active_mark):
        # catches out of range input
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


def check_line(line):
    if np.all(np.equal(line, line[0])):  # checks if all the marks in the line are equal
        if line[0] == 0:  # since 0 represents an empty square
            return False
        elif line[0] in (1, 2):
            return True
        else:
            raise ValueError("Impossible symbol on board")


def is_win(game_board):
    for i in range(game_board.width):
        if check_line(game_board.state[:, i]):  # checks for completed columns
            return True

    for j in range(game_board.height):
        if check_line(game_board.state[j, :]):  # checks for completed rows
            return True

    # need to update this to check for all diagonals with correct length or only allow square boards?
    if check_line(game_board.state.diagonal()) or check_line(np.fliplr(game_board.state).diagonal()):
        # checks for completed diagonal or anti-diagonal
        return True

    return False  # if no full lines are found


def get_move():
    try:
        coordinate = tuple(map(int, input(f'Enter two integers within the width and height bounds '
                                          f'respectively: ').split()))
    except ValueError as err:
        raise ValueError("Integer inputs expected") from err

    return coordinate[1] - 1, coordinate[0] - 1  # converts from human convenient coordinates to flipped index 0
    # coordinates


def main():
    board_size = 3
    game_board = Board(board_size)
    print("Current State:\n", game_board, sep="")

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
                    print(err)
                else:
                    break

            if command == 'm':
                while True:  # move input loop
                    try:
                        move = get_move()
                    except ValueError as err:
                        print(err)
                    else:
                        break
            elif command == 'q':
                exit("Quitting game...")

        else:
            # code for processing AI player input
            while True:
                move = (random.randrange(game_board.height), random.randrange(game_board.width))
                if not game_board.is_occupied(move):
                    break

        try:  # Places mark at chosen position
            game_board.place_mark(move, player_current)
        except NameError as err:  # Throws error if variable move is not set
            print(err)
            exit(-1)
        except (IndexError, ValueError):
            continue

        print("Current State:\n", game_board, sep="")

        result = is_win(game_board)
        if result:
            print(f"Winner is player {player_current}")
            break

        print("turn end")
        player_current = 2 if player_current == 1 else 1


if __name__ == '__main__':
    main()
