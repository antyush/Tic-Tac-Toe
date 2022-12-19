# This file is where game logic lives. No input
# or output happens here. The logic in this file

import random
import pandas as pd

class Game_Data:
    def __init__(self) -> None:
        self.path = "tic-tac-toe-data.csv"
        try:
            with open("tic-tac-toe-data.csv"):
                self.games = pd.read_csv(self.path, index_col=0)
        except FileNotFoundError:
            self.games = pd.DataFrame(
                columns=[
                    "game_id",
                    "X",
                    "O",
                    "winner",
                    "char_winner",
                    "turn1",
                    "turn2",
                    "turn3",
                    "turn4",
                    "turn5",
                    "turn6",
                    "turn7",
                    "turn8",
                    "turn9"
                ]
            )

    # Create a new game
    def insert_new_game(self, game_id, X, O):
        self.games = self.games.append(
            {"game_id": game_id, "X": X, "O": O},
            ignore_index=True,
        )
        self.save()

    # Insert a turn into the database
    def insert__new_move(self, game_id, turn_num, coordinates):
        game = self.games[self.games["game_id"] == game_id]
        if len(game) == 0:
            return False
        move_column = "move" + str(turn_num)
        self.games.loc[self.games["game_id"] ==
                       game_id, move_column] = coordinates
        self.save()
        return True

    # Update the databse with a winner
    def update_winner(self, game_id, winner, char_win):
        game = self.games[self.games["game_id"] == game_id]
        if len(game) == 0:
            return False
        self.games.loc[self.games["game_id"] == game_id, "winner"] = winner
        self.games.loc[self.games["game_id"] ==
                       game_id, "char_winner"] = char_win
        self.save()
        return True

    # return all of the games
    def all(self):
        return self.games

    # Return a game based on the ID it has been assigned
    def game_by_id(self, game_id):
        return self.games[self.games["game_id"] == game_id]

    def stats(self):
        games = self.games
        total = len(games)
        if total == 0:
            return {
                "total": 0,
                "player_wins": 0,
                "bot_wins": 0
            }

    # Save the DataFrame to the CSV file
    def save(self):
        self.games.to_csv(self.path)


class Week6_TicTacToe:

    player = None #this variable represents the current player who is taking a turn
    board = None
    winner = None
    type = None
    bot = None

    def __init__(self): # what to do at the start of the program
        # initalize an empty board
        self.board = [[None, None, None],
            [ None, None, None],
            [None, None, None]]

        #ask the user for single or multiplayer

    def game_type(self, type_of_game):
        # print(type(type_of_game))
        if type_of_game == '1':
            self.single_player()
        elif type_of_game == '2':
            self.multi_player()
       
    def single_player(self):
        self.player = input('Would like you like to be X or O?: ').upper()
        return(self.player)    
    
    def multi_player(self):
        player1 = input("Choose a character (X or O): ").upper()
        self.player = player1
        player2 = None
        player2 = self.other_player(player1)

    def print_board(self):
        """Prints the board"""
        for row in self.board:
            print(row)

    def get_winner(self):
        """Determines the winner of the given board.
        Returns X, O, or None"""
        if self.board[0][0] == self.board[1][0] == self.board[2][0]:
            self.winner = self.board[0][0]
            return(self.winner)
        if self.board[0][1] == self.board[1][1] == self.board[2][1]:
            self.winner = self.board[0][1]
            return(self.winner)
        if self.board[0][2] == self.board[1][2] == self.board[2][2]:
            self.winner = self.board[0][2]
            return(self.winner)
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            self.winner = self.board[0][0]
            return(self.winner)
        if self.board[1][0] == self.board[1][1] == self.board[1][2]:
            self.winner = self.board[1][1]
            return(self.winner)
        if self.board[2][0] == self.board[2][1] == self.board[2][2]:
            self.winner = self.board[2][0]
            return(self.winner)
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.winner = self.board[0][0]
            return(self.winner)
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.winner = self.board[0][2]
            return(self.winner)
        else:
            return(None)

    def other_player(self, current_player):
        """Given the character for a player, return the other player"""
        if current_player == 'X':
            return('O')
        elif current_player == 'O':
            return('X')
    
    def bot_action(self):
        # pick a random x coordinate from 1-3 and random y coordinate 1-3
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if (x >= 1 or x <= 3) and (y >= 1 or y <= 3) and (self.board[x-1][y-1] == None):
            self.board[x - 1][y - 1] = self.bot # place character here
            self.print_board()
            return(self.board)
        else:
            self.bot_action()