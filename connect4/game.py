from connect4.board import Board
from connect4.utils import get_int_input
import numpy as np


class Game:
    def __init__(self, num_players: int, board: Board) -> None:
        self.num_players = num_players
        self.board = board

        self.players_labels = np.arange(1, num_players + 1)

    def get_player_move(self, player_label: int) -> int:

        while True:
            print(f"Player {player_label} choose column")
            player_move = get_int_input()

            if self.board.is_valid_move(player_move):
                return player_move

    def step(self) -> bool:
        self.board.show()

        for player_label in self.players_labels:

            player_move = self.get_player_move(player_label)

            self.board.set_cell_value(player_move, player_label)

            self.board.show()

            if self.board.is_player_win(player_label):
                print(f"Player {player_label} won!")
                return True

            if self.board.is_board_full():
                print("Draw!")
                return True

        return False
