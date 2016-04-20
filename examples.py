""" Pipeless / examples.py. MIT licensed.

Basic functionality
>>> from pipeless import pipeline
>>> function, run, _ = pipeline(lambda item, e: None)
>>> @function
... def up_one(_): return _+1
>>> list(run([0, 1, 3]))
[1, 2, 4]
>>> @function
... def twofer(_):
...     yield _
...     yield _
>>> list(run([0, 1, 3]))
[1, 1, 2, 2, 4, 4]

Pipelines are composable
>>> list(run(run([0])))
[2, 2, 2, 2]

Returning None Drops result
>>> @function
... def none(_): return None
>>> list(run([0]))
[]

Exception handler can replace result
>>> function, run, _ = pipeline(lambda item, e: 100)
>>> @function
... def raises_exception():
...     def func(_):
...         raise Exception
...     return func
>>> list(run([0]))
[100]

Grouping up functions
>>> function, run, _ = pipeline(lambda item, e: None)
>>> @function('my_group')
... def nothing_special(_): return _
>>> list(run([1,2,3]))
[1, 2, 3]
>>> @function('baller_group')
... def triple_double(_):
...     return 3*(_**2)
>>> list(run([1,2,3]))
[3, 12, 27]
>>> @function('my_group')
... def zeroed(_): return 0
>>> list(run([1,2,3]))
[0, 0, 0]
>>> list(run([1,2,3], function_groups_to_skip=['my_group']))
[3, 12, 27]
>>> list(run([1,2,3], function_groups_to_skip=['my_group', 'baller_group']))
[1, 2, 3]


Function Builders
>>> function, run, _ = pipeline(lambda item, e: None, use_builders=True)
>>> @function
... def bob_the_builder(): return lambda _: _+1
>>> list(run([1,2,3]))
[2, 3, 4]

"""
