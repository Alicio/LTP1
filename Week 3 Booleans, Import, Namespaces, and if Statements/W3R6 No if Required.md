# No `if` Required

### Optional Reading:

*   5.4 Remembering the Results of a Boolean Expression Evaluation (not a perfect match, but it didn't fit better elsewhere)

It is common for new programmers to write code like the following:

<pre>def is_even(num):
    """ (int) -> bool
    Return whether num is even.
    """

    if num % 2 == 0:
        return True
    else:
        return False
</pre>

This works, but is stylistically questionable. It's also more typing and reading than is necessary!

`num % 2 == 0` already produces `True` or `False`, so that expression can be used with the `return` statement:

<pre>def is_even(num):
    """ (int) -> bool
    Return whether num is even.
    """

    return num % 2 == 0
</pre>

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *