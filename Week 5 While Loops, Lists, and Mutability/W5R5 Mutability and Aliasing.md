# Mutability and Aliasing

### Optional Reading:

*   Chapter 8.5 Aliasing: What’s in a Name?

### Mutability

We say that lists are _mutable_: they can be modified. All the other types we have seen so far (`str`, `int`, `float` and `bool`) are _immutable_: they cannot be modified.

Here are several examples of lists being modified:

<pre>>>> classes = ['chem', 'bio', 'cs', 'eng']
>>>
>>> # Elements can be added:
>>> classes.append('math')
>>> classes
['chem', 'bio', 'cs', 'eng', 'math']
>>>
>>> # Elements can be replaced:
>>> classes[1] = 'soc'
>>> classes
['chem', 'soc', 'cs', 'eng', 'math']
>>>
>>> # Elements can be removed:
>>> classes.pop()
'math'
>>> classes
['chem', 'soc', 'cs', 'eng']
</pre>

### Aliasing

Consider the following code:

<pre>>>> lst1 = [11, 12, 13, 14, 15, 16, 17]
>>> lst2 = lst1
>>> lst1[-1] = 18
>>> lst2
[11, 12, 13, 14, 15, 16, 18]
</pre>

After the second statement executes, `lst1` and `lst2` both refer to the same list. When two variables refer to the same objects, they are _aliases_. If that list is modified, both of `lst1` and `lst2` will see the change.

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *