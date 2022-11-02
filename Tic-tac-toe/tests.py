import unittest
import logic

class TestLogic(unittest.TestCase):
    
    def test_get_winner(self):
        board = [
            ['X', None, 'O']
            [None, 'X', None]
            [None, 'O', 'X']
        ]
    self.assertEqual(logic.get_winner(board), 'X')

if __name__ == '__main__':
    unittest.main()

