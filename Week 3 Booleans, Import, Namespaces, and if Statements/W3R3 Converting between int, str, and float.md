# Converting between `int`, `str`, and `float`

### Optional Reading:

*   Chapter 4.1 Creating Strings of Characters

### str

Builtin function `str` takes any value and returns a string representation of that value.

<pre>>>> str(3)
'3'
>>> str(47.6)           
'47.6'
</pre>

### int

Builtin function `int` takes a string containing only digits (possibly with a leading minus sign `-`) and returns the `int` that represents. Function `int` also converts `float` values to integers by throwing away the fractional part.

<pre>>>> int('12345')
12345
>>> int('-998')
-998
>>> int(-99.9)
-99
</pre>

If function `int` is called with a string that contains anything other than digits, a `ValueError` happens.

<pre>>>> int('-99.9')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '-99.9'
</pre>

### float

Builtin function `float` takes a string containing only digits and zero or one decimal points (possibly with a leading minus sign `-`) and returns the `float` that represents. Function `float` also converts `int` values to `float`s.

<pre>>>> float('-43.2')
-43.2
>>> float('432')
432.0
>>> float(4)
4.0
</pre>

If function `float` is called with a string that can't be converted, a `ValueError` happens.

<pre>>>> float('-9.9.9')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '-9.9.9'
</pre>

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *