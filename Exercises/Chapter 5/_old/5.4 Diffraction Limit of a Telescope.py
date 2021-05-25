# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:38:54 2020
PHYS453 - CH 4 Homework
Graph the first four spherical Bessel functions.

@author: Nate Pierce
"""

from numpy import pi, cos, sin
from pylab import linspace
import matplotlib.pyplot as plt

# to output .svg vector plot
%matplotlib inline
%config InlineBackend.figure_format = 'svg'

# Constants 
N = 1000 # number of slices in simpson integration method
a = 0 # lower limit of integration
b = pi # upper limit of integration
h = (b-a)/N # width of each slice, dx
FUNCS_TO_PLOT = 9 # number of bessel functions to plot

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


def main():
    # initialize vars for generating J(x)
    x = linspace(0, 20, 1000)
    l = 0
    Jl = 0
    
    # loop for easy control of plots to generate 
    while l < FUNCS_TO_PLOT:
        Jl = J(l, x)
        plt.plot(x, Jl, label=("For \u2113 = {}".format(l)))
        l += 1

    # display/graph
    plt.grid(b=True, which='both')
    plt.xlabel("x")
    plt.ylabel("J\u2113(x)")
    plt.title("PHYS453 - HW 4 Computation: Graphs of Spherical Bessel Functions")
    plt.legend()
    plt.xlim(0, 14)
    plt.show()

if __name__ == '__main__': 
    main()



        
        
        
        
        
        
        
        