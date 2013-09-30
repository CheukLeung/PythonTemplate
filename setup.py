import os
from setuptools import setup

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "game_of_life",
    version = "0.0.5",
    author = "Cheuk",
    author_email = "cheuk.wingleung@xdin.com",
    packages=['game_of_life', 'game_of_life.test'],
    scripts=['bin/run_game.py'],
    url = "",
    license = "LICENSE.txt",
    description = ("An demonstration of how to create, document, and publish "
				   "to the cheese shop a5 pypi.org."),
    long_description=read('README'),
    keywords = "example documentation tutorial",
    install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
    ],
)
