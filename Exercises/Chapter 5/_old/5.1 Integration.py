# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:04:59 2020

@author: Nathan
"""

from numpy import loadtxt, linspace, sin, cos
from pylab import plot, show, xlabel

def f(x): # the derivative of the velocity function - gives position at x = t
    return cos(x)


data = loadtxt("velocities.txt", float)
t = data[:,0] # assign time array to t
v = data[:,1] # assign velocities array to v

# Part A, calculate distance (integral of v over all t) using trapezoidal rule

N = len(t)
a = t[0] # Lower bound for t
b = t[-1] # Upper bound for t, also good way to get last element in the list!
h = (b-a)/N

# See the velocity graph over time - NOTE it's a sin wave
plot(t,v)

s = 0.5*f(a) + 0.5*f(b) # initialize the sum with the two known values


distance_plot = []

for k in range(0,N):
    distance_plot.append(s) # Collect distance travelled in a list to plot
    s += abs(f(a+k*h)) # we want distance travelled, not displacement! Use abs()

    
print("The total distance, s, covered by the particle is: ", s)

# Display plot of the distance
plot(t, distance_plot)
xlabel("time (s)")
show()
    
    