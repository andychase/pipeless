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
      version='2.0.0',
      description='Simple data pipeline building library',
      long_description=readme_or_docstring(),
      author='Andy Chase',
      author_email='theandychase@gmail.com',
      url='https://andychase.me/pipeless',
      download_url="https://github.com/andychase/pipeless/archive/master.zip",
      license="MIT",
      py_modules=['pipeless'],
      classifiers=(
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing'
      ),
      )
