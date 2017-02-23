# `str` Methods: Functions Inside Objects

### Optional Reading:

*   Chapter 7.1 Modules, Classes, and Methods
*   Chapter 7.2 Calling Methods the Object-Oriented Way
*   Chapter 7.3 Exploring String Methods

### Methods

A _method_ is a function inside of an object.

The general form of a method call is:

`object.method(arguments)`

### String Methods

Consider the code:

<pre>>>> white_rabbit = "I'm late! I'm late! For a very important date!"
</pre>

To find out which methods are inside strings, use the function `dir`:

<pre>>>> dir(white_rabbit)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__','__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', 'capitalize', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier',
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
 'zfill']
</pre>

Passing `str` as an argument to `dir` gets the same result:

<pre>>>> dir(str)
</pre>

For many of the string methods, a new string is returned. Since strings are immutable, the original string is unchanged. For example, a lowercase version of the `str` that `white_rabbit` refers to is returned when the method `lower` is called:

<pre>>>> white_rabbit.lower()
>>> "i'm late! i'm late! for a very important date!"
>>> white_rabbit
>>> "I'm late! I'm late! For a very important date!"

</pre>

To get information about a method, such as the `lower` method, do the following:

<pre>>>> help(str.lower)
</pre>

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *