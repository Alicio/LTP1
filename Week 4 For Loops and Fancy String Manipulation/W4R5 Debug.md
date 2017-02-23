# IDLE's Debugger

### Debug Control

The Python Visualizer has limitations: it does not allow import statements, and it stops tracing after 300 steps. IDLE comes with a debugger, which is a tool that works a lot like the visualizer but without the pretty pictures. To run a program in IDLE's debugger, the steps are:

1.  Make sure the Python Shell window is on top and select Debug->Debugger. This opens a window called "Debug Control".
2.  Check the checkbox for Source.
3.  Open the Python file where you have saved your program.
4.  Select Run->Run Module. This will change the contents of Debug Control.

### Understanding The Debug Window

`Step` is like `Forward` in the visualizer: it executes the current instruction. We click `Step` to "step" through the program. The Debug Control window will highlight the current line being executed. It will also show the current variables in the "Locals" pane. The middle pane shows the current stack frames and the current lines of code for each. We can switch back and forth between them to see the variables.

* * *

<center>Jennifer Campbell • Paul Gries
University of Toronto</center>

* * *