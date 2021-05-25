# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:55:36 2020

@author: Nathan

This program uses Gaussian quadrature
"""

from gaussxw import gaussxw
from numpy import e
from pylab import plot, show, xlabel, ylabel, linspace

BOLTZMANN_CONSTANT = 8.617e10-5 # eV/K
DEBYE_TEMPERATURE = 428 # K

def f(x):
    return (x**4*e**x)/(e**x - 1)**2

def coeff(V, phi, T):
    return 9*V*phi*BOLTZMANN_CONSTANT*(T/DEBYE_TEMPERATURE)**3

N = 50
T = 100 # K, this can be whatever!

x, w = gaussxw(N)

a = 0  # lower limit to domain of integration
b = DEBYE_TEMPERATURE/T

xp = 0.5*(b-a)*x + 0.5*(b+a) # formula 5.61 rescale independent variable (spacing)
wp = 0.5*(b-a)*w # formula 5.62 rescale the weighting function

phi = 6.022e28 # atoms/cubic meter
V = 1000 # cubic meters

s = 0.0  # initialize sum
Cv = []
for k in range(N):
    Cv.append(s)
    s += wp[k]*f(xp[k])
    
s = coeff(V, phi, T) * s
print(s)

x_axis = linspace(5,500,N) # N number of evenly spaced intervals
y_axis = Cv
xlabel("Temperature (K)")
ylabel("Heat Capacity")
plot(x_axis, y_axis)
show()


