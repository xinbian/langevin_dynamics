===============================
Langevin-dynamics
===============================


.. image:: https://img.shields.io/pypi/v/langevin_dynamics.svg
        :target: https://pypi.python.org/pypi/langevin_dynamics

.. image:: https://img.shields.io/travis/xinbian/langevin_dynamics.svg
        :target: https://travis-ci.org/xinbian/langevin_dynamics

.. image:: https://readthedocs.org/projects/langevin-dynamics/badge/?version=latest
        :target: https://langevin-dynamics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/xinbian/langevin_dynamics/shield.svg
     :target: https://pyup.io/repos/github/xinbian/langevin_dynamics/
     :alt: Updates


a langevin dynamics project


* Free software: MIT license
* Documentation: https://langevin-dynamics.readthedocs.io.


Features
--------

* The intitial position is x=10, where the potential is lowest. The potential at rim (x=0 and x=20) is designed to be very large so that the particle should not get out of the range 0<x<20 (unless the termperature is very very high).
* Euler method is used.
* Linear interpolation is used to get the potential in a specific position, since the potential is given be a discrete table/file.
* The figures of position and velocity are added in the directory of the langevin_dynamics 
* My code coverage is 100%, but the total code coverage is not 100% because of a file cli.py, gengerated by cookiecutter. I need to keep this file to pass the test.
Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

