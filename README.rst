===============================
broot
===============================

.. image:: https://img.shields.io/travis/pelssers/broot.svg
           :target: https://travis-ci.org/pelssers/broot

.. image:: https://img.shields.io/pypi/v/broot.svg
           :target: https://pypi.python.org/pypi/broot


Library for converting python numpy datastructures to the ROOT output format.

* Free software: LGPL 2.1 license
* Documentation: https://broot.readthedocs.org.


The ROOT(https://root.cern.ch/) data analysis framework is used much in High Energy Physics (HEP) and has its own output format (.root). ROOT can be easily interfaced with software written in C++. For software tools in Python there exists pyROOT(https://root.cern.ch/drupal/content/pyroot). Unfortunately pyROOT does not work well with python3.4.

**broot** is a small library that converts data in python numpy ndarrays to ROOT files containing trees with a branch for each array.

The goal of this library is to provide a generic way of writing python numpy datastructures to ROOT files. The library should be portable and supports both python2, python3, ROOT v5 and ROOT v6 (requiring no modifications on the ROOT part, just the default installation). Installation of the library should only require a user to compile to library once or install it as a python package.

Secondly the library can be used to convert other file formats that store information in numpy-like structures, such as HDF5, to ROOT.

Installation
------------

To use broot a user must have installed python, ROOT and be able to compile C++ code.
Then clone the repository and run 'compile.sh' to compile RootOutput.cpp to libRootOutput.so

::
    ./compile.sh

Use
---

To use broot one needs libRootOutput.so and RootWrap.py

RootWrap can be imported in any python file and a new RootOutput instance can be made:

.. code:: python
    import RootWrap

    OUT = RootWrap.RootOutput()

Two example scripts are provided in 'examples'.

- 'convert.py' demonstrates the functions available using some ndarrays.
- 'hdf_to_root.py' is a first implementation of a HDF5 to ROOT converter (HDF5 file not provided).

Current support:
----------------

- python2
- python3.4
- ROOT v5
- ROOT v6
- compiles on gcc versions with c++11
- compiles on gcc versions without c++11 (see branch no-c++11)
- tested on GNU/Linux

Todo list:
----------

- Proper Makefile instead of 'compile.sh'
- Python package
- HDF5 converter class
- OS support for Windows and Mac
- Documentation
