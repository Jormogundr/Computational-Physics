# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:53:31 2020

@author: Nathan
wrong
"""

from numpy import e
from pylab import plot, show, linspace

ANALYTIC_SOLUTION = 0.886207

def f(t):
   return e**-t**2 # careful with the syntax, (-t)**2 =/= -t**2

N = 1000
a = 0
b = 3
h = (b-a)/N

# Part A

s = 0 # initialize the sum at zero

for k in range(1,N):
    s += f(a+k*h)
    
c    # from the formula 5.3 on pg 142 
print(solution)


# Part B

s = 0 # initialize the sum at zero
graph = []

for k in range(1,N):
    s = (h)*(0.5*f(a)+0.5*f(b)+f(a+k*h))
    print(s)
    graph.append(s)
    
x = linspace(0, 1000, 999) 
plot(x,graph) # this plot shows the positive side of a bell curve
show()