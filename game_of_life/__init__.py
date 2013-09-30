"""A pypi demonstration vehicle.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>

"""
import time
import universe
import pixel


def start():
    "This starts this module running ..."
    uni = universe.Universe(20)
    print uni.display()
    while True:
        time.sleep(1)
        uni.step()
        print uni.display()
start()
