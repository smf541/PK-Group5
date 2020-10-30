> This library is in ALPHA version. The API is defined but subject to change as we further develop the functionality and our understanding of the product.

# Group 5: Pharmacokinetic Modelling Project

[![codecov](https://codecov.io/gh/smf541/PK-Group5/branch/master/graph/badge.svg)](https://codecov.io/gh/smf541/PK-Group5)

[![BCH compliance](https://bettercodehub.com/edge/badge/smf541/PK-Group5?branch=master)](https://bettercodehub.com/)

[![Documentation Status](https://readthedocs.org/projects/pk-model/badge/?version=latest)](https://pk-model.readthedocs.io/en/latest/?badge=latest)

![Run unittests](https://github.com/smf541/PK-Group5/workflows/Run%20unittests/badge.svg)

![Run on multiple os](https://github.com/smf541/PK-Group5/workflows/Run%20on%20multiple%20os/badge.svg)

# PK Model

This repository contains a Python library for specifying, solving and visualising a pharmacokinetic model. 

## About 

PK Model is a useful library for quantitatively describing the absorption, distribution, metabolism, and excretion of a drug through a patient's system. 

The patient's body is modelled as one or more kinetically homogenous compartments: a primary central compartment into which the drug is administered and excreted, and zero or more peripheral compartments into which the drug may be distributed to/from. For example:

![Image of equation](https://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;q_{c}}{\mathrm{d}&space;t}=&space;Dose\left&space;(&space;t&space;\right&space;)-&space;\frac{q^{_{c}}}{V_{c}}CL&space;-&space;Q_{p1}\left&space;(&space;\frac{q_{c}}{V_{c}}&space;-&space;\frac{q_{p1}}{V_{p1}}\right&space;))

Where:

    - Dose(t) is the drug dose function (dosage with respect to time)
    - Vc [mL] is the volume of the central compartment
    - Vp1 [mL] is the volume of the first peripheral compartment
    - Vp1 [mL] is the volume of the peripheral compartment 
    - CL [mL/h] is the clearance/elimination rate from the central compartment
    - Qp1 [mL/h] is the transition rate between central compartment and peripheral compartment 

This easy-to-use package enables the drug quantity in each comparment to be tracked and visualised at different time points. It is highly versatile, enabling users to alter parameters such as the number of peripheral compartments, the type of dosing, the dosing protocol, and more.

PK Model is an up-and-coming Python package that strives to make pharmacokinetic modelling intuitive and user-friendly by providing a simple yet powerful model of drug delivery. 


## Using the PK Model library


#TODO: Add usage example once classes and functions are defined.


## Installing PK Model and Version Specification

PK Model is compatible with Python versions 3.6+. 

To install the latest release of the PK Model library, simply type the following command into the console:

```bash
python -m pip install --extra-index-url https://test.pypi.org/simple/ pkmodel
```

If you wish to uninstall the library, you can do so using the following command:

```bash
pip uninstall PKModel
```

## Package Documentation and Requirements

Our API Reference and User Guide is available on [Read the Docs](https://pk-model.readthedocs.io/en/latest/ "PK Model Documentation").

The dependencies for this package can be found in the list of [Requirements](https://github.com/smf541/PK-Group5/blob/master/requirements.txt). Note: all dependencies are automatically installed when the PK Model package is installed. 

## Contributing 

For instructions on how to contribute to PK model, see the [Contributor README](https://github.com/smf541/PK-Group5/blob/master/docs/contributor_README.md).



