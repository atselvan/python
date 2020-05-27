import os
import time


def display_board(moves=None):
    # Board layout
    board_layout_00 = "     |     |     "
    board_layout_01 = "  %s  |  %s  |  %s  \n"
    board_layout_02 = "-" * 18

    if moves is None:
        moves = ([" "] * 10)
    os.system('clear')
    board = []
    layout = board_layout_00 + "\n" + board_layout_01 + board_layout_00

    board.append(layout % (moves[7], moves[8], moves[9]))
    board.append(board_layout_02)
    board.append(layout % (moves[4], moves[5], moves[6]))
    board.append(board_layout_02)
    board.append(layout % (moves[1], moves[2], moves[3]))

    for line in board:
        print(line)


def player_selection():
    players = {1: "", 2: ""}

    while players[1] not in ["X", "O"]:
        players[1] = input("Player 1 - Would you like to play as X or O? : ").upper()
        if players[1] not in ["X", "O"]:
            print("Invalid input - please try again!")

    if players[1] == "X":
        players[2] = "O"
    else:
        players[2] = "X"

    return players


def move_selection(players, current_player, allowed_moves):
    move = 0

    while move not in allowed_moves:
        move = int(input(f"Player {current_player} : where would you like to place {players[current_player]} : "))
        if move not in allowed_moves:
            print(f"Invalid move: Valid moves are {allowed_moves}. Please try again")

    return move


def check_win(played_moves):
    """
    Checks if one of the players has won the game and returns the winner's marker
    :param played_moves: List of all the moves that are played
    :return: The winner: X or O
    """
    win_cases = [(7, 8, 9), (4, 5, 6), (1, 2, 3), (7, 4, 1,), (8, 5, 2), (9, 6, 3), (7, 5, 3), (9, 5, 1)]
    for case in win_cases:
        if played_moves[case[0]] == played_moves[case[1]] == played_moves[case[2]] == "X":
            return "X"
        elif played_moves[case[0]] == played_moves[case[1]] == played_moves[case[2]] == "O":
            return "O"


def play():
    print("Welcome to TIC-TAC-TOE")

    players = player_selection()
    allowed_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    played_moves = [" "] * 10

    display_board(played_moves)
    time.sleep(1)

    game_over = False
    player1_move = True

    while not game_over:

        if player1_move:
            player1_move = move_selection(players, 1, allowed_moves)
            played_moves[player1_move] = players[1]
            allowed_moves.remove(player1_move)
            display_board(played_moves)
            winner = check_win(played_moves)
            player1_move = False
        else:
            player2_move = move_selection(players, 2, allowed_moves)
            played_moves[player2_move] = players[2]
            allowed_moves.remove(player2_move)
            display_board(played_moves)
            winner = check_win(played_moves)
            player1_move = True

        if winner is not None:
            print(f"Winner is {winner}")
            game_over = True
        elif len(allowed_moves) == 0:
            print("GAME OVER! There was no winner")
            game_over = True


play()
