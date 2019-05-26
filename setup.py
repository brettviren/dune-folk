#!/usr/bin/env python
from glob import glob
from setuptools import setup

setup(name='dune-folk',

      # fixme: should make a dune-python to that does not much more
      # than provides the top-level "dune" module and maybe some
      # README describing how to add new submodules.

      provides = [ 'dune', "dune.folk" ],
      requires = ['dune'],
      version='0.0.0',
      description='Module and command line interface to muck with DUNE collaboration info',
      url='https://github.com/DUNE/dune-folk',
      author='Brett Viren',
      author_email='bv@bnl.gov',
      packages = ['dune', 'dune.folk'],
      #data_files = [],
      install_requires = [l for l in open("requirements.txt").readlines() if l.strip()],
      entry_points='''
      [console_scripts]
      dune-folk=dune.folk.main:main
      ''',
      )
