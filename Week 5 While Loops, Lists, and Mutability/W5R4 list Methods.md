# `list` Methods

### Optional Reading:

Chapter 8.6 List methods

### Methods

A method is a function inside an object. You can find out the methods in type `list` by typing `dir(list)`.

### Modifying Lists

The table below contains methods that modify lists.

| Method | Description | Example |
| --- | --- | --- |
| `list.append(object)` | Append `object` to the end of list. | >>> colours = ['yellow', 'blue']<br/>>>> colours.append('red')<br/>>>> print(colours)<br/>['yellow', 'blue', 'red']|
| `list.extend(list)` | Append the items in the list parameter to the list. | >>> colours.extend(['pink', 'green'])<br/>>>> print(colours)<br/>['yellow', 'blue', 'red', 'pink', 'green']|
| `list.pop([index])` | Remove the item at the end of the list; optional index to remove from anywhere. | >>> colours.pop()<br/>'green'<br/>>>> print(colours)<br/>['yellow', 'blue', 'red', 'pink']<br/>>>> colours.pop(2)<br/>'red'<br/>>>> print(colours)<br/>['yellow', 'blue', 'pink']|
| `list.remove(object)` | Remove the first occurrence of the object; error if not there. | >>> colours.remove('green')<br/>ValueError: list.remove(x): x not in list<br/>>>> colours.remove('pink')<br/>>>> print(colours)<br/>['yellow', 'blue']|
| `list.reverse()` | Reverse the list. | >>> grades = [95, 65, 75, 85]<br/>>>> grades.reverse()<br/>>>> print(grades)<br/>[85, 75, 65, 95]|
| `list.sort()` | Sort the list from smallest to largest. | >>> grades.sort()<br/>>>> print(grades)<br/>[65, 75, 85, 95]|
| `list.insert(int, object)` | Insert object at the given index, moving items to make room. | >>> grades.insert(2, 80)<br/>>>> print(grades)<br/>[65, 75, 80, 85, 95]|

### Getting Information from Lists

The table below contains methods that return information about lists.

| Method | Description | Example |
| --- | --- | --- |
| `list.count(object)` | Return the number of times object occurs in list. | >>> letters = ['a', 'a', 'b', 'c']<br/>>>> letters.count('a')<br/>2|
| `list.index(object)` | Return the index of the first occurrence of object; error if not there. | >>>> letters.index('a')<br/>0<br/>>>> letters.index('d')<br/>ValueError: 'd' is not in list|

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *