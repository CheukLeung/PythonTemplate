import os
from setuptools import setup

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "example",
    version = "0.0.5",
    author = "Cheuk",
    author_email = "cheuk.wingleung@xdin.com",
    packages=['example', 'example.test'],
    scripts=['bin/example.py','bin/wash-towels.py'],
    url = "http://packages.python.org/an_example_pypi_project",
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
