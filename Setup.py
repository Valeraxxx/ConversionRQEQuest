from setuptools import setup
from Cython.Build import cythonize

path = str
setup(
  name="Bmod"
  ext_modules=cythonize(include_path=[])
)


