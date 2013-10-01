"""
Testing of Pixel class
"""

import unittest
import xmlrunner
import doctest
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pixel

class Test(unittest.TestCase):

    def test_unit(self):
        pix = pixel.Pixel(0, 0, True)
        self.assertTrue(pix.is_live())
        self.assertEqual(pix.get_symbol(), 'O')
        pix.set_next_live(False)
        pix.step()
        self.assertFalse(pix.is_live())
        self.assertEqual(pix.get_symbol(), ' ')

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(pixel))
    xmlrunner.XMLTestRunner(output="unittests").run(SUITE)
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="unittests"))
