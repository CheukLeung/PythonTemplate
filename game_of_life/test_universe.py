"""
Testing of Universe class
"""

import unittest
import xmlrunner
import doctest
import universe

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(universe))
    xmlrunner.XMLTestRunner(output="unittests").run(SUITE)
