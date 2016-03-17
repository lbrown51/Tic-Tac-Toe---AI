import random
import re
import time

if __name__ == "__main__":
            import multiprocessing as mp
            pool = mp.Pool(processes=9)


def get_board(board, cboard=-1):
    if cboard == -1:
        return board
    else:
        return board[cboard]


def try_choice(tfm, choice, thboard, game, player, cboard):
    get_board(thboard, cboard)[choice] = 1
    sum_trials = 0
    total_trials = 0
    while time.clock() < tfm:
        trial = game.go(thboard, player, cboard)
        type(trial)
        type(sum_trials)
        sum_trials = sum_trials + trial
        total_trials += 1

    average = sum_trials / total_trials
    return choice, average


def paratry(tfm, game, board, available, player, cboard):
    if cboard == -1:
        thboard = [item for item in board]
    else:
        thboard = [[item for item in brd] for brd in board]

    if __name__ == "__main__":
        results = []
        for choice in available:
            results.append(pool.apply_async(try_choice, args=(tfm, choice, thboard, game, player, cboard)))

        max_item = 0,0
        for item in results:
            returned = item.get()
            if returned[1] > max_item[1]:
                max_item = returned

        return max_item


def is_number(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def print_board(board):
    to_print = [item for item in board]
    index = 0
    for item in board:
        if item == 2:
            to_print[index] = " "
        elif item == 1:
            to_print[index] = "X"
        else:
            to_print[index] = "O"
        index += 1
    print(to_print[:3])
    print(to_print[3:6])
    print(to_print[6:])


def print_boards(board):
    to_print = [[item for item in brd] for brd in board]
    index = 0
    for brd in board:
        jndex = 0
        for item in brd:
            if item == 2:
                to_print[index][jndex] = " "
            elif item == 1:
                to_print[index][jndex] = "X"
            else:
                to_print[index][jndex] = "O"
            jndex += 1
        index += 1

    row1 = []
    row2 = []
    row3 = []

    for item in to_print:
        row1.append(item[:3])
        row2.append(item[3:6])
        row3.append(item[6:])

    print(row1[:3])
    print(row2[:3])
    print(row3[:3])
    print()
    print(row1[3:6])
    print(row2[3:6])
    print(row3[3:6])
    print()
    print(row1[6:])
    print(row2[6:])
    print(row3[6:])


class Game:
    test = 0
    win_pat = [
        '111[210][210][210][210][210][210]',
        '[210][210][210]111[210][210][210]',
        '[210][210][210][210][210][210]111',
        '1[210][210]1[210][210]1[210][210]',
        '[210]1[210][210]1[210][210]1[210]',
        '[210][210]1[210][210]1[210][210]1',
        '1[210][210][210]1[210][210][210]1',
        '[210][210]1[210]1[210]1[210][210]',
        '000[210][210][210][210][210][210]',
        '[210][210][210]000[210][210][210]',
        '[210][210][210][210][210][210]000',
        '0[210][210]0[210][210]0[210][210]',
        '[210]0[210][210]0[210][210]0[210]',
        '[210][210]0[210][210]0[210][210]0',
        '0[210][210][210]0[210][210][210]0',
        '[210][210]0[210]0[210]0[210][210]'
    ]
    win = [re.compile(item) for item in win_pat]

    def __init__(self, player=1):
        pass

    def go(self, board, player, cboard):
        self.test = []
        self.actions(board, player, cboard)
        return self.test

    def actions(self, board, player, cboard):
        next_action = -1
        if 2 not in get_board(board, cboard):
            self.test = 0
        else:
            available = []
            index = 0
            for item in get_board(board, cboard):
                if item == 2:
                    get_board(board, cboard)[index] = player
                    if self.is_goal(''.join(str(e) for e in get_board(board, cboard))):
                        next_action = index
                    get_board(board, cboard)[index] = 2
                    available.append(index)
                index += 1

            if not (next_action == -1):
                if player == 0:
                    self.test = -1
                else:
                    self.test = 1
            else:
                next_action = available[random.randrange(0, len(available))]
                get_board(board, cboard)[next_action] = player
                player = (player + 1) % 2
                self.actions(board, player, cboard)
                player = (player + 1) % 2
                get_board(board, cboard)[next_action] = 2

    def is_goal(self, board):
        for item in self.win:
            if item.match(board) is not None:
                return True
        return False


if __name__ == "__main__":
    def comp_move(tfm, game, player, board, cboard):
        def next_move_win(num_board):
            jndex = 0
            for item in board[num_board]:
                if item == 2:
                    board[num_board][jndex] = 0
                    if game.is_goal(''.join(str(e) for e in board[num_board])):
                        board[num_board][jndex] = 2
                        return True
                    board[num_board][jndex] = 2
                jndex += 1
            return False

        available = []
        index = 0
        for pos in get_board(board, cboard):
            if pos == 2:
                if cboard == -1:
                    get_board(board, cboard)[index] = (player + 1) % 2
                    if game.is_goal(''.join(str(e) for e in board)):
                        return index, 1
                    available.append(index)
                    get_board(board, cboard)[index] = 2
                else:
                    if not (next_move_win(index)):
                        available.append(index)
            index += 1

        player = (player + 1) % 2
        move = paratry(int(tfm)+time.clock(), game, board, available, player, cboard)

        player = (player + 1) % 2
        return move


    def start(gc, tfm, player=1):
        if gc == 1:
            board = [2 for item in range(9)]
            cboard = -1
        else:
            board = [[2 for item in range(9)] for item in range(9)]
            if player == 1:
                cboard = 4

        game = Game()

        def condition():
            if gc == 1:
                return game.is_goal(''.join(str(e) for e in board))
            else:
                for brd in board:
                    if game.is_goal(''.join(str(e) for e in brd)):
                        return True
                    else:
                        return False

        while not condition():
            if gc == 1:
                print_board(board)
                print()
            else:
                print_boards(board)
                print("Current Board: " + str(cboard + 1))
                print()

            if player == 0:
                available = []
                index = 0
                for pos in get_board(board, cboard):
                    if pos == 2:
                        available.append(index)
                    index += 1

                human = input("What placement would you like")
                while not (is_number(human)) or not (int(human) - 1 in available):
                    if human == "exit":
                        print("Exiting Game")
                        return
                    else:
                        print("That's placement's not available. Try again")
                        human = input("What placement would you like")

                get_board(board, cboard)[int(human) - 1] = 0

                if gc == 2:
                    cboard = int(human) - 1
            else:
                index = 0
                move = -1
                for pos in get_board(board, cboard):
                    if pos == 2:
                        get_board(board, cboard)[index] = 1
                        if game.is_goal(''.join(str(e) for e in get_board(board, cboard))):
                            move = index, 1
                        get_board(board, cboard)[index] = 2
                    index += 1

                if move == -1:
                    move = comp_move(tfm, game, 1, board, cboard)

                get_board(board, cboard)[move[0]] = 1

                if gc == 2:
                    cboard = move[0]

            player = (player + 1) % 2

        # print_boards(board)
        print("Player %s wins!!" % player)


    def menu():
        print("1. 3X3 Tic Tac Toe")
        print("2. Nine Board Tic Tac Toe")
        human = input("Enter 1 or 2 to select a game")
        while not (is_number(human)) or not (int(human) == 1 or int(human) == 2):
            if human == "exit":
                print("Exiting Game")
                return
            else:
                print("That's not an available option. Try again")
                print("1. 3X3 Tic Tac Toe")
                print("2. Nine Board Tic Tac Toe")
                human = input("Enter 1 or 2 to select a game")

        print("How much time will the computer have for each move?")
        tfm = input("Enter time in seconds")
        while not (is_number(tfm)):
            if tfm == "exit":
                print("Exiting Game")
                return
            else:
                print("That's not a valid time")
                tfm = input("Enter time in seconds")

        start(int(human), tfm)


    menu()
