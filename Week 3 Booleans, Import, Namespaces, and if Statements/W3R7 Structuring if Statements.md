# Structuring `if` Statements

### Optional Reading:

*   Chapter 5.3 Nested If Statements

### `if-elif` vs. `if-if`

An `if` statement with an `elif` clause is a single statement. The expressions are evaluated from top to bottom until one produces `True` or until there are no expressions left to evaluate. When an expression produces `True`, the body associated with it is executed and then the `if` statement exits. Any subsequent expressions are ignored. For example:

<pre>    grade1 = 70
    grade2 = 80

    if grade1 >= 50:
        print('You passed a course with grade: ', grade1)
    elif grade2 >= 50:
        print('You passed a course with grade: ', grade2)

</pre>

The `if` statement condition (`grade1 >= 50`) evaluates to `True`, so the body associated with the `if` is executed and then the `if` exits. The `elif` condition is not even evaluated in this case.

It is possible for `if` statements to appear one after another in a program. Although they are be adjacent to each other, they are completely independent of each other and it is possible for the body of each `if` to be executed. For example:

<pre>    grade1 = 70
    grade2 = 80

    if grade1 >= 50:
        print('You passed a course with grade: ', grade1)
    if grade2 >= 50:
        print('You passed a course with grade: ', grade2)

</pre>

In the program above, the condition associated with the first `if` statement (`grade1 >= 50`) produces `True`, so the body associated with it is executed. The condition associated with the second `if` statement (`grade2 >= 50`) also produces `True`, so the body associated with it is also executed.

### Nested `if`s

It is possible to place an `if` statement within the body of another `if` statement. For example:

<pre>    if precipitation:
        if temperature > 0:
            print('Bring your umbrella!')
        else:
            print('Wear your snow boots and winter coat!)   

</pre>

The statement above can be simplified by removing some of the nesting. The message `'Bring your umbrella!'` is printed only when both of the `if` statement conditions are `True`. The message `'Wear your snow boots and winter coat!'` is printed only when the outer `if` condition is `True`, but the inner `if` condition is `False`. The following is equivalent to the code above:

<pre>    if precipitation and temperature > 0:
        print('Bring your umbrella')
    elif precipitation:
        print('Wear your snow boots and winter coat!')
</pre>

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *