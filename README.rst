auto_pypi
===========

This is a shell script to auto setup your (updated version) python package onto PyPi. 


Usage
-----

- Copy the ``setup_new_pypi.sh`` file into your python package's root folder (where the ``setup.py`` exists). 

- Run ``setup_new_pypi.sh`` under your python package's root folder in terminal, *providing your package's name* :

  .. code-block:: shell

   $ ./setup_new_pypi.sh your-package-name


- Then you'll be asked to input the new version number to continue. 

- Then you'll be asked to input the username and passcode of PyPi as usual. 
  - Here you'll also be asked to choose whether to use Test PyPi or the real PyPi.
