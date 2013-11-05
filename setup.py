#!/usr/bin/env python
from distutils.core import setup

setup(name='Pipeless',
      version='1.0',
      description='Simple pipelines building framework.',
      long_description= \
      """ [=|Pipeless|=] provides a simple framework
      for building a data pipeline.
      
      It's an advanced version of this:
      function4(function3(function2(function1(0))))
      
      It looks like this:
      
          >>> function, run, _ = pipeline(lambda item, e: None)
          >>> @function
          ... def up_one(): return lambda item: item+1
          >>> list(run([0, 1, 3]))
          [1, 2, 4]
          >>> @function
          ... def twofer(): return lambda item: [item, item]
          >>> list(run([0, 1, 3]))
          [1, 1, 2, 2, 4, 4]

      *  Pipelines operate over sources
      *  Functions can return 1 Item, None to drop the item, or
         a generator to expand the item.
      
      Also provides a simple Optionally-Argumented NamedTuple and a Commmand Line Generator.
      """,
      author='Andy Chase',
      author_email='andy@asperous.us',
      url='http://github.com/asperous/pipeless',
      download_url="https://github.com/asperous/pipeless/archive/master.zip",
      license="MIT",
      py_modules=['pipeless']
     )