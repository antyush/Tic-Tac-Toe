# This file is where game logic lives. No input
# or output happens here. The logic in this file

def make_empty_board():
    return[
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

def get_winner(board):
    """Determines the winner of the given board.
    Returns X, O, or None"""
    winner = ''
    if board[0][0] == board[1][0] == board[2][0]:
        winner = board[0][0]
        return(winner)
    if board[0][1] == board[1][1] == board[2][1]:
        winner = board[0][1]
        return(winner)
    if board[0][2] == board[1][2] == board[2][2]:
        winner = board[0][2]
        return(winner)
    if board[0][0] == board[0][1] == board[0][2]:
        winner = board[0][0]
        return(winner)
    if board[1][1] == board[1][1] == board[1][2]:
        winner = board[1][1]
        return(winner)
    if board[2][0] == board[2][1] == board[2][2]:
        winner = board[2][0]
        return(winner)
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return(winner)
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return(winner)
    else:
        draw = "None"
        return(draw)

def other_player(player):
    """Given the character for a player, return the other player"""
    if player == 'X':
        return('O')
    if player == 'O':
        return('X')