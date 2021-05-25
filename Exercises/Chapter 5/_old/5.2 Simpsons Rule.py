# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:58:22 2020

@author: Nathan
"""

ACCEPTED_VALUE = 4.4 # The analytic solution to our integral

def f(x):
    return x**4-2*x+1

N = 10 # number of slices 
a = 0.0 # lower bound of integration
b = 2.0 # upper bound of integration
h = (b-a)/N # width of each quadratic section

odd = 0
for k in range(1,N,2): # summation over odd terms, third argument is incrementation
    odd += f(a+k*h)

even = 0
for k in range(2,N,2): # summation over even terms
    even += f(a+k*h)
   
final = (1/3*h)*(f(a) + f(b) + (4*odd) + (2*even)) # formula on pg 146

percent_error = (final-ACCEPTED_VALUE)/ACCEPTED_VALUE * 100

print(final, "Percent error: ", percent_error, "%")

# As can be seen compared to exercise 5.1 (which uses the trapezoidal rule)
# Simpsons rule is much more accurate for smaller N