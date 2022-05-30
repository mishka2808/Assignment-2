"""
Created on Tue May 24 10:26:30 2022
@author: Mish
Assignment 2
Question 1 Numerical differentiation
a & b
"""

import numpy as np
import matplotlib.pyplot as plt

x_a = np.linspace(-2, 3, 100)
x_b = np.linspace(-5, 5, 100)

H_a = x_a[10]-x_a[9]
H_b = x_b[10]-x_b[9]

"""----------------------------------------------------------------------------"""
def funcA(x): #wrote each equation as a function
    y_a = (1/4)*x**4 - x**2 - x
    return y_a

def funcB(x): 
    y_b = np.tanh(x)
    return y_b
"""----------------------------------------------------------------------------"""
def first_der_forward(f,h,x):   # Numerical estimation of First Derivative (Forward)
   # y_n' = (y_{n+1}  - y_n})/h                                         ...eqn (2.3)
    
    y_first_der_forward = (f(x+h) - f(x))/h
    return y_first_der_forward

"""----------------------------------------------------------------------------"""
def first_der_back(f,h,x):      # Numerical estimation of First Derivative Backward
   # y_n' = (y_{n}  - y_n-1})/h                                         ...eqn (2.4)
    
    y_first_der_back = (f(x) - f(x-h))/h
    return y_first_der_back

"""----------------------------------------------------------------------------"""
def first_der_cent(f,h,x):      # Numerical estimation of First Derivative Centered
    # y_n' = (y_{n}  - y_n-1})/2h                                       ...eqn (2.5)

    y_first_der_cent = (f(x+h) - f(x-h))/(2*h)
    return y_first_der_cent

"""----------------------------------------------------------------------------"""


plt.figure()
plt.plot(x_a, x_a**3 - 2*x_a -1 , '-k', label = "Theoretical")
plt.plot(x_a, first_der_forward(funcA,H_a,x_a), '.r', label = "Numerical (Forward)")
plt.plot(x_a, first_der_back(funcA,H_a,x_a), '.b', label = "Numerical (Back)")
plt.plot(x_a, first_der_cent(funcA,H_a,x_a), '.y', label = "Numerical (Center")
plt.title("First derivative: a)")
plt.legend()


"""----------------------------------------------------------------------------"""


plt.figure()
plt.plot(x_b, 1/(np.cosh(x_b))**2 , '-k', label = "Theoretical")
plt.plot(x_b, first_der_forward(funcB,H_b,x_b), '.r', label = "Numerical (Forward)")
plt.plot(x_b, first_der_back(funcB,H_b,x_b), '.b', label = "Numerical (Back)")
plt.plot(x_b, first_der_cent(funcB,H_b,x_b), '.y', label = "Numerical (Center")
plt.title("First derivative: b)")
plt.legend()

"""----------------------------------------------------------------------------"""
"""ERRORS"""
plt.figure()
plt.plot(x_a, (x_a**3 +2*x_a -1) - (first_der_forward(funcA,H_a,x_a)), '.r', label = "Error of a (Forward)" )
plt.plot(x_a, (x_a**3 +2*x_a -1) - (first_der_back(funcA,H_a,x_a)) ,   '.b', label = "Error of a (Back)")
plt.plot(x_a, (x_a**3 +2*x_a -1) - (first_der_cent(funcA,H_a,x_a)) ,   '.y', label = "Error of a (Center)")
plt.title("Error of a")
plt.legend()


plt.figure()
plt.plot(x_a, (1/(np.cosh(x_b))**2) - (first_der_forward(funcB,H_b,x_b)), '.r', label = "Error of b (Forward)" )
plt.plot(x_a, (1/(np.cosh(x_b))**2) - (first_der_back(funcB,H_b,x_b)),  '.b', label = "Error of b (Back)") 
plt.plot(x_a, (1/(np.cosh(x_b))**2) - (first_der_cent(funcB,H_b,x_b)),  '.y', label = "Error of b (Center)") 
plt.title("Error of b")
plt.legend()
"""----------------------------------------------------------------------------"""
"""Comments on the Inaccuracy:
    a) In the case of equation a, the backwards method seems to give us a positive error, meaning that the numerical calculation is slightly
       over the true value. 
       The forward method gives us a negative error at the same proportion of the backwards method, and is slightly below the true value.
       Both of these errors seem to be proportional to a hyperbolic graph, and the error increases proportional to +- x**2
       In the case of the center method, it does not give us any error, hence this is the most accurate method to use.
    b) In the case of the equation b, the center method is the most accurate method to use as it gives us the least error.
       Both the forward and backwards method gives us error as we approach 0.5. The error of one method is the negative of the other method.
       
       According to both graphs obtained for the error, the error of the forward method is the error of the backwards method
       but has been flipped over the x-axis. 
       The center method is the most accurate, combining the results of both the forward and backwards methods in order to create a superposition
       of error, which decreases the total error into being extremely insignificant or completely gone. """
       
"""Completed on Wed May 25  19:58:08 2022 """
"""Final Edits on Mon May 30  17:38:20 2022 """
