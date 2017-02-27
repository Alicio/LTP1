# Write Files

### Optional Reading:

*   Chapter 10.5 Writing Files

### Writing To A File Within A Python Program

In order to write to a file, we use `_file_.write(str)`. This method writes a string to a file. Method `write` works like Python's `print` function, except that it does not add a newline character.

### File dialogs

Module `tkinter` has a submodule called `filedialog`. We import it like this:

<pre>import tkinter.filedialog
</pre>

Function `askopenfilename` asks the user to select a file to open:

<pre>tkinter.filedialog.askopenfilename()
</pre>

This function returns the full path to the file, so we can use that when we call function `open` to open that file.

<pre>from_filename = tkinter.filedialog.askopenfilename()
</pre>

Function `asksaveasfilename` asks the user to select a file to save to, and provides a warning if the file already exists.

<pre>to_filename = tkinter.filedialog.asksaveasfilename()
</pre>

### Example

Below is a program that copies a file, but puts `"Copy"` as the first line of the copied file.

In order to prompt a user for a file.

Now we can open the file we want to read from and get the contents:

<pre>from_file = open(from_filename, 'r')
contents = from_file.read()
from_file.close()
</pre>

And we can open the file we want to write to and write the contents:

<pre>to_file = open(to_filename, 'w')
to_file.write('Copy\n')  # We have to add the newline ourselves.
to_file.write(contents)  # Now write the contents of the file.
to_file.close()
</pre>

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *