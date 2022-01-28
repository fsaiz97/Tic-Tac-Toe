import sys


def get_possibles(board, n):
    # get rows
    possible = [[(x, y) for x in range(n)] for y in range(n)]
    # get columns
    possible += [[(x, y) for y in range(n)] for x in range(n)]
    # get diagonals
    possible += [[(i, i) for i in range(n)], [(i, n-1-i) for i in range(n)]]

    return possible


def check_win(board, possible):
    for line in possible:
        symbols = set(board[coord[1]][coord[0]] for coord in line)
        if len(symbols) != 1:
            continue
        else:
            symbol = next(iter(symbols))
        if symbol == 0:
            continue
        else:
            return symbol
    return False
        

def main():
    n = 3
    board = [[0 for _ in range(n)] for _ in range(n)]
    active, passive = 1, 2
    possible = get_possibles(board, n)

    while True:
        try:
            x, y = tuple(map(int,
                             input(f'Enter two integers between 0 and {n-1}:').split()))
        except ValueError:
            print("Error: Input must be integers." , file=sys.stderr)
            continue

        try:
            board[y][x] = active
        except IndexError:
            print(f"Error: Input should be between 0 and {n-1}.", file=sys.stderr)
            continue

        for line in board:
            print(line)

        result = check_win(board, possible)
        if result != False:
            print(f"Winner is player {result}")
            break

        # changes active player
        active, passive = passive, active


if __name__ == '__main__':
    main()
