#!/bin/bash

g++ -c -fPIC -I `root-config --incdir` `root-config --libs` RootOutput.cpp -o RootOutput.o
g++ -shared -Wl,-soname,libfoo.so -I `root-config --incdir` `root-config --libs` -o libRootOutput.so  RootOutput.o
