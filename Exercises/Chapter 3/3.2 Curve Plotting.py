# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:16:42 2020

@author: Nathan

Zoom in to see the other functions for A and B. The plot of Fay's function dominates'
"""

from math import pi
from numpy import linspace, sin, cos, exp
from pylab import plot, show, xlabel, ylabel, xlim, ylim

def parametricX(theta):
    x = 2*cos(theta)+(cos(theta))**2
    return x

def parametricY(theta):
    y = 2*sin(theta)-(sin(theta))**2
    return y

def polar_to_cart_x(r,theta):
    x = r*cos(theta)
    return x

def polar_to_cart_y(r,theta):
    y = r*sin(theta)
    return y


theta = linspace(0,2*pi,100) # for the Deltoid curve

# Part A, Deltoid Curve
xlabel("Radians")
plot(parametricX(theta),parametricY(theta), "--r")

# Part B, Galilean spiral
theta = linspace(0,10*pi,100) # for the galilean spriral
r = theta**2 # galilean spiral
gal_x = polar_to_cart_x(r, theta)
gal_y = polar_to_cart_y(r,theta)

plot(gal_x,gal_y)

# Part C, Fey's function
theta = linspace(0,24*pi,100) # for Fey's function
r = exp(cos(theta))-2*cos(4*theta)+(sin(theta/12))**5
feys_x = polar_to_cart_x(r, theta)
feys_y = polar_to_cart_y(r,theta)
plot(feys_x,feys_y)



show()