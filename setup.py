#!/usr/bin/env python
import os
from distutils.core import setup


def readme_or_docstring(): 
    path = os.path.join(os.path.dirname(__file__), 'readme.rst')
    if os.path.isfile(path):
        return open(path).read()
    else:
        import pipeless
        return pipeless.__doc__

setup(name='Pipeless',
      version='1.11',
      description='Simple pipelines building framework.',
      long_description=readme_or_docstring(),
      author='Andy Chase',
      author_email='theandychase@gmail.com',
      url='https://andychase.me/pipeless',
      download_url="https://github.com/andychase/pipeless/archive/master.zip",
      license="MIT",
      py_modules=['pipeless']
      )
