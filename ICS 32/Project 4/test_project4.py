import mechanics
import unittest

class GameTest(unittest.TestCase):

    def setUp(self):
        self._game = mechanics.Game([['   ', '   ','   '],
                                     ['   ', '   ','   '],
                                     ['   ', '   ','   '],
                                     ['   ', '   ','   '],
                                     ['   ', '   ','   '],
                                     ['   ', '   ','   ']], 4, 3)

    def test_faller_rotates(self):
        self._game._board = [['   ', '   ','   '],
                             ['   ', '   ','   '],
                             ['   ', '   ','[S]'],
                             ['   ', '   ','[T]'],
                             ['   ', '   ','[V]'],
                             ['   ', '   ','   ']]
        
        self.assertEqual(self._game.rotate(),
                         [['   ', '   ','   '],
                          ['   ', '   ','   '],
                          ['   ', '   ','[V]'],
                          ['   ', '   ','[S]'],
                          ['   ', '   ','[T]'],
                          ['   ', '   ','   ']])

    def test_faller_moves_left(self):
        self._game._board = [['   ', '   ','   '],
                             ['   ', '   ','   '],
                             ['   ', '   ','[S]'],
                             ['   ', '   ','[T]'],
                             ['   ', '   ','[V]'],
                             ['   ', '   ','   ']]
        
        self.assertEqual(self._game.move_left(), [['   ', '   ','   '],
                                                  ['   ', '   ','   '],
                                                  ['   ', '[S]','   '],
                                                  ['   ', '[T]','   '],
                                                  ['   ', '[V]','   '],
                                                  ['   ', '   ','   ']])

        self.assertEqual(self._game.move_left(), [['   ', '   ','   '],
                                                  ['   ', '   ','   '],
                                                  ['[S]', '   ','   '],
                                                  ['[T]', '   ','   '],
                                                  ['[V]', '   ','   '],
                                                  ['   ', '   ','   ']])

    def test_faller_moves_right(self):
        self._game._board = [['   ', '   ','   '],
                             ['   ', '   ','   '],
                             ['[S]', '   ','   '],
                             ['[T]', '   ','   '],
                             ['[V]', '   ','   '],
                             ['   ', '   ','   ']]

        self.assertEqual(self._game.move_right(),
                         [['   ', '   ','   '],
                          ['   ', '   ','   '],
                          ['   ', '[S]','   '],
                          ['   ', '[T]','   '],
                          ['   ', '[V]','   '],
                          ['   ', '   ','   ']])

        self.assertEqual(self._game.move_right(),
                         [['   ', '   ','   '],
                          ['   ', '   ','   '],
                          ['   ', '   ','[S]'],
                          ['   ', '   ','[T]'],
                          ['   ', '   ','[V]'],
                          ['   ', '   ','   ']])
        

    def test_pieces_match(self):
        self._game._board = [[' T ', '   ','   '],
                             ['   ', ' T ','   '],
                             [' W ', '   ',' T '],
                             [' W ', '   ',' S '],
                             [' W ', ' S ','   '],
                             [' S ', ' S ',' S ']]

        self.assertEqual(self._game.replace_matching(),
                         [['*T*', '   ','   '],
                          ['   ', '*T*','   '],
                          ['*W*', '   ','*T*'],
                          ['*W*', '   ','*S*'],
                          ['*W*', '*S*','   '],
                          ['*S*', '*S*','*S*']])



    def test_pieces_fill_empty_space(self):
        self._game._board = [[' S ', '   ',' V '],
                             ['   ', '   ','   '],
                             [' T ', '   ','   '],
                             ['   ', ' Y ','   '],
                             [' W ', ' X ','   '],
                             ['   ', '   ',' V ']]

        self.assertEqual(self._game.fill_empty_space(),
                         [['   ', '   ','   '],
                          ['   ', '   ','   '],
                          ['   ', '   ','   '],
                          [' S ', '   ','   '],
                          [' T ', ' Y ',' V '],
                          [' W ', ' X ',' V ']])


    def test_freeze_faller_if_landed(self):
        self._game._board = [['   ', '   ','   '],
                             ['   ', '   ','   '],
                             ['   ', '   ','[Z]'],
                             ['[S]', '   ','[Y]'],
                             ['[T]', '   ','[X]'],
                             ['[V]', '   ',' W ']]

        self.assertEqual(self._game.freeze_faller(),
                         [['   ', '   ','   '],
                          ['   ', '   ','   '],
                          ['   ', '   ','|Z|'],
                          ['|S|', '   ','|Y|'],
                          ['|T|', '   ','|X|'],
                          ['|V|', '   ',' W ']])

    def test_unfreeze_faller_if_moved(self):
        self._game._board = [['   ', '   ', '   '],
                             ['   ', '   ', '   '],
                             ['   ', '   ', '|Z|'],
                             ['   ', '   ', '|Y|'],
                             ['   ', '   ', '|X|'],
                             ['   ', '   ', ' W ']]

        self.assertEqual(self._game.move_left(), self._game.unfreeze_faller(),
                         [['   ', '   ', '   '],
                          ['   ', '   ', '   '],
                          ['   ', '[Z]', '   '],
                          ['   ', '[Y]', '   '],
                          ['   ', '[X]', '   '],
                          ['   ', '   ', ' W ']])

    def test_if_faller_is_falling(self):
        self._game._board = [['   ', '   ', '   '],
                             ['   ', '   ', '[S]'],
                             ['   ', '   ', '[T]'],
                             ['   ', '   ', '[V]'],
                             ['   ', '   ', '   '],
                             ['   ', '   ', '   ']]

        self.assertEqual(self._game.falling(),
                         [['   ', '   ', '   '],
                          ['   ', '   ', '   '],
                          ['   ', '   ', '[S]'],
                          ['   ', '   ', '[T]'],
                          ['   ', '   ', '[V]'],
                          ['   ', '   ', '   ']])


    

if __name__ == '__main__':
    unittest.main()
        
