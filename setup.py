from setuptools import setup, find_packages

import sys
import os.path
sys.path.insert(0, os.path.abspath('.'))
from snortparser import __version__

with open('requirements.txt') as f:
    _requirements = f.read().splitlines()

with open('README.md') as f:
    _long_description = f.read()

setup(
    name='snortparser',
    version=__version__,
    url='https://github.com/jtschichold/snortparser',
    author='Luigi Mori',
    author_email='l@isidora.org',
    description='Parser for Snort rules',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
        'Topic :: Internet'
    ],
    long_description=_long_description,
    packages=find_packages(),
    install_requires=_requirements
)
