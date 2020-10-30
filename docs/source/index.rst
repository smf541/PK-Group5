.. pkmodel documentation master file, created by
   sphinx-quickstart on Fri Oct 23 10:11:44 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the PK Model documentation!
==========================================

We hope that you will find this page helpful as you learn to use the PKModel 
library! You can use the functions we provided to specify, solve, and visualise 
the absorption, distribution, metabolism and clearance of a drug. The body is 
here modelled as a group of homogeneous compartments.

Below you can find documentation on all the methods and functions you might want to use: 

* The Model class lets you specify the parameters of your pharmacokinetic model, for example the volumes and clearance rates of the central and peripheral compartments.

* The Protocol class lets you define how the drug is administered, the size of the initial dose and the time span over which to simulate the metabolism of the drug.

* The Solution Class allows you to solve the model using a SciPy ODE solver and visualise the amount of the drug in the central compartment over time using MatPlotLib.


Join our `GitHub Repo <https://github.com/smf541/PK-Group5>`_ to work with us on this library!

.. toctree::
   :maxdepth: 2
   :caption: Contents

   quickstart

Documentation
===============
.. automodule:: pkmodel.model

.. automodule:: pkmodel.solution
.. autoclass:: Solution
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
