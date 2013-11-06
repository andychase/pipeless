#!/usr/bin/env python
import os
from distutils.core import setup

read = lambda file_name: open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(name='Pipeless',
      version='1.1',
      description='Simple pipelines building framework.',
      long_description=read('readme.rst'),
      author='Andy Chase',
      author_email='andy@asperous.us',
      url='http://asperous.github.io/pipeless',
      download_url="https://github.com/asperous/pipeless/archive/master.zip",
      license="MIT",
      py_modules=['pipeless']
      )
