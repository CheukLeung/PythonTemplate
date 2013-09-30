"""A pypi demonstration vehicle.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>

"""
import time
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pixel
import universe

def start():
    "This starts this module running ..."
    uni = universe.Universe(20)
    print uni.display()
    for index in range(10):
        time.sleep(1)
        uni.step()
        print uni.display()
start()
