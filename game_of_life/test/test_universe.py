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
import pixel

UNIVERSE_1 = "------------------------------------------\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|\n\
------------------------------------------"

UNIVERSE_2 = "------------------------------------------\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
|                                        |\n\
------------------------------------------"

class Mock_pixel(object):

    def __init__(self, x_i, y_i, live):
        self.live = True
        self.next_live = False

    def is_live(self):
        return self.live

    def get_symbol(self):
        if self.live:
            return 'O'
        else:
            return ' '

    def step(self):
        self.live = self.next_live

    def set_next_live(self, next_live):
        return


class Test(unittest.TestCase):
    @mock.patch('pixel.Pixel', Mock_pixel)
    def test_display(self):
        uni = universe.Universe()
        self.assertEqual(uni.display(), UNIVERSE_1)
        uni.step()
        self.assertEqual(uni.display(), UNIVERSE_2)


if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(universe))
    xmlrunner.XMLTestRunner(output="unittests").run(SUITE)
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="unittests"))
