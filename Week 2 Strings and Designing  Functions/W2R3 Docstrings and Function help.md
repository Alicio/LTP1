# Docstrings and Function `help`

### Optional Reading:

*   3.3 Defining Our Own Functions

Built-in function `help` displays the docstring from a function definition. For example, consider this function:

<pre>def area(base, height):
    """(number, number) -> number

    Return the area of a triangle with dimensions base
    and height.
    """

    return base * height / 2
</pre>

Calling `help` on function `area` produces this output:

<pre>>>> help(area)
Help on function area in module __main__:

area(base, height)
    (number, number) -> number

    Return the area of a triangle with dimensions base
    and height.
</pre>

* * *

<center>Jennifer Campbell • Paul Gries</center>
<center>University of Toronto</center>

* * *