# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:12:32 2020

@author: Nathan

Use Gaussian quadrature to estimate an integral running over an infinite domain
using the techniques from section 5.8. See pg 180
"""


from gaussxw import gaussxw
from math import exp

def f(z):
    return exp(-z**2/(1-z)**2)*(1/(1-z)**2) # We had to distribute the exponent in the first
# power to the -z and (1-z) to make this works

N = 50 # number of legendre polynomial zeroes to calculate
a = 0.0
b = 1.0
x, w = gaussxw(N)
xk = 0.5*(b-a)*x + 0.5*(b+a)
wk = 0.5*(b-a)*w

s= 0.0
for k in range(N):
    s += wk[k]*f(xk[k])
    
print(s)