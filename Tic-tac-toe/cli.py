# This is the main file

from logic import make_empty_board
from logic import print_board
from logic import get_winner
from logic import other_player

def player():
    """Defines who the current player is"""
    return

def input_X(board):
    x = int(input("Choose a row (1, 2, 3): "))
    y = int(input("Choose a column (1, 2, 3): "))
    if (x >= 1 or x <= 3) and (y >= 1 or y <= 3) and (board[x-1][y-1] == None):
        board[x - 1][y - 1] = 'X'
        return(board)
    else:
        print("Try again. This coordinate out of bounds or already taken.")
        input_X(board)

def input_O(board):
    x = int(input("Choose a row (1, 2, 3): "))
    y = int(input("Choose a column (1, 2, 3): "))
    if (x >= 1 or x <= 3) and (y >= 1 or y <= 3) and (board[x-1][y-1] == None): 
        board[x - 1][y - 1] = 'O'
        return(board)
    else:
        print("Try again. This coordinate out of bounds or already taken.")
        input_O(board)

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    
    player1 = input("Player 1, choose a character (X or O): ")
    player2 = ""
    if player1 == 'X' or player1 == 'x':
        player1 = 'X'
        player2 = 'O'
    if player1 == 'O' or player1 == 'o':
        player1 = 'O'
        player2 = 'X'

    print("Player 1 is " + player1)
    print("Player 2 is " + player2)
    player = player1

    while winner == None:
        print("TODO: take a turn!")

        # TODO: Show the board to the user
        print_board(board)

        # TODO: Input a move from the player
        if player == 'X':
            input_X(board)
            winner = get_winner(board)
            if winner == player:
                print_board
                print(player + " is the winner!")
                break
        else:
            input_O(board)
            winner = get_winner(board)
            if winner == 'O':
                print_board
                print(player + " is the winner!")
                break
        print(winner)
        # TODO: Update the board
        print("Board has been updated!")

        # TODO: Update whose turn it is.
        player = other_player(player)
        print("Now it is " + player + "'s turn!")
