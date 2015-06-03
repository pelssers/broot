#!/usr/bin/python
""" Example use of the RootOutput library through the RootWrap wrapper
    Works for both python 2 & 3

    2015, Bart Pelssers
"""

import numpy as np
from broot import RootWrap


# Create a new instance of RootOutput
OUT = RootWrap.RootOutput()

# Create and open a new output file
OUT.create_new_file("test_rootfile.root")

# Create some trees
OUT.create_new_tree("boompje_a")
# OUT.create_new_tree("boompje_b")

# Create some numpy ndarrays, many dtypes are supported.
"""
    Strings can be declared as dtype=np.string but then the number of
    characters will also dictate the maximum string length for a given branch.
    Its better to declare a string as dtype 'aX', with X the maximum number of
    characters.

     ROOT   | C++, ROOT Type             | python (numpy dtypes)
    -----------------------------------------------------
     C      | char string terminated \0  | 'a100' (100 = max length)
     B      | 8 bit signed, Char_t       | int8
     b      | 8 bit unsigned, UChar_t    | uint8
     S      | 16 bit signed, Short_t     | int16
     s      | 16 bit unsigned, UShort_t  | uint16
     I      | 32 bit signed, Int_t       | int32
     i      | 32 bit unsigned, UInt_t    | uint32
     F      | 32 bit signed, Float_t     | float32
     D      | 64 bit signed, Double_t    | float64
     L      | 64 bit signed, Long64_t    | int64
     l      | 64 bit unsigned, ULong64_t | uint64
     O      | bool, Bool_t               | bool_
"""

# ndarrays with ndim > 1 will be flattenend to 1D.
in_data = np.ones((2, 2), dtype=np.float32)
bool_data = np.ones((5, 1), dtype=np.bool)
string_array = np.array([b'Hello ROOT'], dtype=np.dtype('a100'))

# change some values
in_data[0][0] = 1.1
in_data[0][1] = 2.2
in_data[1][0] = 3.3
in_data[1][1] = 4.4

# Create the actual branches
OUT.create_new_branch("boompje_a", "takje_a", in_data)
OUT.create_new_branch("boompje_a", "takje_c", string_array)
OUT.create_new_branch("boompje_a", "takje_b", bool_data)

# fill the tree with a new entry, each branch will be filled with the
# current value of its buffer (indata, string_array, booldata)
OUT.tree_fill("boompje_a")

# Change more values
in_data[0][0] = 10.111
in_data[0][1] = 20.222
in_data[1][0] = 30.333
in_data[1][1] = 40.444

string_array[0] = "Bye ROOT"

bool_data[0] = False
bool_data[1] = True
bool_data[2] = False
bool_data[3] = True
bool_data[4] = False

# Fill the tree with another entry
OUT.tree_fill("boompje_a")

# Write all objects (trees and branches) to the file
OUT.write_all_objects()

# Close the file
OUT.shutdown()
