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
      zip_safe=False,
      setup_requires="numpy",
      install_requires=["matplotlib","scipy","numpy","emcee","corner"],
      package_data={"":["*.h","src/*.h"]},
      classifiers=['Programming Language :: Python'],
      ext_modules=[ext])