===============================
Langevin-dynamics
===============================


.. image:: https://img.shields.io/travis/xinbian/langevin_dynamics.svg
        :target: https://travis-ci.org/xinbian/langevin_dynamics

.. image:: https://readthedocs.org/projects/langevin-dynamics/badge/?version=latest
        :target: https://langevin-dynamics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/xinbian/langevin_dynamics/shield.svg
     :target: https://pyup.io/repos/github/xinbian/langevin_dynamics/
     :alt: Updates


.. image:: https://codecov.io/gh/xinbian/langevin_dynamics/branch/master/graph/badge.svg
     :target: https://codecov.io/gh/xinbian/langevin_dynamics

A Langevin equation solver:

* input: intial position, velocity, temperature, damping coefficient, time step, total time, and potential energy specified as a file. Potential energy file will be a text-file where each line contains an index, x, U(x), and F(x) separated by spaces.
* output: final position, velocity and a file in the same format as above, except each line contains index, time, position, velocity. 


* Free software: MIT license
* Documentation: https://langevin-dynamics.readthedocs.io.
How to use
---------
* modify the input file in the fold of /langevin_dynamics
* run langevin_dymaics.py

Features
--------

* The intitial position is x=10, where the potential is lowest. The potential is in the form of (2-2x(x-10)^2)^2. The potential at rim (x=0 and x=20) is designed to be very large so that the particle should not get out of the range 0<x<20 (unless the termperature is very very high).
* Euler method is used.
* Linear interpolation is used to get the potential in a specific position, since the potential is given be a discrete table/file.
* The figures of position and velocity are added in the directory of the langevin_dynamics 

Tests
-----------

* I add two test results. You can find it in the source code folder.
* potential given by (2-2x(x-10)^2)^2;intial position x=10; intial velocity=0; Temperature=10, dissipation=2; time step=0.02; total time=50
* zero potential; intial position x=10; intial velocity=0; Temperature=10, dissipation=2; time step=0.02; total time=50
Unit test
------------
*  There are four unit tests.
*  test nstep cal function:
     def test_step(self):
        self.assertEquals(cacl_nstep(1.0, 0.1), 10)
* test the mean of random number is reasonable or not
     def test_random_mean(self):
        self.assertTrue(np.mean(cacl_random(0,1,1000))<1)
* test whether the particle is confined within the potential well which should be by design
     def test_particle_confiment(self):
        self.assertTrue(np.abs(x-10)<10)
* test acceleration caculation
     def test_acce(self):
        self.assertEqual(cacl_acce(1,1,1,1,1), -1)
     



To do
-------
* add some object-oriented features
* make a film of the particle position 
Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

