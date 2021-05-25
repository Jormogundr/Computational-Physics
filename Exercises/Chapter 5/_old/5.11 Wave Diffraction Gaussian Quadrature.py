# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:37:39 2020

@author: Nathan

More gaussian quadrature work.

This program is unfinished, skipped due to time 
"""


from gaussxw import gaussxw
from numpy import sqrt, cos, sin, pi
from pylab import plot, show, xlabel, ylabel, linspace


# Constants go here
N = 50
# Functions go here
def C(u):
    return cos(0.5*pi*u**2)

def S(u):
    return sin(0.5*pi*u**2)

# Variables go here

wavelength = 1 # meter
z = 3 # meters, horizontal position component
x = linspace(-5,5,50)
u = x*sqrt(2/(wavelength*z))
a = 0
b = u




# Generate the legendre polynomial zeroes, rescale your sample point positions (under integrand)
# and rescale your weighting function
x, w = gaussxw(N)
xk = 0.5*(b-a)*x + 0.5*(b+a)
wk = 0.5*(b-a)*w

C_sum = 0 # initialize sum
plot = []

for k in range(N):
    plot.append(C_sum)
    C_sum += wk[k]*C(xk[k])
    

y_axis = plot
plot()
show()
