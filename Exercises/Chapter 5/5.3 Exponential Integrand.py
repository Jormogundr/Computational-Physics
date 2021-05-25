# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:10:34 2021

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt 


N = 10
a = 0
x = np.linspace(0,3,10)
b = x
h = (b-a)/N

def f(t):
    arg = -(t**2)
    return np.exp(arg)

def Simpsons():
    factor = (1/3)*h
    s_even = 0
    s_odd = 0
    
    for k in range(1,N,2): # odd summation
        s_odd += f(a + k*h)
    
    for k in range(2,N,2): # even summation
        s_even += f(a + k*h)
    
    return factor*(f(a) + f(b) + 4*s_odd + 2*s_even)

print(x)
print(Simpsons())

plt.plot(x,Simpsons())
plt.xlabel('x')
plt.ylabel('E(x)')