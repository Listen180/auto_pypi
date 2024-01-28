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

#from distutils.core import setup

version_number = input("Input the new version number you are going to use: ")


# Get the long description
with codecs.open('README.rst' ,'r') as f:
    #long_description = '\n{}'.format(f.read())
    long_description = f.read()


setuptools.setup(
#setup(
    name="auto-pypi-setup",
    version=version_number,
    author="Sen LEI",
    author_email="sen.lei@outlook.com",
    description="A Python command line tool to automatically setup and upload your package to PyPi. ",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url="https://github.com/Listen180/autopip",
    packages=setuptools.find_packages(),
    install_requires=[
        'click',
    ],
    license="BSD 3-clause",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    keywords='python, package, pypi, shell, pip, clt, cli, tools, auto',
    entry_points={'console_scripts': [
        'autopypi = autopypi.autopypi:main',
        ]},
)
