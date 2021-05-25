# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:59:32 2021

@author: Nate
"""

N = 1000 # number of slices
a = 0 # lower limit of integration
b = 2 # upper limit of integration
h = (b-a)/N


def f(x):
    return x**4 - 2*x + 1

def Simpsons():
    factor = (1/3)*h
    s_even = 0
    s_odd = 0
    
    for k in range(1,N,2): # odd summation
        s_odd += f(a + k*h)
    
    for k in range(2,N,2): # even summation
        s_even += f(a + k*h)
    
    return factor*(f(a) + f(b) + 4*s_odd + 2*s_even)
        

observed = Simpsons()


accepted  = 4.4
error = observed/accepted
print("Using extended simpsons method ", observed)
print("Error", error)