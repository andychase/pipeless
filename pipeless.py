""" [=|Pipeless|=]
Simple pipelines building framework in Python, by Andy Chase.

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
"""
from types import GeneratorType


def pipeline(error_func=None, use_builders=False):
    """ Pipeline
    Takes:

    - (Optional, Default: None) A function to run on errors that
      takes an errored_item and an exception as inputs.

      If a result other than None is returned, result
      continues in the pipeline. If None, pipeline
      exceptions are raised (useful for debugging).
      Example: error_function(errored_item, exception)

    - (Optional, Default: False) A True/False on whether you want the pipeline
      to be built using function builders or just the pipeline functions directly.

    Outputs:

    - function_annotator
      ^- Annotate your pipeline functions with this in order in which they should run.
      The pipeline functions should generate and return (a function that takes 1 item,
      and returns None, 1 item, or yields many items).
      `` def fn(): return lambda item: item + 1 ``

    - master_runner(item_generator)
      ^- Takes a generator or list of items and creates a generator out of them.
      Optional arguments ```functions_to_run``` and ```function_groups_to_skip```

    - functions_list
      ^- A list of tuples containing your functions as (group, name, function_builder).
      You can ignore this one if you like.

    >>> function, run, _ = pipeline(lambda item, e: None)
    >>> @function
    ... def forwards_and_backwards(_):
    ...     yield _
    ...     yield _[::-1]
    >>> @function
    ... def title(_): return _.title()
    >>> list(run([-1, 'tool', 'flow', 'bat']))
    ['Tool', 'Loot', 'Flow', 'Wolf', 'Bat', 'Tab']
    """
    functions_list = []

    def add_func(func, group):
        """ Functions_list is a list of tuples to maintain order.
            Originally it was an OrderedDict, but that became out of order
            when you did group1 group2 group1.
        """
        functions_list.append((group, func.__name__, func))
        return func

    def function_annotator(group=''):
        if callable(group):
            return add_func(group, '')
        else:
            return lambda func: add_func(func, group)

    def get_functions_to_run(functions=functions_list, function_groups_to_skip=None):
        if function_groups_to_skip is None:
            function_groups_to_skip = []
        functions_to_run = [fn for group, _, fn in functions if group not in function_groups_to_skip]

        if use_builders:
            def build(fn):
                fn = fn()
                assert callable(fn), \
                    "Pipeless annotated functions should build a function when use_builders=True"
                return fn

            functions_to_run = [build(fn) for fn in functions_to_run]

        return functions_to_run

    def run_pipeline(item_generator=None, functions_to_run=None, function_groups_to_skip=None):
        def safe_source(source, error_func):
            item = None
            try:
                for item in source:
                    yield item
            except Exception as e:
                if error_func is None:
                    raise
                error_func(item, e)
                raise StopIteration

        if functions_to_run is None:
            functions_to_run = get_functions_to_run(function_groups_to_skip=function_groups_to_skip)

        for item in safe_source(item_generator, error_func):
            should_yield = True
            for fn_num, function in enumerate(functions_to_run):
                try:
                    item = function(item)
                except Exception as exception:
                    if error_func is None:
                        raise
                    item = error_func(item, exception)

                if item is None:
                    should_yield = False
                    break
                if isinstance(item, GeneratorType):
                    should_yield = False
                    for i in run_pipeline(item, functions_to_run[fn_num + 1:], function_groups_to_skip):
                        yield i
                    break
            if should_yield:
                yield item

    return function_annotator, run_pipeline, functions_list
