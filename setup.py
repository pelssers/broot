#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess


try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

from Cython.Distutils import build_ext
from distutils.command.build_clib import build_clib
from distutils import log


def root_flags(root_config='root-config'):
    root_incdir = subprocess.Popen(
        [root_config, '--incdir'],
        stdout=subprocess.PIPE).communicate()[0].strip()
    root_ldflags = subprocess.Popen(
        [root_config, '--libs'],
        stdout=subprocess.PIPE).communicate()[0].strip()
    if sys.version > '3':
        root_incdir = root_incdir.decode('utf-8')
        root_ldflags = root_ldflags.decode('utf-8')
    return root_incdir.split(), root_ldflags.split()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

test_requirements = requirements + ['flake8',
                                    'tox',
                                    'coverage',
                                    'bumpversion']

lib_build_paths = []
root_incdir, root_libdir = root_flags()

class build_libRootOutput(build_clib):
    def build_libraries(self, libraries):
        for (lib_name, build_info) in libraries:
            sources = build_info.get('sources')
            sources = list(sources)

            log.info("building '%s' library", lib_name)
            include_dirs = build_info.get('include_dirs')
            extra_compile_args = build_info.get('extra_compile_args')
            extra_link_args = build_info.get('extra_link_args')
            objects = self.compiler.compile(sources,
                                            output_dir=self.build_temp,
                                            include_dirs=include_dirs,
                                            extra_preargs=extra_compile_args,
                                            extra_postargs=extra_link_args,
                                            debug=self.debug,
                                            )

            self.compiler.link_shared_object(objects,
                                             'lib' + lib_name + '.so',
                                             output_dir=self.build_clib,
                                             extra_preargs=extra_compile_args,
                                             extra_postargs=extra_link_args,
                                             debug=self.debug)

            lib_build_paths.append(('broot/lib', [self.build_clib + '/lib' + lib_name + '.so']))



libRootOutput = ('RootOutput', {'sources': ['broot/src/RootOutput.cpp'],
                                'include_dirs': root_incdir,
                                'extra_compile_args': ['-std=c++11',
                                                       '-Wno-unused-function',
                                                       '-Wno-unused-variable'],
                                'language': 'c++',
                                'extra_link_args': root_libdir,
                               })


setup(
    name='broot',
    version='0.1.0',
    description="Library for converting python numpy datastructures to the ROOT output format.",
    long_description=readme + '\n\n' + history,
    author="Bart Pelssers",
    author_email='bartp@nikhef.nl',
    url='https://github.com/pelssers/broot',
    packages=[
        'broot',
    ],
    package_dir={'broot':
                 'broot'},
    include_package_data=True,
    install_requires=requirements,
    libraries=[libRootOutput],
    cmdclass={'build_clib': build_libRootOutput,
              'build_ext': build_ext},
    data_files=lib_build_paths,
    license="GPL2",
    zip_safe=False,
    keywords='broot',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: C++',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
