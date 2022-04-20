import sys
import numpy as np


def check_line(line):
    if np.all(np.isclose(line, line[0])):
        if line[0] == 0:
            return False
        elif line[0] in (1,2):
            return True
        else:
            raise ValueError("Impossible symbol on board")


def is_win(game_board, BOARD_SIZE):
    for i in range(BOARD_SIZE):
        if check_line(game_board[:,i]) or check_line(game_board[i,:]):
            return True

    if check_line(game_board.diagonal()) or check_line(np.fliplr(game_board).diagonal()):
        return True

    return False  # if no full lines are found


def get_move(BOARD_SIZE):
    try:
        coordinate = tuple(map(int, input(f'Enter two integers between 1 and {BOARD_SIZE}: ').split()))
    except ValueError as err:
        raise ValueError("Integer inputs expected") from err

    for component in coordinate:
        if not (1 <= component <= BOARD_SIZE):
            raise ValueError("Input is outside the expected range")

    return (coordinate[1]-1, coordinate[0]-1)  # converts from human convenient coordinates to flipped index 0
    # coordinates


def main():
    BOARD_SIZE = 3
    game_board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    print("Current State:\n", game_board)

    player_current = 1

    while True:
        while True:
            try:
                command = input(f' Enter m to make a move or enter q to quit: ')
                if command == 'm':
                    while True:
                        try:
                            move = get_move(BOARD_SIZE)
                            if game_board[move[0]][move[1]] != 0:
                                raise ValueError("Board position already filled")
                        except ValueError as err:
                            print(err, file=sys.stderr)
                        else:
                            break
                elif command == 'q':
                    exit("Quitting game...")
                else:
                    raise ValueError("Invalid command")
            except ValueError as err:
                print(err, file=sys.stderr)
            else:
                break


        game_board[move[0]][move[1]] = player_current

        print(game_board)

        result = is_win(game_board, BOARD_SIZE)
        if result:
            print(f"Winner is player {player_current}")
            break

        player_current = 2 if player_current == 1 else 1


if __name__ == '__main__':
    main()
