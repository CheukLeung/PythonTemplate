"""
Testing of Pixel class
"""

import unittest
import xmlrunner
import doctest
import pixel

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(pixel))
    xmlrunner.XMLTestRunner(output="unittests").run(SUITE)
