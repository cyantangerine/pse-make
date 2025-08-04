from setuptools import setup, Extension
import pybind11
ext_modules = [ Extension(
'pse', ['pse.cpp'],
include_dirs=[pybind11.get_include()],
language='c++', ),
]
setup(ext_modules=ext_modules)