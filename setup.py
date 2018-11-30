#!/Users/leisen/anaconda3/bin/python3
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-30 11:53
# * Last modified : 2018-11-30 11:53
# * Filename      : setup.py
# * Description   : 
# *********************************************************

import setuptools
import sys
import codecs

from distutils.core import setup

version_number = input("Input the new version number you are going to use: ")


# Get the long description
with codecs.open('README.rst' ,'r') as f:
    #long_description = '\n{}'.format(f.read())
    long_description = f.read()


#setuptools.setup(
setup(
    name="auto_pypi",
    version=version_number,
    author="Sen LEI",
    author_email="sen.lei@outlook.com",
    description="A package to automatically setup and upload your package to PyPi. ",
    long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/Dual-Points/dplearn",
    packages=setuptools.find_packages(),
    license="BSD 3-clause",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        #"License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    keywords='python package pypi shell',
)
