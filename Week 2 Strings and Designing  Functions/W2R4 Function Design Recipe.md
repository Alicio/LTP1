# Function Design Recipe

### Optional Reading:

*   Chaper 3.6 Designing New Functions: A Recipe

### The Six Steps

1.  **Examples**
    *   What should your function do?
    *   Type a couple of example calls.
    *   Pick a name (often a verb or verb phrase): What is a short answer to "What does your function do"?
2.  **Type Contract**
    *   What are the parameter types?
    *   What type of value is returned?
3.  **Header**
    *   Pick meaningful parameter names.
4.  **Description**
    *   Mention every parameter in your description.
    *   Describe the return value.
5.  **Body**
    *   Write the body of your function.
6.  **Test**
    *   Run the examples.

### Applying the Design Recipe

**The problem:**

The United States measures temperature in Fahrenheit and Canada measures it in Celsius. When travelling between the two countries it helps to have a conversion function. Write a function that converts from Fahrenheit to Celsius.

1.  **Examples**

    <pre>    >>> convert_to_ccelsius(32)
        0
        >>> convert_to_celsius(212)
        100

    </pre>

2.  **Type Contract**

    <pre>    (number) -> number

    </pre>

3.  **Header**

    <pre>    def convert_to_celsius(fahrenheit):

    </pre>

4.  **Description**

    <pre>    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    </pre>

5.  **Body**

    <pre>        return (fahrenheit - 32) * 5 / 9

    </pre>

6.  **Test**

    <pre>     Run the examples.   

    </pre>

#### Putting it all together:

<pre>def convert_to_celsius(fahrenheit):
   ''' (number) -> number

   Return the number of Celsius degrees equivalent to fahrenheit degrees.

   >>> convert_to_ccelsius(32)
   0
   >>> convert_to_celsius(212)
   100
   '''

   return (fahrenheit - 32) * 5 / 9
</pre>

* * *

<center>Jennifer Campbell • Paul Gries</center>
<center>University of Toronto</center>

* * *