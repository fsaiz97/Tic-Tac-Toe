import sys


def get_possibles(n):
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
        if symbol == None:
            continue
        else:
            return symbol
    return False


class Player:
    def __init__(self, name, ai=False):
        self.name = name
        self.isAI = ai
        self.records = {"wins": 0, "losses": 0, "draws": 0}

    def ai_pick(self):
        import random

        return [random.randint(0,2) for _ in range(2)]

    def get_input(self):
        if not active.isAI:
            while True:
                try:
                    x, y = tuple(map(int,
                        input(f'({active.name}) Enter two integers between 0 and {self.n-1}:').split()))
                    break
                except ValueError:
                    print("Error: Input must be integers." , file=sys.stderr)
                    continue
        else:
            x, y = active.ai_pick()


class Game:
    def __init__(self, n, player1, player2):
        self.board = tuple([None for _ in range(n)] for _ in range(n))
        self.size = n
        player1.symbol, player2.symbol = 'O', 'X'
        self.players = (player1, player2)
        self.turn = 0
        self.state = "ongoing"


    def place_selection(self):
        try:
            self.board[y][x] = active.symbol
        except IndexError:
            print(f"Error: Input should be between 0 and {self.n-1}.", file=sys.stderr)
            continue


    def print_board(self):
        for line in self.board:
            print(line)


    def run_turn(self):
        # select active player's name based on turn
        active = self.players[self.turn % 2]

        x, y = active.get_input()

        place_selection()

        print_board()

        result = check_win(self.board, possible)
        if result != False:
            print(f"Winner is player {result}")
            break

        self.turn += 1


class Player:
    def __init__(self, name, ai=False):
        self.name = name
        self.isAI = ai
        self.records = {"wins": 0, "losses": 0, "draws": 0}

    def ai_pick(self):
        import random

        return [random.randint(0,2) for _ in range(2)]


class Game:
    def __init__(self, n, player1, player2):
        self.board = tuple([None for _ in range(n)] for _ in range(n))
        self.size = n
        player1.symbol, player2.symbol = 'O', 'X'
        self.players = (player1, player2)
        self.turn = 0
        self.state = "ongoing"


    def run_turn(self):
        # select active player's name based on turn
        active = self.players[self.turn % 2]

        if not active.isAI:
            while True:
                try:
                    x, y = tuple(map(int,
                                     input(f'({active.name}) Enter two integers between 0 and {n-1}:').split()))
                    break
                except ValueError:
                    print("Error: Input must be integers." , file=sys.stderr)
                    continue
        else:
            x, y = active.ai_pick()

        try:
            self.board[y][x] = active.symbol
        except IndexError:
            print(f"Error: Input should be between 0 and {n-1}.", file=sys.stderr)
            continue

        for line in self.board:
            print(line)

        result = check_win(self.board, possible)
        if result != False:
            print(f"Winner is player {result}")
            break

        self.turn += 1


def main():
    n = 3  # board size
    human = Player(input("name = "))
    comp = Player("comp", ai=True)
    game = Game(3, human, comp)
    possible = get_possibles(game.size)

    while True:
        # select active player's name based on turn
        active = game.players[game.turn % 2]

        if not active.isAI:
            try:
                x, y = tuple(map(int,
                                 input(f'({active.name}) Enter two integers between 0 and {n-1}:').split()))
            except ValueError:
                print("Error: Input must be integers." , file=sys.stderr)
                continue
        else:
            x, y = active.ai_pick()

        try:
            game.board[y][x] = active.symbol
        except IndexError:
            print(f"Error: Input should be between 0 and {n-1}.", file=sys.stderr)
            continue

        for line in game.board:
            print(line)

        result = check_win(game.board, possible)
        if result != False:
            print(f"Winner is player {result}")
            break

        game.turn += 1


if __name__ == '__main__':
    main()
