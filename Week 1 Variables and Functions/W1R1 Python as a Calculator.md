[

<div style="float:right; position:relative; width:30%; border: 2px solid black; margin:5px;">![Practical Programming](https://imagery.pragprog.com/products/336/gwpy2_largecover.jpg?1361381128)

*   Chapter 2.2\. Expressions and Values: Arithmetic in Python
*   Chapter 2.3\. What Is a Type?
*   Chapter 2.6\. How Python Tells You Something Went Wrong
*   <span style="position:absolute; bottom:0; right:0;">_Optional reading_</span>

</div>

](https://www.coursera.org/learn/learn-to-program/resources/oTgXi)

# Python as a Calculator

### Arithmetic Operators

<table border="1">

<tbody>

<tr>

<td>Operator</td>

<td>Operation</td>

<td>Expression</td>

<td>English description</td>

<td>Result</td>

</tr>

<tr>

<td>`+`</td>

<td>addition</td>

<td>`11 + 56`</td>

<td>11 plus 56</td>

<td>67</td>

</tr>

<tr>

<td>`-`</td>

<td>subtraction</td>

<td>`23 - 52`</td>

<td>23 minus 52</td>

<td>-29</td>

</tr>

<tr>

<td>`*`</td>

<td>multiplication</td>

<td>`4 * 5`</td>

<td>4 multiplied by 5</td>

<td>20</td>

</tr>

<tr>

<td>`**`</td>

<td>exponentiation</td>

<td>`2 ** 5`</td>

<td>2 to the power of 5</td>

<td>32</td>

</tr>

<tr>

<td>`/`</td>

<td>division</td>

<td>`9 / 2`</td>

<td>9 divided by 2</td>

<td>4.5</td>

</tr>

<tr>

<td>`//`</td>

<td>integer division</td>

<td>`9 // 2`</td>

<td>9 divided by 2</td>

<td>4</td>

</tr>

<tr>

<td>`%`</td>

<td>modulo (remainder)</td>

<td>`9 % 2`</td>

<td>9 mod 2</td>

<td>1</td>

</tr>

</tbody>

</table>

### Types `int` and `float`

A _type_ is a set of values and operations that can be performed on those values.

Two of Python's numeric types:

*   `int`: integer  
    For example: `3`, `4`, `894`, `0`, `-3`, `-18`

*   `float`: floating point number (an approximation to a real number)  
    For example: `5.6`, `7.342`, `53452.0`, `0.0`, `-89.34`, `-9.5`

### Arithmetic Operator Precedence

When multiple operators are combined in a single expression, the operations are evaluated in order of precedence.

<table border="1">

<tbody>

<tr>

<td>Operator</td>

<td>Precedence</td>

</tr>

<tr>

<td>**</td>

<td>highest</td>

</tr>

<tr>

<td>- (negation)</td>

</tr>

<tr>

<td>*, /, //, %</td>

</tr>

<tr>

<td>+ (addition), - (subtraction)</td>

<td>lowest</td>

</tr>

</tbody>

</table>

### Syntax and Semantics

_Syntax_: the rules that describe valid combinations of Python symbols

_Semantics_: the meaning of a combination of Python symbols is the meaning of an instruction — what a particular combination of symbols does when you execute it.

### Errors

A syntax error occurs when we an instruction with invalid syntax is executed. For example:

<pre>>>> 3) + 2 * 4
SyntaxError: invalid syntax
</pre>

A semantic error occurs when an instruction with invalid semantics is executed. For example:

<pre>>>> 89.4 / 0
Traceback (most recent call last):
  File "", line 1, in
    89.4 / 0
ZeroDivisionError: float division by zero
</pre>

* * *

<center>Jennifer Campbell • Paul Gries  
University of Toronto</center>

* * *