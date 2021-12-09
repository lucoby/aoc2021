import numpy as np
import warnings

warnings.simplefilter("ignore", UserWarning)


def read_board(f):
    f.readline()
    return np.expand_dims(np.loadtxt(f, max_rows=5), axis=0)


if __name__ == '__main__':
    with open("input1.txt") as f:
        numbers = [int(i) for i in f.readline().strip().split(",")]

        boards = []
        board = read_board(f)
        while board.size > 0:
            boards.append(board)
            board = read_board(f)
        boards = np.concatenate(boards)

        for i in numbers:
            boards[boards == i] = -1
            winning_board_idx = np.where((boards == -1).all(axis=2).any(axis=1) | (boards == -1).all(axis=1).any(axis=1))[0]


            if winning_board_idx.size > 0:
                winning_board_idx = winning_board_idx[0]
                break

        winning_board = boards[winning_board_idx]
        print(winning_board[winning_board > 0].sum() * i)
