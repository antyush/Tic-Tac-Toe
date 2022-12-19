import unittest
from week6_logic import Week6_TicTacToe

class TestLogic(unittest.TestCase):
    
    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X']
        ]
        self.assertEqual(week6_logic.get_winner(board), 'X')

    def test_other_player(self):
        self.assertEqual(week6_logic.other_player('X'), 'O')
        self.assertEqual(week6_logic.other_player('O'), 'X')
    
        
if __name__ == '__main__':
    unittest.main()