""" Pipeless / examples.py. MIT licensed.

Basic functionality
>>> from pipeless import pipeline
>>> function, run, _ = pipeline(lambda item, e: None)
>>> @function
... def up_one(): return lambda item: item+1
>>> list(run([0, 1, 3]))
[1, 2, 4]
>>> @function
... def twofer(): return lambda item: [item, item]
>>> list(run([0, 1, 3]))
[1, 1, 2, 2, 4, 4]

Pipelines are composable
>>> list(run(run([0])))
[2, 2, 2, 2]

Returning None Drops result
>>> @function
... def none(): return lambda i: None
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
... def nothing_special(): return lambda i: i
>>> list(run([1,2,3]))
[1, 2, 3]
>>> @function('baller_group')
... def triple_double():
...     return lambda i: 3*i**2
>>> list(run([1,2,3]))
[3, 12, 27]
>>> @function('my_group')
... def zeroed(): return lambda i: 0
>>> list(run([1,2,3]))
[0, 0, 0]
>>> list(run([1,2,3], function_groups_to_skip=['my_group']))
[3, 12, 27]
>>> list(run([1,2,3], function_groups_to_skip=['my_group', 'baller_group']))
[1, 2, 3]

Optional NamedTuples
>>> from pipeless import namedtuple_optional
>>> new_class = namedtuple_optional({'field': 'value'}, 'cool_class')
>>> my_instance = new_class()
>>> type(my_instance)
<class 'pipeless.cool_class'>
>>> my_instance.field
'value'

CLi Generator
>>> import sys
>>> from pipeless import commandline
>>> command, cli = commandline()
>>> @command
... def print_when_1(_=0):
...     if int(_) == 1:
...         print('input was 1')
>>> sys.argv = ['.']; cli()
Command options: print_when_1
>>> sys.argv = ['.', 'print_when_1']; cli()
>>> sys.argv = ['.', 'print_when_1', '1']; cli()
input was 1
"""