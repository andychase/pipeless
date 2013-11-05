Pipeless
=========

*[=|Pipeless|=] provides a simple framework for building a data pipeline.*

|Build Status|

It's an advanced version of this:
``function4(function3(function2(function1(0))))``

It looks like this:

.. code-block:: python

    >>> error_handler = lambda item, exception: None
    >>> function, run, _ = pipeline(error_handler)
    >>> @function
    ... def add_one():
    ...     return lambda _: _+1
    >>> list(run([0, 1, 3]))
    [1, 2, 4]
    >>> @function
    ... def twofer(): 
    ...     def func(item): return [item, item]
    ...     return func
    >>> list(run([0, 1, 3]))
    [1, 1, 2, 2, 4, 4]

*  Pipelines operate over a source iterator (like a generator or a list).
*  Functions can return 1 Item, None to drop the item, or
   a generator. If a generator is given, the items all continue along the pipeline,
   creating like a fork.
*  All exception are caught and andled by the ``error_handler`` input argument
   to prevent one broken item from stoping the flow.

.. code-block:: python

     add_one  twofer
    [0]--|------\-----1
    Input        -----1
                    Output [1,1]

Also provides a simple optionally-argumented NamedTuple and a commmand line interface generator.

Installation
------------

Supports Python 2.7 and Python 3.x. Python 2.6 will need the ordereddict package.

.. code-block:: python

    pip install pipeless

or copy ``pipeless.py`` into your project.

Support
-------

Need some help? Send me an email at andy@asperous.us and I'll do my best to help you.

Contribution
------------

Send me suggestions, issues, and pull requests on Github and I'll gladly review them!

Licence
-------

The MIT License (MIT)

Copyright (c) 2013 Andrew Chase

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. |Build Status| image:: https://travis-ci.org/asperous/pipeless.png?branch=master
   :target: https://travis-ci.org/asperous/pipeless