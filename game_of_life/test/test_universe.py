"""
Testing of Universe class
"""

import unittest
import xmlrunner
import doctest
import mock
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import universe

UNIVERSE_1 = \
"-------\n\
|OOOOO|\n\
|OOOOO|\n\
|OOOOO|\n\
|OOOOO|\n\
|OOOOO|\n\
-------"

UNIVERSE_2 = \
"-------\n\
|     |\n\
|     |\n\
|     |\n\
|     |\n\
|     |\n\
-------"

UNIVERSE_3 = \
"-------\n\
|O O O|\n\
| O O |\n\
|O O O|\n\
| O O |\n\
|O O O|\n\
-------"

pixels = [['O',' ','O',' ','O'], \
[' ','O',' ','O',' '], \
['O',' ','O',' ','O'], \
[' ','O',' ','O',' '], \
['O',' ','O',' ','O']]

class Mock_pixel(object):

    def __init__(self, x_i, y_i, live):
        self.live = True

    def is_live(self):
        return self.live

    def get_symbol(self):
        if self.live:
            return 'O'
        else:
            return ' '

    def step(self):
        self.live = False

    def set_next_live(self, next_live):
        return


class Test(unittest.TestCase):
    @mock.patch('pixel.Pixel', Mock_pixel)
    def test_display(self):
        uni = universe.Universe(dim_x=5, dim_y=5)
        self.assertEqual(uni.display(), UNIVERSE_1)
        uni.step()
        self.assertEqual(uni.display(), UNIVERSE_2)
        
    def test_set_universe(self):
        uni = universe.Universe(dim_x=5, dim_y=5)
        uni.set_universe(pixels)
        self.assertEqual(uni.display(), UNIVERSE_3)

    def test_get_neigbour(self):
        uni = universe.Universe(dim_x=5, dim_y=5)
        expected = [{'y': 1, 'x': 1}, {'y': 2, 'x': 1}, {'y': 3, 'x': 1}, \
                    {'y': 1, 'x': 2}, {'y': 3, 'x': 2}, {'y': 1, 'x': 3}, \
                    {'y': 2, 'x': 3}, {'y': 3, 'x': 3}]
        self.assertEqual(uni.get_neigbour(2,2), expected) 

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(universe))
    xmlrunner.XMLTestRunner(output="unittests").run(SUITE)
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="unittests"))
