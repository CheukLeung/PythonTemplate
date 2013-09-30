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

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(pixel))
    xmlrunner.XMLTestRunner(output="unittests").run(SUITE)
