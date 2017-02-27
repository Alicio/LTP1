# Nested Lists

### Optional Reading:

*   Chapter 8.7 Working with a List of Lists

Lists can contain items of any type, including other lists. These are called _nested lists_.

Here is an example.

<pre>>>> grades = [['Assignment 1', 80], ['Assignment 2', 90], ['Assignment 3', 70]]
>>> grades[0]
['Assignment 1', 80]
>>> grades[1]
['Assignment 2', 90]
>>> grades[2]
['Assignment 3', 70]
</pre>

To access a nested item, first select the sublist, and then treat the result as a regular list.

For example, to access `'Assignment 1'`, we can first get the sublist and then use it as we would a regular list:

<pre>>>> sublist = grades[0]
>>> sublist
['Assignment 1', 80]
>>> sublist[0]
'Assignment 1'
>>> sublist[1]
80

</pre>

Both `sublist` and `grades[0]` contain the memory address of the `['Assignment 1', 80]` nested list.

We can access the items inside the nested lists like this:

<pre>>>> grades[0][0]
'Assignment 1'
>>> grades[0][1]
80
>>> grades[1][0]
'Assignment 2'
>>> grades[1][1]
90
>>> grades[2][0]
'Assignment 3'
>>> grades[2][1]
70
</pre>

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *