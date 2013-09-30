"""
Testing of Universe class
"""

import unittest
import xmlrunner
import doctest
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import universe

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(universe))
    xmlrunner.XMLTestRunner(output="unittests").run(SUITE)
