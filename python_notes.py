<USEFUL PYTHON NOTES>

In terminal: python --version # to check the python version most people still use 2.6/2.7

0. The head of the file: #!/usr/bin/python # this line tells OS which package to use to run program

Documentation strings: """ string """, use help(functionname) to see this string.

Make a file executable: chmod +x filename.py

For integer: 027 = 23 # because this number with base of 8 rather than 10
For decimal: 027.= 27.0 # this number is still with base of 10



1. Operators: ** # exponent
           != # not equal to
           // # truncating division. For example, 5//2=2.
           %  # modulo (remainder after division). For example, 5%2=1
	   += # For example: x+=2 is equivalent to x=x+2
	   -=, /=, *=, **=, %=, ==, <, >, <=, >=.
In python 2.x, 10/3=3, 10//3=3, 10./3.=3.3333333333333335, 10/3.=3.3333333333333335, so it is better to do this in the code: from future import division, then we can use division directly: 10/3=3.3333333333333335. In python 3, the type of 3/1 is float.  


Logical operators: or, and, not. Boolean values: bool, True, False.

Set undecided or no value: None

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

4. Functions: def function_name(parameters):  # define function
               some local variables or operation
               return expression with parameters

             function_name(values) # to use the defined function

Arguments: *args
Keyword arguments: ** kwargs


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
  





