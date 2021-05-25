# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:52:49 2020

@author: Nathan

"""

# Remember to NOT use sqrt from math but from numpy
from math import pi
from numpy import linspace, sqrt
from pylab import plot, show

# Below I calculate the graph of the integrand to see it's a semi circle

x = linspace(-1,1,100)
y = sqrt(1-x**2)
plot(x,y)
show()

radius = 1
area_of_semi_circle = pi*radius**2/2
print("Using pi and radius, the area is: ", area_of_semi_circle)

# Convert the integral to a Riemann sum
# We're interested at what N we can reasonably run this program, for analytic lim N goes to inf

N = 1000000 # Number of 'slices' over the domain of the integral
h = 2/N # Width of the slices. Note: 2/N due to symmetry of curve.

I = 0

for k in range(1,N):
    x_sub_k = -1 + h*k
    y_sub_k = sqrt(1-x_sub_k**2)
    I += h*y_sub_k
    if k % 100  == 0:
        print("iteration ", k, "of ", N)
    else:
        continue
    
print("Using the Riemann sum, the area is: ", I, " for ", N, " slices.")

percent_error = abs(area_of_semi_circle - I) * 100
print("The percent error is: %", percent_error)