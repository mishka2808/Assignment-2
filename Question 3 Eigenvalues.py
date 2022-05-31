"""
Created on Thu May 26 09:49:51 2022
@author: Mish
Assignment 2
Question 3 Eigenvalues
"""
import numpy as np


pauli_1 = np.array([ [0 , 1], [1, 0] ])
pauli_2 = np.array([ [0 , -1j], [1j, 0] ])
pauli_3 = np.array([ [1, 0], [0, -1] ])
matrix = np.array([ [4 , 1] , [2 , -1] ])

#-----------------------------------------------------------------------------------------
def bisect(mat, a, b, epsilon):
    """
    Idea: 
    |00-l   01 | = 0   ...00,11,01,10 are positions of the matrix, not actual numbers
    |10    11-l|
    => 0 = l^2 + l[-(11+00)] + [(00)(11) - (10)(01)]
    rewrite: al^2 + bl + c
    a = 1
    b = [-(11+00)]
    c =[(00)(11) - (10)(01)]
    => 0 = x^2 + bx + c =f(x)
    """
#-----------------------------------------------------------------------------------------
    a_00 = mat[0,0]             #creates the variables for the function
    a_11 = mat[1,1]
    a_01 = mat[0,1]
    a_10 = mat[1,0]
    
    d = (-1)*(a_11+a_00)
    e = ((a_00)*(a_11) - (a_10)*(a_01))
    
#-----------------------------------------------------------------------------------------

    def f(x):                   #defines the function of lambda. This way we can replace x easily with our boundaries.
        f = (x)**2 + x*d + e
        return f
    alreadygiven = False
    error = abs(b - a)
    
    while error > epsilon :     
        
        c = (b + a)/2           #c is the midway point of the interval

        if f(a)*f(b) > 0:      #just incase there is a case where there are no roots or too many roots,
            print("No roots present. Bisection will not work.") #it will only accept functions with 1 root
            alreadygiven = True
            break              #otherwise it will quit out of the loop entirely
        
        elif f(a)*f(b) == 0 or f(c) == 0:
            alreadygiven = True
            if f(a) == 0:
                print("Root at: x =     ", a)
                break       
            elif f(b) == 0:
                print("Root at: x =     ", b)
                break 
            elif f(c) == 0:
                print("Root at: x =     ", c) 
                break   
    
            
        elif f(c)*f(a)<0:       #checks to see if f(c)*f(a) is negative, if so, then the new boundary for b is c, since the root lies between a and c
            b = c
            error = abs(b-a)
        
        elif f(c)*f(b)<0:       #checks to see if f(c)*f(b) is negative, if so, then the new boundary for a is c, since the root lies between b and c
            a = c
            error = abs(b-a)
            
    if alreadygiven == False: 
        print("The error is     ", error)
        print("The new lower boundary is:   " , a , "   and the new upper boundary is:    ", b )

            


print("FOR PAULI 1 MATRIX")
print("First root:")
print(bisect(pauli_1, -2.33, 0, 0.01 )) #should be close to -1
print("")
print("Second root:")
print(bisect(pauli_1, 0.5 , 2.53, 0.01)) #should say +1 
print("-------------------------------------------------------------------------------")
print("FOR PAULI 2 MATRIX")
print(bisect(pauli_2, -5 , 5, 0.5))  #no roots 
print("-------------------------------------------------------------------------------")
print("FOR PAULI 3 MATRIX")
print("First root:")
print(bisect(pauli_3, 0 , 2.33, 0.01))
print(" ")
print("Second root:")
print(bisect(pauli_3, -2.33 , 0, 0.01))
print("-------------------------------------------------------------------------------")
print("FOR GIVEN MATRIX")
print("First root:")
print(bisect(matrix, -2.33 , -0.5, 0.01)) 
print(" ")
print("Second root:")
print(bisect(matrix, 4.35 , 7.5, 0.5))
print("-------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------

def secant(mat, x0, x1, n): #x0 and x1 are the boundary conditions (a and b) while n is the number of iterations
    a_00 = mat[0,0]             
    a_11 = mat[1,1]
    a_01 = mat[0,1]
    a_10 = mat[1,0]

    d = (-1)*(a_11+a_00)
    e = ((a_00)*(a_11) - (a_10)*(a_01))

    def f(x):                   #defines the function
        f = (x)**2 + (x)*d + e
        return f
    
    for intercept in range(1, n):  #will start to iterate over n times to find the roots

        fx0 = f(x0) #we evaluate our 2 guesses/boundary 
        fx1 = f(x1)
        
        xi = x0 - (fx0 / ((fx0 - fx1) / (x0 - x1))) #same as equation 4.2, just written differently
        
        x0 = x1
        x1 = xi
        
    if f(x1)*f(x0) > 0:
      print("No roots found after:     ", n, "iterations")
    else:
      print("The root was found to be  at " , xi, " after " , n, "iterations") 
      
     
print("FOR PAULI 1 MATRIX")
print("First root:")
print(secant(pauli_1, 0, 2, 10))
print("")
print("Second root:")
print(secant(pauli_1, -2, 0, 10))
print("-------------------------------------------------------------------------------")
print("FOR PAULI 2 MATRIX")
print(secant(pauli_2, -2.33, 5, 10))
print("-------------------------------------------------------------------------------")
print("FOR PAULI 3 MATRIX")
print("First root:")
print(secant(pauli_3, 0 , 2.33, 10))
print(" ")
print("Second root:")
print(secant(pauli_3, -2.33 , 0, 10))
print("-------------------------------------------------------------------------------")
print("FOR GIVEN MATRIX")
print("First root:")
print(secant(matrix, -3.338 , -0.5, 10)) 
print(" ")
print("Second root:")
print(secant(matrix, 2 , 8.9, 10))
print("-------------------------------------------------------------------------------")

"""Comparision between the secant and bisectional method:
    Initial Expectations:
        Initially I expected the difference between both the secant and bisectional method to be almost negligible.
        From what I've learnt, the bisectional method is a different form of the secant method, more specifically when calculating:
            According to the bisection method, our value for c is (b+a)/2.
            Similarly, according to the secant method, this value can be expressed by x0 - (fx0 / ((fx0 - fx1) / (x0 - x1))) which is
            just an easier way (personally) of describing the equation (4.2) in our notes.
        My expectation was that there wouldn't be too much of a change 
        
    The Reality:
        Both methods work quite well in determining the eigenvalues of the matrix. I suggest that the bisection method is a bit more reliable than the secant method as the
        bisection method calculates the root based within the users error value where as the secant method (despite being the "mother" of the bisection method)
        it relies more on the number of iterations the user would like to make. In my opinion, the comparison of these two methods are solely based on the user inputs
        such as the boundaries, error and iteration."""
        
"""Completed on Tue May 31  18:14:48 2022 """
