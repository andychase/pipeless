Pipeless
=========

*A simple framework for building a data pipeline.*

|Build Status|

It's an advanced version of this:
``function4(function3(function2(function1(0))))``

It looks like this:

.. code-block:: python

    from pipeless import pipeline

    error_handler = lambda item, exception: None
    function, run, _ = pipeline(error_handler)


    @function
    def add_one(_):
        return _ + 1


    @function
    def doubler(_):
        return [_, _]


    list(run([1, 2, 3]))
    # => [2, 4,  3, 6,  4, 8]

*  Pipelines operate over a source iterator (like a generator or a list).
*  Functions can return 1 Item, None to drop the item, or
   a generator. If a generator is given, the items all continue along the pipeline,
   creating a fork.

.. code-block:: python

     add_one  doubler
    [1]--|-2----\-----2
    Input        -----4
                    Output [2,4]

*  All exception are caught and handled by the optional ``error_handler`` input argument
   to prevent one broken item from stopping the flow. If the handler returns something,
   that something continues on down the pipeline.
*  Functions can be grouped with an optional argument on the annotator i.e. ``@function('my_group')``.
   Set up your functions this way and you can skip groups with the ``function_groups_to_skip`` argument
   on the pipeline runner.

Also provides a simple optionally-argumented NamedTuple and a command line interface generator.

See the doc strings in ``pipeline.py`` for a lot more information!

Versions:

- *1.1* Function builders optional.
- *1.0.1* Fixed ordering problem.

Installation
~~~~~~~~~~~~

Supports Python 2.6, 2.7, 3.x, pypy.

.. code-block:: bash

    pip install pipeless

or copy ``pipeless.py`` into your project.

Support
~~~~~~~

Need some help? Send me an email at andy@asperous.us and I'll do my best to help you.

Contribution
~~~~~~~~~~~~

Send me suggestions, issues, and pull requests on Github and I'll gladly review them!

Licence
~~~~~~~

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
