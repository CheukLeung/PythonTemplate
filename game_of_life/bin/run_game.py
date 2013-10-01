"""Runner of game of life
argv[1] state the number of steps to be done
"""
import time
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pixel
import universe


if (len(sys.argv) > 1):
    # Number of steps to be done (default=infinity)
    TIME = int(sys.argv[1])
    # Flag to state if it should run for infinity times
    FOREVER = False
else:
    TIME = 0
    FOREVER = True

def start():
    # Create the universe
    uni = universe.Universe(20)
    print uni.display()

    # Step through the universe
    index = 0
    while index < TIME or FOREVER:
        time.sleep(1)
        uni.step()
        print uni.display()
        index = index + 1

start()
