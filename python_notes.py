<USEFUL PYTHON NOTES>

In terminal/shell/commandline: python --version # check the python version most people still use 2.6/2.7
	* Can pass arguments (strings) to the program:  python3 my prog.py arg1 "arg two"
	 Make a file executable: chmod +x filename.py

Python visualized steps: http://pythontutor.com/visualize.html#mode=edit		
Python has two basic modes: script(write in a file) and interactive(write in command line). 
0. Syntax:
The head of the file: #!/usr/bin/python # this line tells OS which package to use to run program
-1 can multiply string but get empty string, but -1 cannot multiply None.

absolute path: it specifies the full path, from the top-level (“root”) directory.
relative path: specifies a location in the directory structure relative to the current working directory.
	
import os 
get the current work directory:	os.getcwd( )
get the absolute path: os.path.abspath('filename')
change directory to another path: os.chdir('path')
check whether a file or directory exists: os.path.exists('filename')
check whether it is a directory: os.path.isdir('path/foldername or filename')
check whether it is a file: os.path.isfile('path/foldername or filename')
return a list of the files in the given directory: os.listdir(path). os.listdir('..') will return 
           a list of the subdirectories and files in the parent of the current working directory.

Path: 
    Linux and macOS: 
	  An absolute path starts with a '/', the separator is '/', '..' means the directory above.
	  Single directory tree. File and directory names are case sensitive.
	  For example, /students/u5869920/test.py
    Windows: 
	  Absolute path starts with drive letter and ':', like C:.
	  The separator is '\', but must write '\\' in python because '\' has its meaning in python. '..' means the directory above.
	  One directory tree for each drive (A to Z). File and directory names are not case sensitive.
	  For example, C:\\Users\\u5869920\\test.py  ..\\lab1\\exercise1.py

whitespace: spaces, tab, end-of-line are whitespace and they are used to show the end of a statement or indentation.
	    At other times, whitespace is ignored.
	               
Indent can be a tab or any spaces>=1, but the convention is 4 spaces.
Single and double quotes are the same in python, use double quotes when there is an apostrophe in string. 
Straight quotes ' ' " " are legal in python. Curly quotes  ‘ ’ “ ” are not. 

Continuation: add a \ at the end makes the statement continue onto the next line
hash sign (#): marks the beginning of a comment; it continues to end-of-line.

input()
	
Errors: -Syntax errors # are shown in spyder before running the code
	-Runtime errors # code is syntactically valid, but operation is impossible for python interpreter,
		        # so they will cause an exception.
	*Exception names:-TypeError, ValueError (incorrect type or value for operation)
			 -NameError, UnboundLocalError, AttributeError
			  (variable or function name not defined)
			 -IndexError (invalid sequence index) E.g. [] input can incur Index error
			 -KeyError (key not in dictionary)
			 -ZeroDivisionError,etc.
			
	-Semantic/logic errors: code runs without error, but does the wrong thing,
				like returns the wrong answer. For example,
			        filereadline() move the file position to the end.
				compare floating point numbers with ==, <, >.
	Runtime errors are preferrable to semantic errors, because it is immediately clear when and
		where they occur.
	⇒ it is better to “fail fast” (raise an exception) than to return a non-sense result.
	
Raising Exception:
  -assert condition, "fail message" # Code Defensively, check violated assumptions.
   If can’t compute a correct value, raise an exception! But don’t assert more than what is necessary.
  - For example, don’t restrict input types if the function works for any sequence type.
    # Evaluate condition (to type bool), if the value is not True, raise an AssertionError
    # with the (optional) message.
   It is used to check programmers's assumptions: including correct use of functions, like make sure
   input data is not empty. Function’s docstring states assumptions; assertions can check them.
  -raise ExceptionName('optional argument') 
  # Raise the named exception. Exception arguments (required or optional) depend on exception type.
  # Raise an exception is the same as runtime erros that Python raise, but the raise statement can
  # take a detailed error message and typically used with programmer-defined exception types.
	
Exception handling: catch the abnormal actions, 
			but NEVER catch an exception unless there is a sensible way to handle it.
		     try:
			 suite
		     except ExceptionName:
			 error-handling suite 
		    * Execute suite.
		    * If no exception arises, skip error-handling suite and continue as normal.
		    * If the named exception arises from executing suite immediately execute
		      errorhandlingsuite, then continue as normal.
		    * If any other error occurs, fail as normal.
		     try:
			 suite
		     except ExceptionName:
			 error-handling suite
		     finally:
			 clean-up suite
	       * After suite finishes (whether it causes an exception or not), execute clean-up suite.
	       * If an except clause is triggered, the error handler is executed before clean-up suite.
               * If the exception passes to the caller, clean-up suite is still executed before leaving
		 the function.
	       * finally is usually used to ensure file is closed even if an exception occurs:
			def read file(fname):
			    file = open(fname)
			    try:
				for line in file:
				   # process line
			    finally:
				file.close() # close file

 	

Number in base b: 
	- The position of the least significant digit is 0 (b**0 = 1 for any base b).
	- Each digit is one of 0, . . . , b − 1.
	- nnnn_b means a number in base b.
	- Not every fraction has a finite decimal expansion in a given base and digital computers work 
	  with numbers of fixed width, so representation of fractions have finite precision(float numbers).
	- A floating point number x in base b: x = + or - m* b**e (sign: + or -; significand m; exponent e).
	- Floating point number systems:  
	  (base, precision of significand, lower limit, upper limit of the exponent).
	  IEEE double-precision system: (2, 52, -1023, 1024).
	  In this system, the smallest number > 0 is 2e−1023 ≈ 10e−308,
	                  the smallest number > 1 is 1+2e−52≈1+2·10e−16.
	- The numbers that can be represented (exactly) in a floating point number system are not evenly
	      distributed on the real line. 
	- Rounding to p+1 digits in base b, the  absolute error is ≤ 1/2 b^{-p}· b^e,
	                                    the relative error is ≤ 1/2 b^{-p}.
	
object: every value computed by the interpreter is an object. An object in python has an id and some attributes, like type.
	When we assign a value to variable, the variable name is associated with a reference to the object;
	that is objects id. Several variables can refer to the same objects.
id: identity, this is a number assigned by the python interpreter when an object is created. Can access using id() function.
	
Immutable objects never change id. 
	Operations on immutable objects create new objects, leaving the original unchanged: tuple.
Mutable objects: A mutable object can be modified of its attributes yet it’s identity remains the same.
	mutable types: ndarray, list, set, dictionary, user-defined class
hashable: Immutable types like integers, floats and strings are hashable;
	  mutable types like lists and dictionaries are not.
Abstract data types(ADT): the set of operations that can be done on values of the type.
		Example: “sequence type” (length, index, slice)
			 “iterable type” (for loop)
local namespace: is the namespace that is created when a function is called, and stops existing when the function ends.
		 use locals() to examine the contents of the current local namespace, return as a dictionary.
global namespace: is created when the program (or the python interpreter) starts executing, and persists until it finishes.
		 use globals() to examine the contents of the current global namespace, return as a dictionary.

1. Expressions:
	a. constants
	   type     value (every value is an object, every object has a unique identifier 
		    (its location in memory): id())
   	   int      integer (no inherent size limit but the computer may crash if number is too big)
	   str      string (enclosed in single or double quote marks, must match)
	   float    floating-point number: (Almost) never compare floats with ==.
		    - have limited range:  Min/max value: ±1.79*10^308
		    - have limited precision: == can fail even for 0.1+0.2==0.3.
	  	    special values: inf, nan (not a number, for example inf-inf is not defined).
		    inf is not a pre-defined variable but it can be got by float('inf'). 
		    float('inf') / 10 == inf, float('inf') // 10 == nan.
		    For exact decimal representation, use the decimal module.
		    For exact arithmetic, use the fractions module.
	   bool     truth values: False True. Do not use +, -, *, etc, on them.
	   NoneType None
	   For integer: 027 = 23 # because this number with base of 8 rather than 10
	   For decimal: 027.= 27.0 # this number is still with base of 10
	   In python 2.x, 10/3=3, 10//3=3, 10./3.=3.3333333333333335, 10/3.=3.3333333333333335, 
	                  so it is better to do this in the code: from future import division, 
			  then we can use division directly: 10/3=3.3333333333333335.   
	   In python 3.x, the result of division is always a float. type(4/2)==float, type(4//2)==int
	   Floats can be written in scientific notation: 1e30 mean 1*10^{30}, but it is a float. 
		 
 	   Type conversion: 
		 input        output
		int ('32')      32  Conversion from str to number only works if the string contains 
				    only a numberic literal
		int (32)        32
		int (3.8)       3   int does not round off, it just chops off the fraction part
		float(32）      32.0
		float('3.14')   3.14 Conversion from str to number only works if the string contains
		      		     only a numberic literal
		str(32)         '32'  
		str('32')       '32'
		      
	b. variables:
		Variable name cannot begin with a number but begin with a letter or underscore.
		Variable name cannot use Python's keywords: False class finally is return None continue
		      for lambda try True def from nonlocal while and del global not with as elif if or
		      yield assert else import pass break except in raise
		Variable name is case sensitive.	
		A variable assignment is written as variable_name=expression # this is a statement
		Naming conventions: i, j, k are often used for loop indices.
		      			  n, m, k are often used for counts.
		      			  x, y and z are often used for coordinates.
		      				
	c. Operators: 
	   log is ln
          log10 is lg      
	   numeric operators:
	   ** # exponentiation has higher precedence than multiplication
           // # truncating/integer/floor division.
	      # divides two numbers and rounds down (toward negative infinity) to an integer.
		For example, 5//2=2. -10/3=-3.33333 takes the floor of -3.33333 is -4.
           %  # modulus (remainder after division). For example, 5%2=1
	      #10//3==3, 10%3==1; -10//3==-4, -10%3==2; 10//-3==-4, 10%-3==-2; -10//-3==3, -10%-3==-1
	      Rule: For any two numbers a and b, if q = a // b and r = a % b, sign(a%b)==sign(b),
		    then it should be true that (q * b) + r == a and that r is “between” 0 and b 
		    (when b is positive, that means 0 <= r < b; if b is negative, it means b < r <= 0).
		     number axis  -5 -4 -3 -2 -1  0  1  2  3  4  5  
		     python %3     1  2  0  1  2  0  1  2  0  1  2
		                   # it is more convenient in python for array, like [-1]
	      Usage: can extract the right-most digit or digits from a number. 
		For example, x % 10 yields the right-most digit of x (in base 10) and 
		             x % 100 yields the last two digits.
	   -  cannot work on string
	   /  cannot work on string
	   +  plus, can also work as string concatenation, which means join the strings end-to-end.
		    only + same types
	   *  works in the form of 'string'*integer for repetition of string	      
	   += # For example: x+=2 is equivalent to x=x+2
	   -=, /=, *=, **=, %=.
		      
 	   comparison/relational operators: #lower precedence than arithmetic operators
		                # work with tuples and other sequences; starts by comparing
				# the first element from each sequence. If they are equal, 
		                # it goes on to the next elements, and so on, until it finds
		      		# elements that differ. Subsequent elements are not considered 
		      		# (even if they are really big).
	   <, >, <=, >= # ordering
	   == # equality, do not use this on floats
          != # not equal to
	   can compare two values of the same type, return True or False (type bool). 
		      
	   logical (Boolean) operators: #lower precedence than comparison operators
	   or, and, not are used to combine Boolean values: True, False. 
		      Any nonzero number is interpreted as True as well.
		     
	   Set undecided or no value: None
	   is operator tests whether two references are to the same object;
		 that is, x is y is True if and only if id( x ) == id( y ).
	d. function calls
 	   Python built-in functions: https://docs.python.org/3/library/stdtypes.html#string-methods
		      		    min(), max() and sorted() work on any types of sequences but not work on mixed types.
		      		    sorted(seq,key=fun) returns a increasing list, value x are sorted by fun(x). 
		      		    sum() and abs() only works on sequences that contain only numbers.
		      		    range(n) returns an iterable value whose elements are the integers 0, 1, etc, up to n-1.
	   Almost all math functions take and return values of type float.
	   print function convert all arguments to type str before printing.
   	         In python 3, print (sth)
	         In python 2, print sth
 	   Recursive function: a function that calls itself. It must have a branching statement can stop the loop.
	   def function_name(parameters):  # define function
	       """ string """ # function docstring, the first statement inside a function (module, class) definition.
		              # State the purpose and limitations of the function, parameters and return value.
		      	      # use help(function_name) to see this string, use for description and assumptions.
               some local variables or operation # at least one statement
	       When a non-local variable is evaluated, its value is taken from the (enclosing) global namespace.
		      Can use global variable_name to declare this is a global variable.
	       When a local variable (maybe defined after evaluation) is evaluated, only the local namespace is checked.
		      If a variable is assigned anywhere in the function(it doesn't matter if that assignment has been
		      executed, or will be executed, or not), then that variable is considered to be "local", 
		      and the python interpreter will only look for it in the local namespace of the function call.
	       #all statements must be preceded by same space.
               return expression with parameters # parameters and variables that created in a function are local.
	       # a function can contain multiple return statements (and also no return statement).
	       # Without return, the output is None, the expression return print(...) will always return None as well because
	       # print is a function. It has the side effect of printing the arguments to the console, but it returns None. 
	   When call the function: function_name(arguments) # arguments can be expressions and functions
		                   The local namespace disappars when the function call ends.
	   When a function is called, its parameters are assigned references to the argument values. 
	   # So if an argument value refers to a mutable object, modifications to this object made in the function are 
	   # visible outsidethe function’s scope.
    	   If there is no return, the function call returns None, but it is not shown in interactive mode.
           The name of the argument has nothing to do with the name of the parameter. 
           The number of parameters and arguments should match.
	   Arguments: *args
	   Keyword arguments: ** kwargs  
	   Function names can be letters, numbers and underscore but the first character cannot me a number. 
           Function names cannot be the python's keywords. Avoid to define function and variable with the same name.
           Function names are case sensitive. 
           A good function (usually) does one thing and should be general. 
		                     promotes abstraction, reduces code repetition.
		      		     access only local variables within.
		      		     Don’t modify mutable argument values, unless intend to do so.
	   


2. Container types: 
   tuple(): commonly used in functions, immutable.
		      
   list[]: use slice to access sublists [start(default=0):stop(default=none):stride(default=1)], mutable.
    list comprehension: a mechanism for writing compact expressions that create lists, can minimize the loop.
 			[element_expression for variable_name in iterable_expression if condition ]
		      	For example, [x**2 for x in range(50) if x % 2 == 0] # list of even numbers' square.
		      
   set([]): set is a mutable type but elements within must be immutable. {,,,} gives a set.
		Elements can be a mixture of different types. Lists cannot be elements of a set, but tuples can be.
	    set is an unordered collection of (immutable) values without duplicates(no repeated elements).
	    set is iterable, but it is not a sequence (so it is not indexable).
	    set operators: len(), |union, &intersection, -difference, ^symmetric difference, element in aset.
		           set operators return a new result set, and do not modify the operands.
	    set methods: aset.issubset(bset) subset (A ⊆ B), aset.union(bset), aset.intersection(bset),
		         aset.add(element), aset.remove(element).
	    
		      
   dictionary{'dictionary key': dictionary value,'':} or dict(): mutable type, a collection but NOT a sequence.
	{:,:,:} or {} gives a dictionary. dict[key]=value to assign or update the key value. 
	key: -can be different types, must be immutable. Use key as index.
	     -A key can be a string, tuple or integer(immutable), but not dictionary(mutable). 
	     -Each key has exactly one value.
	     -Can use key in dictionary to check the existence of key. 
	value: -can be any types, including mutable objects. 
	       -Values can be of any type, even a dictionary (mutable).
	       -The same value can be associated with several different keys.
	       -Cannot use value in dictionary to check the existence of value. 
		Can set values=dict.values, then use value in values to check the existence of value.
	methods:
	   dict.keys(), dict.values(), and adict.items() return views of the keys, values and key–value pairs
	        as a sequence of tuples, where each tuple is a key-value pair. Can write as key,value=item.
	   The order of items in a dictionary is unpredictable. Can use sorted to sort keys.
	   len(dictionary) gives the number of key-value pairs.
	   Remove keys: del adict[key], adict.pop(key). adict.popitem() removes an arbitrary pair.
	   dict.get(key, default value): If the key appears in the dictionary, get returns the corresponding value;
		      		         otherwise it returns the default value.



3. Open files, read data, write files: 
    Open file: file_obj=open("file_path", "access_mode") access mode: r(ead), w(rite), a(ppend), b(inary).
    Read file: file_obj.read(size of characters), file_obj.readline(), file_obj.readlines().
    Close the file when done (always!): file_obj.close().
    Write file: file_obj.write(string) writes the string to the file. 
		If we want to put other values in a file, we have to convert them to strings: 
		   '%d' to format an integer
		   '%g' to format a floating-point number
                   '%s' to format a string
                print(..., file=file_obj) prints to the specified file instead of the terminal.
                Check whether the file exists before writing to avoid erasing or overwriting:
		      os.path.exists(file_path) returns True or False.
    The file object keeps track of where in the file to read (or write) next. The next read operation (or iteration)
        starts from the current position. So if you call write again, it adds the new data to the end of the file.
    python data[i][j]:    i=j=0 1 2 3 4 =j 
		  	  i = 1
		      	  i = 2
		      	  i = 3
		          i = 4
    	      	      
    a. with open("filename.txt") as file: # with statement will automatically close the file.
            data = file.read()
    b. import csv
       Open file:
       	         with open('filename.csv") as file:
	   	      reader=csv.reader(file)
 	              data=[row for row in reader]
                 After reading the file, all entries in all rows will be strings!
       Write file:
		  with open('filename.csv','a or w') as csvfile:
       		       csvwriter=csv.writer(csvfile)
       		       csvwriter.writerow([time,altitude,velocity])		 
       If the file contains a header, the first row in table will contain this header. Can use slicing to get a table without header.
       Use list comprehension to extract single column, for example, [ row[3] for row in table ].
	   Select rows/columns with certain criterion, for example not having any blank fields: [ row for row in table if row[3] != '' ].
	   Create a list of the indicies of rows in table that have a non-empty value in column 3:
						 [ i for i in range(len(table)) if table[i][3] != '' ].
	   Convert data type, for example:[ [ row[0], row[1], float(row[2]), int(row[3]) ] for row in table ],
	    but try to convert and empty string into a number (int or float) will cause a runtime error. 
	   One way to solve this is to filter out rows with empty entries first and then convert those that remain.
	   Or use a self-defined function: [ my_fun(row[3]) for row in table ].

4. Sequence: contains zero or more values. Each value has an integer index: sequence[index]. Iterable data type.
         [index] # Index must be an interger ranges from -n (first value) through -1 (last value) & 0 (first value) 
		 to n-1 (last value).
	 len(sequence) # returns the sequence length
   a. string: contain only text--a sequence of characters, immutable. write as 'string', "string", '''string'''
	      (The triple quote has the special ability that it can stretch over several lines).
	      # string[len(string)-1] or string[-1] gives the last character.
		1. Quoting characters other than those enclosing a string can be used inside it: "it’s true!".
		2. Quoting characters of the same kind can be used inside a string if escaped by                       
		backslash (\): 'it\'s true'.
		Escapes are used also for some non-printing characters: for example, \n is line break. 
   string methods: similar to a function but use dot notation. string.method(). To use help: help(str.method).
		   returns a  new string and leave the original alone.
        .capitalize() Return a copy of the string with its first character capitalized and the rest lowercased.
        .title() Return a copy of the string with its first character and first character after ' ' capitalized 
		 and the rest lowercased.
        .find('substring or character', start index, stop index): word.find('a') returns the index of first 'a' in word.
        .upper(): takes a string and returns a new string with all uppercase letters of old string.
        .split('delimiter') Return a list of the words  an argument value refers to a mutable objectin the string,
		 they are separated by delimiter.
 	 delimiter.join(list of strings): The inverse of split. It takes a list of strings and concatenates the elements.
         str1 in str2:  a boolean operator that takes two strings and returns True if the first appears as
		        a substring in the second.
        .count(substring,start,end): Return the number of occurrences of substring in the range [start, end]. 
        .is_lower(): Return true if all cased charaprint(index, element)cters in the string are lowercase.
   b. list[]: can contain elements of any type-including a mix of elements of different types in the same list. [,,,]mutable.
	     Since lists are mutable, it is often useful to make a copy before performing operations that modify lists.
	     list("abcd")==[’a’, ’b’, ’c’, ’d’]
	Indexing a list returns an element, but slicing a list returns a list.
	     For example, A = [ [1, 2, 3], [4, 5, 6]]. 
	                  A[0]==[1,2,3] so A[0][1]==2.
	                  A[0:1]==[[1,2,3]] but A[0:1][1] gives IndexError: list index out of range, 
		 because len(A[0:1])==1.
	List methods: 
	     .append(element), .insert(index,element), .pop(index), .extend(elements), .sort(), .reverse(), remove().
	     Most list methods are void; they modify the list and return None, so don't write alist=alist.method().
	A list contains references to its elements. 
		 Two lists can be equivalent, which means elements are the same, 
		 but they can be not identical when they 
		     they are not the same object.
	Aliasing: An object with more than one reference has more than one name, so we say that the object is aliased.
		 If the aliased object is mutable, changes made with one alias affect the other.  
		 In general, it is safer to avoid aliasing when working with mutable objects.
		 If set b=a or b=a[:], when changing the reference, the printout result of a and b can be different,
		    but intrinsically they are pointing to the same objects unless reassignment.
	         If you set list2=list1, they are the same objects.If you set list2=list1.copy(),then they are two objects.
	         Slicing a list creates a new list(list2=list1[:]), but containing references to 
		    the same objects (“shallow copy”).
	 List points to its assignment even after the operation: 
		 for example, a=[[]]*3, then a==[[],[],[]], but a[0].append(1)==[[1], [1], [1]] 
		 because a points to [].
   c. tuple(): a sequence of values. The values can be any type, and they are indexed by integers, 
		like lists but immutable (can not be reassigned once created but can be replaced).
		 t = ('a', 'b', 'c', 'd', 'e') then t = ('A',) + t[1:] gives t==('A', 'b', 'c', 'd', 'e').
	       Syntactically, a tuple is a comma-separated list of values, but it is common to enclose tuples in parentheses.
		 It is the comma that creates the tuple, not the parentheses! t=,,,, can define a tuple.
	       Create a tuple with a single element, have to include a final comma: t1='a', then type(t1)==tuple
		 t2=('a') then type(t2)==str. type((1))==int, type(1,)==int, type((1,))==tuple. Create a empty tuple: x=().  	       
	       If the argument of a tuple is a sequence (string, list or tuple), the result is a tuple with the elements of
		the sequence: t = tuple('lupins') then t==('l', 'u', 'p', 'i', 'n', 's').
	       Tuple assignment: to swap values of two variables: a,b=b,a.
		 		 to split and assign: addr = 'monty@python.org' then uname, domain = addr.split('@') gives
		 		  uname=='monty' and domain=='python.org'.
	       Variable-length argument tuples: a parameter name that begins with *(gather/scatter), usually use *args.
	       zip: a built-in function that takes two or more sequences and returns a list of tuples where each tuple
		      contains one element from each sequence. For example, zip(seq_a,seq_b).
		    If the sequences are not the same length, the result has the length of the shorter one. 
		    Can’t use an index to select an element from a zip object, but can use for x,y in zip(t1,t2). 
		    Enumerate: for index, element in enumerate('abc'): print(index, element).
	       In a return statement, it is syntactically simpler to create a tuple than a list.
	       If you are passing a sequence as an argument to a function, using tuples reduces the
		    potential for unexpected behavior due to aliasing.
   d. NumPy arrays: numpy.ndarray (n-dimensional array data type). All values must be the same type. 
		    len(array) is the size of first dimension. array.shape is a sequence of the size in each dimension.
		    array[i,j]==array[i][j], array[i,:]==array[i] is row i, array[:,j] is column j.
		    np.array([,,,]), np.zeros(size), np.ones(size)*number, np.linspace(start,end,size)
	     
   Warning：For list, list[]+list[] is just the concatenation of two lists.
	    For example, [1,2]+[2,3]==[1,2,3,4], [1,2]*2=[1,2,1,2] but [1,2]+2 is not allowed(cannot concatenate).
            For ndarray, the operation is done for each element in an array or paries of elements 
		at equal positionn in two arrays.
	    For example, array([1,2])+np.array([3,4])==array([4, 6]), np.array([1,2])*2==array([2, 4]), 
		np.array([1,2])+2==array([3,4]).
   traversal: for letter in string:
		  print (letter)
   slicing: access a subsequence by indexing a range of positions: sequence[start:end]
            The type of slice is still the type of original type of sequence, even only has one element. 
		 Slicing a list returns a list.
		      For example, if type(x) == str then type(x[i:i+1]) == str, if type(x) == list
		 then type(x[i:i+1]) == list.
      seq[ start : end : stepsize ]
	  if stepsize is > 0, take every stepsize:th element, start from left, up to, but not including the element
	     at right index, if start is at the right of end, returns empty string ''.
	  if stepsize is < 0, take every stepsize:th element, start from right, down to, but not including the element 
	     at left index, if end is at the right of the start, returns empty string ''.
	       string[n:m:p] # returns the part of the string from the “n-th” character (including the n-th) 
		             # to the “m-th” character (excluding the m-th) in step of p if p>0.
		      	     # Slice indices can go past the start/end of the sequence without raising an error.
	       string[:m] # the slice starts at the beginning of the string.
	       string[n:] # the slice goes to the end of the string
	       string[:] # returns the whole string
	    Python interprets anegative step number as stepping backward.
       	       string[::-1] generates a reversed string.
	       string[::-2] # backwards, every other letter
	       s[-1:len(s)]='last character of s' because it starts from -1 then go to len(s)-1 
		 but does not include len(s).
	       s[0:len(s):-1]==s[-1:(len(s)+1):-1]==''.  
	       s[len(s):0:-1] # backwards but do not inculde s[0]==s[-len(s)]
	       s[::-1]==s[to the end of string and include:from the left of the beginning of string 
			  but not include:backwards]
   Unique to NumPy arrays: 
	 - Indexing with an array of integers selects elements from the positions in the index array.
	   If I is an array of integers, A[I] returns an array with the elemnts of A at indices I (does not preserve shape).
	*- Indexing with an array of Booleans selects elements from the positions where the index array contains True.
	   If L is an array of bool of the same size as A, A[L] returns an array with the elemnts of A where L is True
	      (does not preserve shape).
		 
Sequence comparisons: based on character encoding. 
		 Character encoding: Every character has an integer number, unicode define numbers for >120000 characters.
		 Functions ord and chr map between the character and integer representation: ord(’A’)==65, chr(65)=='A'.
		 All the uppercase letters < all the lowercase letters.
		      
5. Control Flow:
   a. conditional statements (branching): 
	 if
	 elif # abbreviation of “else if”
	 else # If there is an else clause, it has to be at the end, but there doesn’t have to have one.
	      # If there is no indent, the else matchs with the closest if above.
	 Avoid nested conditonals to make code easier to be understood.
   b. loop statement (iteration): 
      iterable types: A file is a sequence of bytes, but python's file object is not a sequence type. 
			   File objects in python are iterable, but not sequences.
      for i in range(integer number): 
		 executes a suite once for every element of a sequence, works on any iterable types.
			# The for loop is simpler to use, but only allows you to look at one element at a time.
      while i < number: # Repeats a suite of statements as long as a condition is true, write condition explicitly.
		- If the condition is initially False, the loop executes zero times.
		- If no variable involved in the condition is changed or updated can make the condition false
		  during execution, the loop will continue forever.
		- It is frequently used when the repetition times are unknown.
		- The while loop must initialise and update an index variable, and specify the loop condition correctly
		  but allows greater flexibility; for example, you can skip elements in the sequence
		  (increment the index by more than one) or look at elements in more than one position in each iteration.
      break # break out of the loop
      continue # continue from the beginning of loop
      pass # null operation, act as a placeholder

      Generate non-integer steps in range: [x * 0.1 for x in range(0,10,2)] 
		 #output: [0.0, 0.2, 0.4, 0.6000000000000001, 0.8]
		 
6. Code testing and debugging: 
		edge cases:- Integers: 0, 1, -1, 2, ...
			   - float: very small (1e-308) or big (1e308)
			   - Sequences: empty ('', []), length one.
			   - Any value that requires special treatment in the code.
		Assertion: assert test expression, "error message" 
		 # check the whether the variable is valid before run the code
		           # The assert statement causes a runtime error if test expression evaluates to False.
		      
 

7. Global variables: Variables in __main__ are sometimes called global because they can be accessed from any function.
		  It is common to use global variables for flags (boolean variables that indicate whether a condition is true).
  Modules: a collection of functions and variables (a sequence of statements). Every python file is a module.
           * When the python shell runs in “script mode”, the file it’s executing becomes the “main module”.
		- Its name becomes ’ main ’.
		- Its namespace is the global namespace.
	   * The first time a module is imported, that module is loaded (executed); it may later be re-loaded.
	   * Every loaded module creates a separate (permanent) namespace and stores the module object(namespace)
		 in the system dictionary of loaded modules and then associates modname with the module object
		 in the current namespace.  
	   * Note: the Spyder IDE reloads all user-defined modules on (first) import when running a file.
	   * The global variable __name__ in every module namespace stores the module name.
  	   * import sys sys.modules is a dictionary of all loaded modules.
	   * dir(module) returns a list of names defined in module’s namespace
	   * dir() lists the current (global) namespace.
  Package: a collection of modules.
  how to use: import modules/package # or 
              from modules/package import variables, functions, classes
  Import them and then help(modules/package name) or dir(modules/package name) 
         to get further information about included variables, functions, classes and usage.
  Just use help() then find the required module, 
  type quit then Enter to leave the help system and return to the python shell.

  an argument value refers to a mutable object
8. Objects in Python: attributes, methods, properties. For example, .real, .imag, .conjugate(), .append(), .sort().
   User-defined objects: class.

9. Ipython : object_name? or object_name??# get help about this object
 	  
10. Matplotlib:plot median lines on the plot: 
		 plot.plot([median(x),median(x)],[min(y),max(y)],linestyle='solid', color='red')
		      			      
		 plot.plot([min(x),max(x)],[median(y),median(y)],linestyle='solid', color='blue')
	       create scatter plots (plt.scatter),
 	       display images (plt.imshow),
	       display contour plots (plt.contour and plt.contourf),
               create hexagonal tessellations (plt.hexbin),
	       draw filled regions (plt.fill and plt.fill_between),
	       create multiple subplots (plt.subplot and plt.axes) 


11. NumPy: import numpy as np 
          Array: fast math operations on arrays/matrices, NumPy arrays is element-wise.
                a.To create an array: np.array([,,,]), np.arange(integer_number),
		 np.linspace(start value, end value, numbers), 
		                      np.zeros(integer number), np.ones(integer number).
   		b.Multidimensional array: For example x=np.zeros((2,4)) # get 2X4 array of zeros.
                                       x[0,:] # get the first row of x
                                       x[:,0] # get the first column of x
   		c.Random array: np.random.random(loc=, scale=, size=integer_number) # uniform between 0 and 1
                	        np.random.normal(size=integer_number) # standard nornal distributed
		 		np.random.randint(low=, high=, size= ) # random integers
   		d. .dtype # check the data type
	  	e. plotting: matplotlib
	  Read data: y=np.loadtxt('x.txt')
          Write data: np.savetxt('x.txt', x)

12. Scipy: 
   Generate random variables: from scipy.stats import distributions
			      distributions.poisson.rvs(10, size=4)
   Analytic Integration: import numpy as np
			 from scipy.integrate import quad
			 result, error=integrate.quad(function to be integrated, lower limit, upper limit)  
   Numerical Integration: from scipy.integrate import trapz
			  result=trapz(y,x=x)
			  
   Optimization: scipy.optimize
   Interpolation: scipy.interpolate
   scipy.spatial: distance and spatial functions, nearest neighbor, Delaunay tessellation
   scipy.cluster: cluster analysis class: vector quantization (vq) and hierarchical clustering (hierarchy)
   scipy.sparse: sparse matrix storage, sparse linear algebra, sparse solvers, sparse graph traversal
   scipy.stats: common statistical functions(>60) and distributions(~80 continuous distributions and >10 
								    discrete distributions)
   scipy.special: special functions (e.g., Airy functions, Bessel functions, orthogonal polynomials, gamma functions,
				     and much more)
   scipy.constants: numerical and dimensional constants
   


13. NumPy and SciPy modules:
   Linear Algebra: numpy.linalg and scipy.linalg 
                   a. matrix inverses (linalg.inv)
 		   b. singular value decompositions (linalg.svd)
		   c. eigenvalue decompositions (linalg.eig)
 		   d. least-squares solutions (linalg.lstsq)

   FFT: NumPy (numpy.fft submodule) and SciPy (scipy.fftpack submodule)


14. Efficient coding: Python loops are slow, and NumPy array tricks can be used to sidestep this problem.
   Guideline 1: store data in NumPy arrays, not Python lists unless building the dynamical array using np.append().
   Guideline 2: avoid large loops (using for or while) in favor of vectorized operations. When apply the same 
		 operation to a sequence
		of many items, vectorized methods within NumPy will likely be a better choice.
   Guideline 3: use array slicing, masks, fancy indexing, and broadcasting to eliminate loops.
		Masks: can be combined using the bitwise operators & for AND, | for OR, ~ for NOT, and ^ for XOR. 
		       For example, x [ ( x < 0 . 1 ) | ( x > 0 . 5 ) ] = 9 9 9 will result in every item in the array 
		 x which is less 
		      		    than 0.1 or greater than 0.5 being replaced by 999. 

15. Scikit:
	   Scikitimage: a more beefed-up image module than scipy.ndimage(imaging processing toolkit) 
	   Scikit-learn: a machine learning package
		 
16. Pandas: Library for (tabular) data analysis.
	    - Special types for 1-d (pandas.Series) and 2-d (pandas.DataFrame) data.
	    - General indexing, selection, alignment, grouping, aggregation.
  





