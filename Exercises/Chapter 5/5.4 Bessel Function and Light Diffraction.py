# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:21:15 2021

@author: Nate

Only Part a is complete, I could not figure out the contour plot.
"""

from numpy import pi, cos, sin
import numpy as np
import math

import matplotlib.pyplot as plt

from pylab import imshow, show # for density plot
from matplotlib import colors

# Constants 
N = 1000 # number of slices in simpson integration method
a = 0 # lower limit of integration
pi = np.pi
b = pi # upper limit of integration
h = (b-a)/N # width of each slice, dx
FUNCS_TO_PLOT = 9 # number of bessel functions to plot
wl = 500E-9 # wavelength in nm
n = 100 # number of points to plot/genarate in arrays

def J(l,x): # bessel function

    def integrand(theta): # bessel function integral
        return cos(l*theta - x*sin(theta))
    
    tot = 0
    even = odd = 0
    
    for k in range(1,N,2): # even index, sums terms in Simpson's rule
        odd += tot + 2*integrand(a+k*h)
    for k in range(2,N,2): # odd number, sums terms in Simpson's rule
        even +=  tot + 4*integrand(a+k*h)
        
    final = ((1/(pi*3)*h)*(integrand(a) + integrand(b) + (4*odd) + (2*even))) # Definition of extended Simpson's rule
    
    
    return final

def I(radius): # intensity of diffraction pattern, symmetric wrt radius
    k = (2*pi)/wl
    kr = k*radius
    J1 = J(1, kr)
    I  = (J1/kr)**2
    return I


# initialize vars for generating J(x)
x = np.linspace(0, 20, n)
l = 0
Jl = 0

# loop for easy control of plots to generate 
while l < FUNCS_TO_PLOT:
    Jl = J(l, x)
    plt.plot(x, Jl, label=("J{}".format(l)))
    l += 1

# display/graph
plt.grid(b=True, which='both')
plt.xlabel("x")
plt.ylabel("J\u2113(x)")
plt.legend()
plt.xlim(0, 14)
plt.show()


