"""
Created on Tue May 24 15:25:07 2022
@author: Mish
Assignment 2
Question 2 Numerical integration
a & b
"""
import math as math
import numpy as np

a_div = 100             #number of divisions of the interval
b_div = 10000
x_a = np.linspace(1, 4, a_div)          #x_a[0]= 1 ; x_a[99]= 4
x_b = np.linspace(-1000, 1000, b_div)   

H_a = x_a[10]-x_a[9]    #H is constant throughout the interval
H_b = x_b[10]-x_b[9]

"""----------------------------------------------------------------------------"""
def funcA(x):           #wrote each equation as a function
    y_a = math.sqrt(1 + x**2)
    return y_a

def funcB(x): 
    y_b = np.exp(-x**2)
    return y_b
"""----------------------------------------------------------------------------"""


def trap(div, x_c, fnc, h):
    n = 0
    trap = 0
    while n<(div-1):                    #created n to run to call the specific numbers in the x_a and x_b arrays, otherwise there will be an error
        diff_x = x_c[n+1] - x_c[n]      #found the difference of the x coords and y coords, then multiplying, then /2 to find the triangular section of the trapezium
        diff_y = fnc(x_c[n+1]) - fnc(x_c[n])
        tri = (diff_x * diff_y)/2       #this is only going to give the top of the trapezium
        sqr = h*fnc(x_c[n])             #this will give the rectangle under the triangle of the trapezium
        trap = trap + (tri + sqr)       #area of the trapezium is the sum of the previous trapezium plus the triangle and square area of the new trapezuim
        n = n + 1                       #shifts the array to use the next set of x and y coords, so we can find the area of the new trapezium
    return trap



"""----------------------------------------------------------------------------"""

def simp(div, x_c, fnc, h):
    n = 0       #parameter/number of divisions in that cycle
    even = 0    #collects the terms where n is even
    odds = 0    #collects the terms where n is odd
    extra = 0   #collects terms ie. n = 0 and n = 99
    while n<(div):  
        x = x_c[0] + n*h    #finds x_n, ie. x_n = x_0 + n*h
        y = fnc(x)          #finds f(x_n)
        if n == 0 or n == div-1: 
                extra = extra + y
        else: 
            if n%2 == 0:    #figures out which n's are even and odd
                even = even + y 
            if not n%2 == 0: #odd terms
                odds = odds + y
                
        n = n+1     #shifts to the next value in array
    thesum = (h/3)*(extra + 4*odds + 2*even) 
    return thesum 


print("Using the Trapezoidal method, we found the area under a) to be:  ", trap(a_div, x_a, funcA, H_a))
print("Using the Simpsons method, we found the area under a) to be:     ", simp(a_div, x_a, funcA, H_a))
print("The true value of a) is 8.145773950169553")
print("The error from the Trapezoidal method is:                       ", 8.145773950169553 - trap(a_div, x_a, funcA, H_a))
print("The error from the Simpsons method is:                           ", 8.145773950169553 - simp(a_div, x_a, funcA, H_a))

print("------------------------------------------------------------------------------------")

print("Using the Trapezoidal method, we found the area under b) to be:  ", trap(b_div, x_b, funcB, H_b))
print("Using the Simpsons method, we found the area under b) to be:     ", simp(b_div, x_b, funcB, H_b))
print("The true value of b) is 1.772453850905516")
print("The error from the Trapezoidal method is:                       ", 1.772453850905516 - trap(b_div, x_b, funcB, H_b))
print("The error from the Simpsons method is:                          ", 1.772453850905516 - simp(b_div, x_b, funcB, H_b))
print(" ")
print("Hence our calculations from using both methods are extremely accurate.")


"""Completed on Thurs May 26  14:46:44 2022 """
"""Final Edits on Mon May 30  17:45:42 2022 """
