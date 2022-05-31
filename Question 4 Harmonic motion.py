"""
Created on Fri May 27 18:39:08 2022
@author: Mish
Assignment 2
Question 4 Harmonic Motion
"""

import matplotlib.pyplot as plt
import numpy as np

#Runge Kutta Intergration
# d^2x/dt^2 = -k*x
# Replace with 2 first order ODEs

#dx/dt = v : f = v
#dv/dt = -kx : g = -kx

#Given v0 and x0, we can update the two to solve for x(t)

x = 10          #initial position
v = 2           #initial velocity
t = 0           #initial time
k = 1           #spring constant
h = 0.001       #time step
gamma = 0.2     #damping constant
n = 0.01        #drag coefficient  for fluid

def f(t,x,v):   #created functions for dx/dt
    return v

def g(t,x,v):   #and dv/dt
    return -k*x

def i(t,x,v):
    return -k*x - gamma*v #and the damped version

def a(t,x,v):       #and now in a fluid
    return -k*x - n*v*v


def RKUTTA_X(fa,ga,x,v,t,k,h): 
    x_values = []   #array to store values

    
    for n in np.arange(0,10000,1):  #collects all the values for x using Runge Kutta
        k_0 = h*fa(t,x,v)
        l_0 = h*ga(t,x,v)
    
        k_1 = h*fa(t+0.5*h, x+0.5*k_0, v+0.5*l_0)
        l_1 = h*ga(t+0.5*h, x+0.5*k_0, v+0.5*l_0)
    
        k_2 = h*fa(t+0.5*h, x+0.5*k_1, v+0.5*l_1)
        l_2 = h*ga(t+0.5*h, x+0.5*k_1, v+0.5*l_1)

        k_3 = h*fa(t+h, x+k_2, v+l_2)
        l_3 = h*ga(t+h, x+k_2, v+l_2)
    
        x = x + (1/6)*(k_0 + 2*k_1 + 2*k_2 + k_3)
        v = v + (1/6)*(l_0 + 2*l_1 + 2*l_2 + l_3)
        t = t+h
        x_values.append(x)
        
    return x_values

def T(t,h): 
    t_values = []
    
    for n in np.arange(0,10000,1):  #collects all the values for t
        t = t+h
        t_values.append(t)
        
    return t_values

plt.plot(T(t,h), RKUTTA_X(f,g,x,v,t,k,h), label = "No Damping")
plt.plot(T(t,h), RKUTTA_X(f,i,x,v,t,k,h),"-y", label = "With Damping")
plt.plot(T(t,h), RKUTTA_X(f,a,x,v,t,k,h),"-r", label = "Fluid")
plt.legend() 
plt.show()

"""Completed on Mon May 30  19:58:08 2022 """
"""Final Edits on Tue May 31  13:15:59 2022 """
