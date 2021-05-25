# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:52:52 2020

@author: Nathan
"""


# Here we are evaluating the integral of x^4-2x+1 using the extended trapezoidal rule
# See page 142 for the math
ACCEPTED_VALUE = 4.4

def f(x):
    return x**4-2*x+1

N = 10 # number of slices (trapezoid)
a = 0.0 # lower bound of integration
b = 2.0 # upper bound of integration
h = (b-a)/N # width of each trapezoid

s = 0.5*f(a) + 0.5*f(b) # determines the first and last terms in the sum so we can simplify our series

for k in range(1,N):
    s += f(a+k*h)
    
final = h*s
percent_error = (final-ACCEPTED_VALUE)/ACCEPTED_VALUE * 100
print(final, "Percent error: ", percent_error, "%")

# Increase N to make the computed value agree with the analytic value 