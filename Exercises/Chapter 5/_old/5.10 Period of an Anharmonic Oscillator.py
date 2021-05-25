# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:34:40 2020

@author: Nathan

This program uses Gaussian quadrature
"""


from gaussxw import gaussxw
from numpy import sqrt
from pylab import plot, show, linspace, xlabel, ylabel

def V(A, x): # The potential function
    return 1/sqrt(A**4 - x**4)


N = 20 # determines the legendre polynomial zeroes via the gaussxw function, used to
# calculate x and w 
a = 0 # physically, when the particle is at the origin
A = 2 # physically, the maximum amplitude
m = 1 # mass

x, w = gaussxw(N)
xk = 0.5*(A-a)*x + 0.5*(A+a)
wk = 0.5*(A-a)*w

# For loop that calculates the area under the curve
s = 0
period_plot = []
for k in range(N):
    period_plot.append(s)
    s += wk[k]*V(A, xk[k])
    

print("Period of oscillator is ", s*sqrt(8*m), " seconds.")

x_axis = linspace(0,2,20)
y_axis = period_plot
xlabel("Amplitude")
ylabel("Period (T)")
plot(x_axis, y_axis)
show()