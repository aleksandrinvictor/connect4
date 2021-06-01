import numpy as np
from numpy.core.fromnumeric import diagonal


class Board:
    def __init__(self, num_rows: int, num_cols: int) -> None:

        self._num_rows = num_rows
        self._num_cols = num_cols

        self.board = np.zeros((num_rows, num_cols))

        self._winner_idx = -1

    @property
    def num_rows(self):
        return self._num_rows

    @property
    def num_cols(self):
        return self._num_cols

    def show(self):
        print("\n------------- Game board -------------\n")

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                print(f" {int(self.board[i, j])} ", end="|")
            print("\n")

        print("\ncolumn numbers:")
        for j in range(self.num_cols):
            print(f" {j} ", end="|")

        print("\n")
        print("--------------------\n")

    def is_board_full(self):
        return np.count_nonzero(self.board) == self.num_cols * self.num_rows

    def is_valid_move(self, y: int) -> bool:
        if y > self.num_cols - 1:
            print(f"{y} > index of last column = {self.num_cols - 1}")
            return False

        if y < 0:
            print(f"{y} < 0")
            return False

        if np.count_nonzero(self.board[:, y] == 0) == 0:
            print("Column is full! Choose another column")
            return False

        return True

    def set_cell_value(self, y: int, value: int) -> None:
        if self.board[-1, y] == 0:
            self.board[-1, y] = value
        else:
            for i in range(self.num_rows - 1):
                if self.board[i + 1, y] != 0:
                    self.board[i, y] = value
                    break

    def _is_row_win(self, player_idx: int) -> bool:
        # check if player win by rows
        for j in range(self.num_cols):
            counter = 0
            for i in range(self.num_rows):
                if self.board[i, j] == player_idx:
                    counter += 1

                if counter >= 4:
                    return True

        return False

    def _is_col_win(self, player_idx: int) -> bool:
        # check if player win by rows
        for i in range(self.num_rows):
            counter = 0
            for j in range(self.num_cols):
                if self.board[i, j] == player_idx:
                    counter += 1

                if counter >= 4:
                    return True

        return False

    def _is_diag_win(self, player_idx: int) -> bool:
        # check if player win by diagonals
        left_to_right_diagonals = [
            np.diagonal(self.board, x)
            for x in range(-(self.num_rows - 1), self.num_cols)
        ]

        right_to_left_diagonals = [
            np.diagonal(np.fliplr(self.board), x)
            for x in range(-(self.num_rows - 1), self.num_cols)
        ]

        diagonals = left_to_right_diagonals + right_to_left_diagonals
        diagonals = [v for v in diagonals if len(v) >= 4]

        for diag in diagonals:
            counter = 0
            for i in range(len(diag)):

                if diag[i] == player_idx:
                    counter += 1

                if counter >= 4:
                    return True

        return False

    def is_player_win(self, player_idx: int) -> bool:
        return (
            self._is_row_win(player_idx)
            or self._is_col_win(player_idx)
            or self._is_diag_win(player_idx)
        )
