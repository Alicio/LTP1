# Type `dict`

### Optional Reading:

*   Chapter 11.3 Storing Data Using Dictionaries

### Dictionary

Another way to store collections of data is using Python's dictionary type: `dict`.

The general form of a dictionary is:

<pre>{key1: value1, key2: value2, ..., keyN: valueN}
</pre>

Keys must be unique. Values may be duplicated. For example:

<pre>asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}
</pre>

In the example above, the keys are unique: `'A1'`, `'A2'` and `'A3'`. The values are not unique: `80`, `90` and `90`.

### How To Modify Dictionaries

Dictionaries are mutable: they can be modified. There are a series of operations and methods you can apply to dictionaries which are outlined below.

| Operation | Description | Example |
| --- | --- | --- | 
| `object in dict` | Checks whether `object` is a key in `dict`. | <pre>>>> asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}<br>>>> 'A1' in asn_to_grade<br>True<br>>>> 80 in asn_to_grade<br>False</pre>|
| `len(dict)` | Returns the number of keys in `dict`. | <pre>>>> asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}<br>>>> len(asn_to_grade)<br>3</pre>|
| `del dict[key]` | Removes a key and its associated value from `dict`. | <pre>>>> asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}<br>>>> del asn_to_grade['A1']<br>>>> asn_to_grade<br>{'A3': 90, 'A2': 90}</pre>|
| `dict[key] = value` | If `key` does not exist in `dict`, adds `key` and its associated `value` to `dict`.<br>If `key` exists in `dict`, updates `dict` by setting the value associated with `key` to `value`. | <pre>>>> asn_to_grade = {'A1' : 80, 'A2': 90, 'A3' : 90}<br>>>> asn_to_grade['A4'] = 70<br>>>> asn_to_grade<br>{'A1': 80, 'A3': 90, 'A2': 90, 'A4': 70}</pre>|

### Accessing Information From Dictionaries

Dictionaries are unordered. That is, the order the key-value pairs are added to the dictionary has no effect on the order in which they are accessed. For example:

<pre>>>> asn_to_grade = {'A1': 80, 'A2': 70, 'A3': 90}
>>> for assignment in asn_to_grade:
    print(assignment)

A1
A3
A2
</pre>

The for-loop above printed out the keys of the dictionary. It is also possible to print out the values:

<pre>>>> asn_to_grade = {'A1': 80, 'A2': 70, 'A3': 90}
>>> for assignment in asn_to_grade:
    print(asn_to_grade[assignment])

80
90
70
</pre>

Finally, both the keys are values can be printed:

<pre>>>> asn_to_grade = {'A1': 80, 'A2': 70, 'A3': 90}
>>> for assignment in asn_to_grade:
    print(assignment, asn_to_grade[assignment])

A1 80
A3 90
A2 70
</pre>

### Empty Dictionaries

A dictionary can be empty. For example:

<pre>d = {}
</pre>

### Heterogeneous Dictionaries

A dictionary can have keys of different types. For example, one key can be of type `int` and another of type `str`:

<pre>d = {'apple': 1, 3: 4}
</pre>

### Immutable Keys

The keys of a dictionary must be immutable. Therefore, lists, dictionary and other mutable types cannot be used as keys. The following results in an error:

<pre>d[[1, 2]] = 'banana'
</pre>

Since lists are mutable, they cannot be keys. Instead, to use a sequence as a key, type `tuple` can be used:

<pre>d[(1, 2)] = 'banana'
</pre>

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *