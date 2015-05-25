# broot
Library for converting python numpy datastructures to the ROOT output format.

The [ROOT](https://root.cern.ch/) data analysis framework is used much in High Energy Physics (HEP) and has its own output format (.root). ROOT can be easily interfaced with software written in C++. For software tools in Python there exists [pyROOT](https://root.cern.ch/drupal/content/pyroot). Unfortunately pyROOT does not work well with python3.4.

**broot** (pronounced 'brute') is a small library that converts data in python numpy ndarrays to ROOT files containing trees with a branch for each array.

The goal of this library is to provide a generic way of writing python numpy datastructures to ROOT files. The library should be portable and supports both python2, python3, ROOT v5 and ROOT v6 (requiring no modifications on the ROOT part, just the default installation). Installation of the library should only require a user to compile to library once or install it as a python package.

Secondly the library can be used to convert other file formats that store information in numpy-like structures, such as HDF5, to ROOT.

### Current support:

* python2 :white_check_mark:
* python3.4 :white_check_mark:
* ROOT v5 :white_check_mark:
* ROOT v6 :white_check_mark:
* compiles on gcc versions with c++11 :white_check_mark:
* compiles on gcc versions without c++11 (see branch no-c++11) :white_check_mark:
* tested on GNU/Linux :white_check_mark:

### Todo list:

* Proper Makefile instead of 'compile.sh'
* Python package
* HDF5 converter class
* OS support for Windows and Mac
