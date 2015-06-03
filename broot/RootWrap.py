# -*- coding: utf-8 -*-
"""Module to wrap the RootOutput C++ class

   2015 Bart Pelssers
   GPL v2.0
"""

import os
from ctypes import cdll, c_void_p


source_dir = os.path.dirname(os.path.abspath(__file__))
lib = cdll.LoadLibrary(source_dir + '/lib/libRootOutput.so')


class RootOutput(object):
    """Class providing wrappers to the C++ class"""

    def __init__(self):
        """Constructor"""

        self.type_convert = {'a': 'C',
                             'int8': 'B',
                             'uint8': 'b',
                             'int16': 'S',
                             'uint16': 's',
                             'int32': 'I',
                             'uint32': 'i',
                             'float32': 'F',
                             'foat64': 'D',
                             'int64': 'L',
                             'uint64': 'l',
                             'bool': 'O'}

        self.obj = lib.RootOutput_new()

    def create_new_file(self, name):
        """Create a new TFile with name"""

        lib.RootOutput_create_new_output(self.obj, name.encode('utf-8'))

    def shutdown(self):
        """Close TFile"""

        lib.RootOutput_close_output(self.obj)

    def write_all_objects(self):
        """Write all objects in memory to TFile
           (Objects being the defined Trees and Branches)
        """

        lib.RootOutput_write_all_objects(self.obj)

    def create_new_tree(self, name):
        """Create a new TTree with name"""

        lib.RootOutput_create_new_tree(self.obj, name.encode('utf-8'))

    def create_new_branch(self, tree_name, branch_name, buffer):
        """Create new branch with branch_name for certain tree_name.
           buffer should be a numpy ndarray of a supported branch type.
        """

        sdtype = str(buffer.dtype)
        if sdtype.startswith('|S') or sdtype.startswith('S'):
            branch_type = 'C'
        elif sdtype in self.type_convert.keys():
            branch_type = self.type_convert[sdtype]
        else:
            raise KeyError()
            return

        lib.RootOutput_create_new_branch(self.obj,
                                         tree_name.encode('utf-8'),
                                         branch_name.encode('utf-8'),
                                         branch_type.encode('utf-8'),
                                         c_void_p(buffer.ctypes.data),
                                         buffer.size)

    def tree_fill(self, tree_name):
        """Fill TTree tree_name with a new entry for each buffer"""

        lib.RootOutput_tree_fill(self.obj, tree_name.encode('utf-8'))
