#!/bin/bash
# Script to compile RootOutput.cpp to libRootOutput.so

g++ -c -fPIC -std=c++11 -I `root-config --incdir` `root-config --libs` RootOutput.cpp -o RootOutput.o
g++ -shared -Wl,-soname,libfoo.so -std=c++11 -I `root-config --incdir` `root-config --libs` -o libRootOutput.so  RootOutput.o
