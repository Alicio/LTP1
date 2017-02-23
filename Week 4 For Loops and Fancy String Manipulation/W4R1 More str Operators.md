# More `str` Operators

### Optional Reading:

*   Chapter 5.1 A Boolean Type

### String Comparisons

The equality and inequlity operators can be applied to strings:

<pre>>>> 'a' == 'a'
True
>>> 'ant' == 'ace'
False
>>> 'a' == 'b'
False
>>> 'a' != 'b'
True

</pre>

We can compare two strings for their dictionary order, comparing them letter by letter:

<pre>>>> 'abracadabra' < 'ace'
True
>>> 'abracadabra' > 'ace'
False
>>> 'a' <= 'a'
True
>>> 'A' < 'B'
True
</pre>

Capitalization matters, and capital letters are less than lowercase letters:

<pre>>>> 'a' != 'A'
True
>>> 'a' < 'A'
False
</pre>

Every letter can be compared:

<pre>>>> ',' < '3'
True
</pre>

We can compare a string and an integer for equality:

<pre>>>> 's' == 3
False
</pre>

We can't compare values of two different types for ordering:

<pre>>>> 's' <= 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>>
TypeError: unorderable types: str() <= int()
</pre>

### Testing For Substrings

The operator `in` checks whether a string appears anywhere inside another one (that is, whether a string is a substring of another).

<pre>>>> 'c' in 'aeiou'
False
>>> 'cad' in 'abracadabra'
True
>>> 'zoo' in 'ooze'
False
</pre>

### String length: function `len`

The builtin function `len` returns the number of characters in a string:

<pre>>>> len('')
0
>>> len('abracadabra')
11
>>> len('Bwa' + 'ha' * 10)
23
</pre>

### Summary

| Description | Operator | Example | Result of example |
| --- | --- | --- | --- |
| equality | `==` | `'cat' == 'cat'` | `True` |
| inequality | `!=` | `'cat' != 'Cat'` | `True` |
| less than | `<` | `'A' < 'a'` | `True` |
| greater than | `>` | `'a' > 'A'` | `True` |
| less than or equal | `<=` | `'a' <= 'a'` | `True` |
| greater than or equal | `>=` | `'a' >= 'A'` | `True` |
| contains | `in` | `'cad' in 'abracadabra'` | `True` |
| length of `str` s | `len(s)` | `len("abc")` | `3` |

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *