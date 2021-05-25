# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:45:11 2020

@author: Nathan
"""


from numpy import sqrt
from pylab import plot, show, xlabel, ylabel, scatter
from gaussxw import gaussxw

def f(x, y, z):
    return 1/sqrt(x**2+y**2+z**2)**3

G = 6.664e-11 # Gravitational consant
N = 100
L = 10 # length of a side of the square
a = L/2
b = -L/2
sigma = 1 # mass per unit area

# Rescale legendre polynomial zeroes (weights) and sample points
x, w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a) # formula 5.61 rescale independent variable (spacing)
wp = 0.5*(b-a)*w # formula 5.62 rescale the weighting function

plot(xp)
show()

s = 0.0
Fz_list = []
for k in range(0,N):
    for m in range(0,N):
        s += wp[k]*f(xp[k], yp[m], 1) 

Fz = 0
for z in range(0,11):
    Fz_list.append(Fz)
    Fz += s*G*sigma*z
    
print(Fz)
    