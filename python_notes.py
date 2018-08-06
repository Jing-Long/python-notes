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
	
1. Expressions:
	a. constants
	
	   type     value
   	   int      integer (no inherent size limit but the computer may crash if the number is too big)
	   str      string (enclosed in single or double quote marks, must match)
	   float    floating-point number (have limited range and precision, == can fail) special values: +inf, -inf, nan.
	   bool     truth values
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
				
	c. Operators: 
	   log is ln
           log10 is lg      
	   numeric operators:
	   ** # exponent
           // # truncating division. For example, 5//2=2.
           %  # modulo (remainder after division). For example, 5%2=1
	   -  cannot work on string
	   /  cannot work on string
	   +  is string concatenation, which means join the strings end-to-end
	   *  works in the form of 'string'*integer for repetition of string	      
	   += # For example: x+=2 is equivalent to x=x+2
	   -=, /=, *=, **=, %=.
 	   comparison operators:
	   <, >, <=, >= # ordering
	   == # equality     
           != # not equal to
	   can compare two values of the same type, return True or False (type bool).      
	   logical operators: 
	   or, and, not. Boolean values: bool, True, False.
	   Set undecided or no value: None
	  
	d. function calls
	   All most all math functions take and return values of type float.
	   print function convert all arguments to type str before printing.
   	   In python 3, print (sth)
	   In python 2, print sth
	   def function_name(parameters):  # define function
	       """ string """ # function docstring, use help(functionname) to see this string, use as description
               some local variables or operation
               return expression with parameters # parameters and variables that created in a function are local.
	   When call the function: function_name(arguments) # arguments can be expressions and functions
    	   If there is no return, the function call returns None, but it is not shown in interactive mode.
           The name of the argument has nothing to do with the name of the parameter. 
           The number of parameters and arguments should match.
	   Arguments: *args
	   Keyword arguments: ** kwargs  
	   Function names can be letters, numbers and underscore but the first character cannot me a number. 
           Function names cannot be the python's keywords. Avoid to define function and variable with the same name.
           Function names are case sensitive. 
           



2. Container types: tuple(), can not be changed once created, commonly used in functions.
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








5. Control Flow: conditional statements: if, elif, else.
	      loop statement: for i in range(integer number):
                              while i < number:
	                      break # break out of the loop
                              continue # continue from the beginning of loop
			      pass # null operation, act as a placeholder

Generate non-integer steps in range: [x * 0.1 for x in range(0,10,2)] #output: [0.0, 0.2, 0.4, 0.6000000000000001, 0.8]

6. Exception handling: try, except, else, finally. # to catch the abnormal actions 

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
          Array:
                a.To create an array: np,array([,,,]), np.arange(integer_number), np.linspace(start value, end value, numbers), np.zeros(integer number), np.ones(integer number).
   		b.Multidimensional array: For example x=np.zeros((2,4)) # get 2X4 array of zeros.
                                       x[0,:] # get the first row of x
                                       x[:,0] # get the first column of x
   		c.Random array: np.random.random(loc=, scale=, size=integer_number) # uniform between 0 and 1
                	        np.random.normal(size=integer_number) # standard nornal distributed
		 		np.random.randint(low=, high=, size= ) # rando, integers
   		d. .dtype # check the data type
	  
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
  





