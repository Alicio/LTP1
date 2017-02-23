# Visualizing Function Calls

### Optional Reading:

*   Chaper 3.5 Tracing Function Calls in the Memory Model

We can explore how Python manages function calls using the Python Visualizer. (See the Resources page.)

In the example below, function `convert_to_seconds` contains a call on `convert_to_minutes`.

<pre>def convert_to_minutes(num_hours):
    """(int) -> int
    Return the number of minutes there are in num_hours hours.
    >>> convert_to_minutes(2)
    120
    """
    result = num_hours * 60
    return result

def convert_to_seconds(num_hours):
    """(int) -> int
    Return the number of seconds there are in num_hours hours.
    >>> convert_to_seconds(2)
    7200
    """
    return convert_to_minutes(num_hours) * 60

seconds_2 = convert_to_seconds(4)
</pre>

Here is what the memory model looks like just before the return statement inside function `convert_to_minutes` looks like:

![call stack before line 8 is executed](https://d396qusza40orc.cloudfront.net/programming1%2Fimages%2Fcallstack1.png)

Note that there are three stack frames on the call stack: the main one, then underneath that a frame for the call on function `convert_to_seconds`, and underneath that the frame for the call on function `convert_to_minutes`.

Here is [a link to the Python Visualizer](http://tinyurl.com/l7hqbwm) at this stage of the execution so that you can explore this yourself. **We strongly encourage you to step backward and forward through this program until you understand every step of execution.**

When the return statement is executed, the call on `convert_to_minutes` exits. The bottom stack frame is removed, and execution resumes using the stack frame for `convert_to_seconds`:

![call stack before line 16 is executed](https://d396qusza40orc.cloudfront.net/programming1%2Fimages%2Fcallstack2.png)

* * *

<center>Jennifer Campbell • Paul Gries</center>
<center>University of Toronto</center>

* * *