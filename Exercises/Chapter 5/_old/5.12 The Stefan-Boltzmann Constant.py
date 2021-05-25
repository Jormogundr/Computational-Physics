# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:28:56 2020

@author: Nathan
"""


from gaussxw import gaussxw
from math import pi, exp


# CONSTANTS
ALLOWED_ERROR = 1E-12
c = 299792458 # meters/second
hBar = 1.054571800e-34 # Joule-seconds
kb = 1.38064852e-23 # Joules/Kelvin
sigma = 5.670367e-8 # Watts/(meters^2 * Kelvin^4)


# FUNCTIONS
def f(z): 
    print(z)
    if abs(z - 0) <= ALLOWED_ERROR:
        z = 0e-1
        return (z/(1-z))**3/((exp((z/(1-z))))-1)*1/(1-z)**2
    else:
        return (z/(1-z))**3/((exp((z/(1-z))))-1)*1/(1-z)**2

# The problem here is with the exponential function. When the arugment resolves to 0, then
# e^0 is 1, and the denominator is then 1-1 resulting in a division by 0 error.
# I'm not sure how to work around this.

# VARIABLES
N = 10 # number of slices 
a = 0.0 # lower bound of integration
b = 1.0 # upper bound of integration
h = (b-a)/N # width of each quadratic section
odd = 0
for k in range(1,N,2): # summation over odd terms, third argument is incrementation
    odd += f(a+k*h)

even = 0
for k in range(2,N,2): # summation over even terms
    even += f(a+k*h)
   
final = (1/3*h)*(f(a) + f(b) + (4*odd) + (2*even)) # formula on pg 146
print(final)

# x, w = gaussxw(N)
# xk = 0.5*(b-a)*x + 0.5*(b+a)
# wk = 0.5*(b-a)*w

# s = 0.0
# for k in range(N):
#     s += wk[k]*f(xk[k])
    

coeff = kb**4/(4*pi**2*c**2*hBar**3)
