#!/usr/bin/env python3

import sys
import numpy

if sys.version_info[0] < 3:
    sys.exit('Sorry, Python < 3.x is not supported')

# Try using setuptools first, if it's installed
from setuptools import setup, find_packages
from setuptools.extension import Extension

# set up binding polynomial C extension
ext = Extension('pytc.indiv_models.bp_ext',['src/_bp_ext.c'], include_dirs=[numpy.get_include()])

# Need to add all dependencies to setup as we go!
setup(name='pytc-fitter',
      packages=find_packages(),
      version='1.1.5',
      author='Michael J. Harms',
author_email='harmsm@gmail.com',
url='https://github.com/harmslab/pytc',
download_url='https://github.com/harmslab/pytc/tarball/1.1.5',
      description="Python software package for analyzing Isothermal Titration Calorimetry data",
      zip_safe=False,
      package_data={"":["*.h","src/*.h"]},
      ext_modules=[ext])