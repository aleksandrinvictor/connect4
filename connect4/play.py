from connect4.board import Board
from connect4.game import Game
from connect4.utils import get_int_input


def setup_game() -> Game:
    print("Enter board rows: ")
    board_rows = get_int_input()

    print("Enter board columns: ")
    board_columns = get_int_input()

    print("Enter number of players: ")
    players_num = get_int_input()

    board = Board(board_rows, board_columns)

    game = Game(players_num, board)
    return game


def main():

    game = setup_game()

    while True:
        is_finished = game.step()

        if is_finished:
            print("Play again? (y / n):")
            play_again = str(input())

            if play_again == "y":
                game = setup_game()
                continue

            break


if __name__ == "__main__":
    main()
