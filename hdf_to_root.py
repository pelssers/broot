#!/usr/bin/python3
""" HDF5 to ROOT converter using the RootOutput library.
    Written for python3.

    2015, Bart Pelssers
"""

from tqdm import tqdm
import numpy as np

import h5py

import RootWrap


in_file = "xe100_120403_0107_000000_light.hdf5"
out_file = "converted_file.root"

file = h5py.File(in_file, 'r')

OUT = RootWrap.RootOutput()
OUT.create_new_file(out_file)

branch_buffers = {}

# ignore some fields
ignore_fields = [  # 'Event',
                 # 'Peak',
                 # 'ReconstructedPosition',
                 'user_float_0',
                 'user_float_1',
                 'user_float_2',
                 'user_float_3',
                 'user_float_4']


# Create all Trees and Branches
for tree_name in file.keys():
    print("Adding tree '%s' to file '%s'" % (tree_name, out_file))
    OUT.create_new_tree(tree_name)
    branch_buffers[tree_name] = {}

    dataset = file[tree_name]
    data_fields = dataset.dtype.fields.items()
    for branch_name, type in data_fields:
        if branch_name in ignore_fields:
            continue

        print("New branch '%s' in tree '%s'" % (branch_name, tree_name))

        branch_buffers[tree_name][branch_name] = np.zeros(1, dtype=type[0])
        OUT.create_new_branch(tree_name,
                              branch_name,
                              branch_buffers[tree_name][branch_name])

# Loop on events, Tree by Tree, Branch by Branch
for tree_name in file.keys():

    print("Filling Tree '%s'" % tree_name)
    dataset = file[tree_name]
    data_fields = dataset.dtype.fields.items()
    events = dataset.value
    for event in tqdm(events):
        for branch_name, type in data_fields:
            if branch_name in ignore_fields:
                continue

            branch_buffers[tree_name][branch_name][0] = event[branch_name]

        OUT.tree_fill(tree_name)

OUT.write_all_objects()
OUT.shutdown()
file.close()
