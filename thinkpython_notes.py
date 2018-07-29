Ch1.
class    type
int      integer
str       string
float    floating-point number

In python 3, print (sth)
In python 2, print sth

Ch2.
Variable name cannot begin with a number.
Variable name cannot use Python's keywords: 
False class finally is return
None continue for lambda try
True def from nonlocal while
and del global not with
as elif if or yield
assert else import pass
break except in raise

-  cannot work on string
/  cannot work on string
+  is string concatenation, which means join the strings end-to-end
*  works in the form of 'string'*integer for repetition of string

Ch3. Functions
input       output
int ('32')     32
int (32)       32
int (3.8)      3     int does not round off, it just chops off the fraction part
float(32）  32.0
float('3.14')   3.14
str(32)        '32'
str('32')      '32'

log is ln
log10 is lg

Function names can be letters, numbers and underscore but the first character cannot me a number. 
Function names cannot be the python's keywords. Avoid to define function and variable with the same name.
Function names are case sensitive.

Single and double quotes are the same in python, double quotes are useful when there is an apostrophe in the string. 
Straight quotes ' ' " " are legal in python
Curly quotes  ‘ ’ “ ” are not. 

When define the function: def function_name(parameter):
When call the function: function_name(argument)
The name of the argument has nothing to do with the name of the parameter. 

Parameters and variables that created in a function are local.
