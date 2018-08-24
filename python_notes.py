<USEFUL PYTHON NOTES>

In terminal: python --version # to check the python version most people still use 2.6/2.7

0. The head of the file: #!/usr/bin/python # this line tells OS which package to use to run program

Make a file executable: chmod +x filename.py
	
get the current work directory: 
import os 
os.getcwd( )

whitespace: spaces, tab, end-of-line are whitespace and they are used to show the end of a statement or indentation.
            At other times, whitespace is ignored.
            
Indent can be a tab or any spaces>=1, but the convention is 4 spaces.
Single and double quotes are the same in python, double quotes are useful when there is an apostrophe in the string. 
Straight quotes ' ' " " are legal in python
Curly quotes  ‘ ’ “ ” are not. 
Continuation: add a \ at the end makes the statement continue onto the next line
\n: line break
input()
Exception handling: try, except, else, finally. # to catch the abnormal actions 

1. Expressions:
	a. constants
	   type     value
   	   int      integer (no inherent size limit but the computer may crash if the number is too big)
	   str      string (enclosed in single or double quote marks, must match)
	   float    floating-point number (have limited range and precision, == can fail even for 0.1+0.2==0.3) 
	  	    special values: inf, nan (not a number, for example inf-inf is not defined).
		    inf is not a pre-defined variable but it can be got by float('inf'). 
		    float('inf') / 10 == inf, float('inf') // 10 == nan.
	   bool     truth values: False True. Do not use +, -, *, etc, on them.
	   NoneType None
	   For integer: 027 = 23 # because this number with base of 8 rather than 10
	   For decimal: 027.= 27.0 # this number is still with base of 10
	   In python 2.x, 10/3=3, 10//3=3, 10./3.=3.3333333333333335, 10/3.=3.3333333333333335, so it is better to do this in the code: from future import division, then we can use division directly: 10/3=3.3333333333333335. In python 3, the type of 3/1 is float.  
	   In python 3.x, the result of division is always a float. type(4/2) is float.
	   Floats can be written in scientific notation: 1e30 mean 1*10^{30}, but it is a float. 
		 
 	   Type conversion: 
		 input        output
		int ('32')      32  Conversion from str to number only works if the string contains only a numberic literal
		int (32)        32
		int (3.8)       3   int does not round off, it just chops off the fraction part
		float(32）      32.0
		float('3.14')   3.14 Conversion from str to number only works if the string contains only a numberic literal
		str(32)         '32'  
		str('32')       '32'
	b. variables:
		      Variable name cannot begin with a number but begin with a letter or underscore.
		      Variable name cannot use Python's keywords: 
				False class finally is return None continue for lambda try True def from nonlocal while
				and del global not with as elif if or yield assert else import pass break except in raise
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
           // # truncating/integer/floor division. For example, 5//2=2. -10/3=-3.33333 takes the floor of -3.33333 is -4.
	      # divides two numbers and rounds down (toward negative infinity) to an integer.
           %  # modulus (remainder after division). For example, 5%2=1
	      #10//3==3, 10%3==1; -10//3==-4, -10%3==2; 10//-3==-4, 10%-3==-2; -10//-3==3, -10%-3==-1
	      Rule: For any two numbers a and b, if q = a // b and r = a % b, sign(a%b)==sign(b),
		    then it should be true that (q * b) + r == a and that r is “between” 0 and b 
		    (when b is positive, that means 0 <= r < b; if b is negative, it means b < r <= 0).
		     number axis  -5 -4 -3 -2 -1  0  1  2  3  4  5  
		     python %3     1  2  0  1  2  0  1  2  0  1  2 # it is more convenient in python for array, like [-1]
	      Usage: can extract the right-most digit or digits from a number. 
		     For example, x % 10 yields the right-most digit of x (in base 10) and x % 100 yields the last two digits.
	   -  cannot work on string
	   /  cannot work on string
	   +  plus, can also work as string concatenation, which means join the strings end-to-end. only + same types
	   *  works in the form of 'string'*integer for repetition of string	      
	   += # For example: x+=2 is equivalent to x=x+2
	   -=, /=, *=, **=, %=.
		      
 	   comparison/relational operators: #lower precedence than arithmetic operators
	   <, >, <=, >= # ordering
	   == # equality, do not use this on floats
           != # not equal to
	   can compare two values of the same type, return True or False (type bool). 
		      
	   logical (Boolean) operators: #lower precedence than comparison operators
	   or, and, not are used to combine Boolean values: True, False. Any nonzero number is interpreted as True as well.
		     
	   Set undecided or no value: None
	  
	d. function calls
 	   Python built-in functions: 
		      		    min(), max() and sorted() work on any types of sequences but not work on mixed types.
		      		    sum() only works on sequences that contain only numbers.
	   All most all math functions take and return values of type float.
	   print function convert all arguments to type str before printing.
   	   In python 3, print (sth)
	   In python 2, print sth
	   def function_name(parameters):  # define function
	       """ string """ # function docstring, the first statement inside a function (module, class) definition.
		              # State the purpose and limitations of the function, parameters and return value.
		      	      # use help(functionname) to see this string, use for description and assumptions.
               some local variables or operation # at least one statement
	       #all statements must be preceded by same space.
               return expression with parameters # parameters and variables that created in a function are local.
	       # a function can contain multiple return statements (and also no return statement).
	       # Without return, the output in None, the expression return print(...) will always return None as well because
	       # print is a function. It has the side effect of printing the arguments to the console, but it returns None. 

	   When call the function: function_name(arguments) # arguments can be expressions and functions
    	   If there is no return, the function call returns None, but it is not shown in interactive mode.
           The name of the argument has nothing to do with the name of the parameter. 
           The number of parameters and arguments should match.
	   Arguments: *args
	   Keyword arguments: ** kwargs  
	   Function names can be letters, numbers and underscore but the first character cannot me a number. 
           Function names cannot be the python's keywords. Avoid to define function and variable with the same name.
           Function names are case sensitive. 
           * A good function (usually) does one thing and should be general. Functions promote abstraction, reduce code repetition.


2. Container types: 
		 tuple(), commonly used in functions.
	         list[], use slice to access sublists [start(default=0):stop(default=none):stride(default=1)].
                 set([]), no repeated elements.
	         dictionary{'dictionary key': dictionary value,'':}			

If you set list1=list2, they are the same objects.
If you set list1=list.copy(), then they are two objects.

3. Open files, write files.

with open("filename.txt") as file:
data = file.read()

Code Defensively – assert # make sure input data is not empty

List comprehension can minimize the loop, for example: a = range(1,50+1) 
                                                       b = [x for x in a if x % 2 == 0] # even numbers only

4. Sequence: contains zero or more values. Each value has an index: sequence[index].
	     [index]: Index must be an interger ranges from -n (first value) through -1 (last value) & 0 (first value) to n-1 (last value).
	     len(sequence) # returns the sequence length
	     string: contain only text, immutable. # string[len(string)-1] or string[-1] gives the last character
	     list[]: can contain a mix of value types. [,,,]
	     tuple(): like lists but immutable (can not be changed once created).
	     NumPy arrays: numpy.ndarray (n-dimensional array data type). All values must be the same type. 
		           np.array([,,,]), np.zeros(size), np.ones(size)*number, no.linspace(start,end,size)
	     Warning： For list, list[]+list[] is just the concatenation of two lists.
		       For example, [1,2]+[2,3]==[1,2,3,4], [1,2]*2=[1,2,1,2] but [1,2]+2 is not allowed(cannot concatenate).
		       For ndarray, the operation is done for each element in an array or paries of elements at equal positionn in two arrays.
		       For example, array([1,2])+np.array([3,4])==array([4, 6]), np.array([1,2])*2==array([2, 4]), np.array([1,2])+2==array([3, 4]).
	     traversal: for letter in string:
		            print (letter)
	     slicing: access a subsequence by indexing a range of positions: sequence[start:end]
		    string[n:m] # returns the part of the string from the “n-eth” character to the “m-eth” character,
		                # including the first (n-th) but excluding the last (m-th).
		      		# If n>=m. returns empty string: ''.
		    string[:m] # the slice starts at the beginning of the string.
		    string[n:] # the slice goes to the end of the string
		    string[:] # returns the whole string
		    Unique to NumPy arrays: 
		      - Indexing with an array of integers selects elements from the positions in the index array.
		     *- Indexing with an array of Booleans selects elements from the positions where the index array contains True.
		      
		      
5. Control Flow:
	      conditional statements (branching): 
		      	      if
		      	      elif # abbreviation of “else if”
		              else # If there is an else clause, it has to be at the end, but there doesn’t have to have one.
		      		   # If there is no indent, the else matchs with the closest if above.
		      	      Avoid nested conditonals to make code easier to be understood.
	      loop statement (iteration):
		              for i in range(integer number): # executes a suite once for every element of a sequence, works on any iterable types.
							      # The for loop is simpler to use, but only allows you to look at one element at a time.
                              while i < number: # Repeats a suite of statements as long as a condition is true, write condition explicitly.
		    				# If the condition is initially False, the loop executes zero times.
						# If no variable involved in the condition is changed or updated can 
		                                # make the condition false during execution, the loop will continue forever.
		      				# It is frequently used when the repetition times are unknown.
		      				# The while loop must initialise and update an index variable, and specify the loop condition correctly
		      				# but allows greater flexibility; for example, you can skip elements in the sequence
		      				# (increment the index by more than one) or look at elements in more than one position in each iteration.
	                      break # break out of the loop
                              continue # continue from the beginning of loop
			      pass # null operation, act as a placeholder

Generate non-integer steps in range: [x * 0.1 for x in range(0,10,2)] #output: [0.0, 0.2, 0.4, 0.6000000000000001, 0.8]
		 
6. Code testing and debugging: 
		edge cases: - Integers: 0, 1, -1, 2, ...
			   - float: very small (1e-308) or big (1e308)
			   - Sequences: empty (’’, []), length one.
			   - Any value that requires special treatment in the code.
		Assertion: assert test expression, "error message" # check the whether the variable is valid before run the code
		           # The assert statement causes a runtime error if test expression evaluates to False.
		      
 

7. Modules: a collection of functions and variables.
  Package: a collection of modules.
  how to use: import modules/package # or 
              from modules/package import variables, functions, classes
  Import them and then help(modules/package name) or dir(modules/package name) 
  to get further information about included variables, functions, classes and usage.
  Just use help() then find the required module, 
  type quit then Enter to leave the help system and return to the python shell.


8. Objects in Python: attributes, methods, properties. For example, .real, .imag, .conjugate(), .append(), .sort().
   User-defined objects: class.

9. Ipython : object_name? or object_name??# get help about this object
 	  
10. Matplotlib: create scatter plots (plt.scatter),
 	       display images (plt.imshow),
	       display contour plots (plt.contour and plt.contourf),
               create hexagonal tessellations (plt.hexbin),
	       draw filled regions (plt.fill and plt.fill_between),
	       create multiple subplots (plt.subplot and plt.axes) 


11. NumPy: import numpy as np 
          Array: fast math operations on arrays/matrices
                a.To create an array: np,array([,,,]), np.arange(integer_number), np.linspace(start value, end value, numbers), np.zeros(integer number), np.ones(integer number).
   		b.Multidimensional array: For example x=np.zeros((2,4)) # get 2X4 array of zeros.
                                       x[0,:] # get the first row of x
                                       x[:,0] # get the first column of x
   		c.Random array: np.random.random(loc=, scale=, size=integer_number) # uniform between 0 and 1
                	        np.random.normal(size=integer_number) # standard nornal distributed
		 		np.random.randint(low=, high=, size= ) # rando, integers
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
   scipy.stats: common statistical functions(>60) and distributions(~80 continuous distributions and >10 discrete distributions)
   scipy.special: special functions (e.g., Airy functions, Bessel functions, orthogonal polynomials, gamma functions, and much more)
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
   Guideline 2: avoid large loops (using for or while) in favor of vectorized operations. When apply the same operation to a sequence of many items, vectorized methods within NumPy will likely be a better choice.
   Guideline 3: use array slicing, masks, fancy indexing, and broadcasting to eliminate loops.
		Masks: can be combined using the bitwise operators & for AND, | for OR, ~ for NOT, and ^ for XOR. For example, x [ ( x < 0 . 1 ) | ( x > 0 . 5 ) ] = 9 9 9 will result in every item in the array x which is less than 0.1 or greater than 0.5 being replaced by 999. 

15. Scikit:
	   Scikitimage: a more beefed-up image module than scipy.ndimage(imaging processing toolkit) 
	   Scikit-learn: a machine learning package
  





