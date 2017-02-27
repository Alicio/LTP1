# Reading Files

### Optional Reading:

*   Chapter 10.1 What Kinds of Files Are There?
*   Chapter 10.2 Opening a File
*   Chapter 10.3 Techniques for Reading Files

Information stored in files can be accessed by a Python program. To get access to the contents of a file, you need to _open_ the file in your program. When you are done using a file, you should _close_ it.

### Opening and Closing A File

Python has a built-in function `open` that can open a file for reading.

The form of `open` is `open(filename, mode)`, where mode is `'r'` (to open for reading), `'w'` (to open for writing), or `'a'` (to open for appending to what is already in the file).

This opens a file called `In Flanders Fields.txt` for reading:

<pre>flanders_file = open('In Flanders Fields.txt', 'r')
</pre>

Note that if the file is saved in the same directory as your program, you can simply write the name of the file, as what was done in the above example. However, if it is not saved in the same directory, you must provide the path to it.

To close a file, you write `flanders_file.close()` .

There are four standard ways to read from a file. Some use these methods:

`readline()`: read and return the next line from the file, including the newline character (if it exists). Return the empty string if there are no more lines in the file.

`readlines()`: read and return all lines in a file in a list. The lines include the newline character.

`read()`: read the whole file as a single string.

| Approach | Code | When to use it |
| --- | --- | --- |
| The `readline` approach | <pre>file = open(filename, 'r')<br>#Read lines until we reach the<br>#place in the file that we want.<br>line = file.readline()<br>while _we are not at the place we want_:<br>    line = file.readline()<br># Now we have reached the section<br># of the file we want to process.<br>line = file.readline()<br>while _we are not at the end of the section_:<br>    _process the line_<br>    line = file.readline()<br>flanders_file.close()</pre>| When you want to process only part of a file.|
| The for _line_ in _file_ approach | <pre>file = open(filename, 'r')<br>for line in file:<br>    _process the line_<br>file.close()</pre>| When you want to process every line in the file one at a time. |
| The `read` approach | <pre>file = open(filename, 'r')<br>contents = file.read()<br>_now process_ contents<br>file.close()</pre>| When you want to read the whole file at once and use it as a single string. |
| The `readlines` approach | <pre>file = open(filename, 'r')<br># Get the contents as a list of strings.<br>contents_list = file.readlines()<br>*process* contents_list *using indexing to*<br>*access particular lines from the file*<br>file.close()</pre>| When you want to examine each line of a file by index. |

### Examples from the video

Here are the code examples that appeared in the video. All of them read the entire file into a string and print that string.

#### The `readline` approach

<pre>flanders_file = open(flanders_filename, 'r')
flanders_poem = ''

line = flanders_file.readline()
while line != "":
    flanders_poem = flanders_poem + line
    line = flanders_file.readline()

print(flanders_poem)
flanders_file.close()

</pre>

#### The `for _line_ in _file_` approach

<pre>flanders_file = open(flanders_filename, 'r')
flanders_poem = ''

for line in flanders_file:
    flanders_poem = flanders_poem + line

print(flanders_poem)
flanders_file.close()

</pre>

#### The `read` approach

<pre>flanders_file = open(flanders_filename, 'r')
flanders_poem = flanders_file.read()

print(flanders_poem)
flanders_file.close()

</pre>

#### The readlines approach

<pre>flanders_file = open(flanders_filename, 'r')
flanders_poem = ''

flanders_list = flanders_file.readlines()
for line in flanders_list:
    flanders_poem = flanders_poem + line

print(flanders_poem)
flanders_file.close()

</pre>

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *