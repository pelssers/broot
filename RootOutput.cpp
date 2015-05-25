/* RootOutput class
 *
 * Copyright (C) 2015, Bart Pelssers
 * License: GPL v2.0
 */ 

#include <iostream>
#include <string>

#include <TFile.h>
#include <TTree.h>
#include <TBranch.h>


class RootOutput{
 private:
    TFile* out_file;

 public:
    void create_new_output(char* name);
    void close_output();
    void write_all_objects();
    void create_new_tree(char* name);
    void create_new_branch(char* tree_name,
                           char* branch_name,
                           char* branch_type,
                           void* buffer,
                           int length);
    void tree_fill(char* tree_name);
};

void RootOutput::create_new_output(char* name) {
/* Create new TFile with name and open it */

    this->out_file = new TFile(name, "RECREATE");

    if (!this->out_file->IsOpen()) {
        std::cerr << "Could not open file" << std::endl;
        exit(1);
    }

    return;
}

void RootOutput::close_output() {
/* Close the output file */

    this->out_file->Close();
    delete this->out_file;

    return;
}

void RootOutput::write_all_objects() {
/* Write all objects in memory to file */

    this->out_file->Write();

    return;
}

void RootOutput::create_new_tree(char* name) {
/* Create a new TTree */

    TTree* tree = new TTree(name, name);

    return;
}

void RootOutput::create_new_branch(char* tree_name,
                                   char* branch_name,
                                   char* branch_type,
                                   void* buffer,
                                   int length = 1) {
/* Create new TBranch for specific TTree */

    std::string s_branch_type(branch_name);

    if (length > 1)
        s_branch_type.append("[" + std::to_string(length) + "]");

    s_branch_type.append("/" + std::string(branch_type));

    TTree* tree = reinterpret_cast<TTree*>(this->out_file->Get(tree_name));

    tree->Branch(branch_name,
                 reinterpret_cast<void*>(buffer),
                 s_branch_type.c_str());

    return;
}

void RootOutput::tree_fill(char* tree_name) {
/* Fill tree_name with buffer values */

    TTree* tree = reinterpret_cast<TTree*>(this->out_file->Get(tree_name));
    tree->Fill();

    return;
}

// Wrap the above C++ class in C functions callable from python
extern "C" {
    RootOutput* RootOutput_new() { return new RootOutput(); }
    void RootOutput_create_new_output(RootOutput* obj, char* name) {
        obj->create_new_output(name);
    }
    void RootOutput_close_output(RootOutput* obj) {
        obj->close_output();
    }
    void RootOutput_write_all_objects(RootOutput* obj) {
        obj->write_all_objects();
    }
    void RootOutput_create_new_tree(RootOutput* obj, char* name) {
        obj->create_new_tree(name);
    }
    void RootOutput_create_new_branch(RootOutput* obj,
                                      char* tree_name,
                                      char* branch_name,
                                      char* branch_type,
                                      void* buffer,
                                      int length) {
        obj->create_new_branch(tree_name,
                               branch_name,
                               branch_type,
                               buffer,
                               length);
    }
    void RootOutput_tree_fill(RootOutput* obj, char* tree_name) {
        obj->tree_fill(tree_name);
    }
}
