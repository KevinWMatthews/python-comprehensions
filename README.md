# Python Comprehensions

Comprehensions allow sequences (list in Python2; list, set, and dict in Python3)
to be constructed from other sequences.
It is a simpler way to effect the same changes as the `map` and `filter` builtins.


## Background

Python's comprehension notation seems to stem from set builder notation in mathematics (research this):
```
{x | x>0}
# The set of all x such that x>0
```
or more generally
```
{object | conditional}
# The set of all objects such that the conditional is met
```


## Python Syntax

### List comprehension

Python's syntax for list comprehension is:
```
[x for x in range(10) if x > 0]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
or more generally
```
<new_list> = [<output_expression> for <variable> in <input_sequence> <conditional>]
```

Python will:

    * iterate over the `input_sequence`
    * place the member of the input sequence in `variable`
    * process `output_expression` if `conditional` is met
    * store resulting sequence in a `new_list`

The `conditional` is used to filter the input sequence, much like `filter()`.
The `output_expression` is used to transform the members of the `input_sequence`, much like `map()`.


### Examples

All numbers in range:

```python
[x for x in range(10)]      # an empty conditional captures all items of the input sequence
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

All numbers in range that are greater than 5:

```python
[x for x in range(10) if x > 5]
# [6, 7, 8, 9]
```

Square odd numbers:
```python
[x**2 for x in range(10) if x % 2 != 0]
# [1, 9, 25, 49, 81]
```


### Set comprehension

In Python, sets are unordered lists.
They are denoted by curly braces:

```python
{1, 2, 3}       # This is a set
```

Notation for set comprehension is similar to that for list comprehension:

```python
{x for x in range(10)}
```

### Dictionary comprehension

Again, this is similar to list comprehension:

```python
{x: x**2 for x in range(4)}
```

```python
{index: number for index, number in enumerate(range(4))}
```

Watch out for the placement of the ':'.


## Links

[Python3 Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
[Python 3 Patterns, Recipes, and Idioms](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html)
[Stack Overflow](https://stackoverflow.com/questions/34835951/what-does-list-comprehension-mean-how-does-it-work-and-how-can-i-use-it)
