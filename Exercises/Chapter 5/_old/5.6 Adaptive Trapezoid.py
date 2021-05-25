# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:30:06 2020

@author: Nathan
"""
from numpy import sin, sqrt

ANALYTIC_SOLUTION = 0.455832

# N is passed as a parameter to the trapezoid function, user defined
a = 0 # lower limit
b = 1 # upper limit
# width of slice is calculated in the function
epsilon = 10e-6 # solution must be accurate to this error - i.e. correct up to 6 decimal places


def f(x):
    return sin(sqrt(100*x))**2

def trapezoidal(N):
    
    s = 0 # initialize sum at zero
    h = (b-a)/N
    
    for k in range(1,N-1,2): # odd sum
        s += f(a+k*h)
    for k in range(2,N-2,2): # even sum
        s += f(a+k*h)
    
    total = h*(0.5*f(a) + 0.5*f(b) + s)
    
    return total

def error(Ii, I_previous):

    return (1/3)*(Ii-I_previous)

def previous_trapezoidal(N, h): # Ii-1
    Ni_minus_one = int(0.5*N)
    hi_minus_one = 2*h
    s = 0 
    
    for k in range(1, Ni_minus_one-1):
        s += f(a+k*hi_minus_one)
    
    return hi_minus_one*(0.5*f(a) + 0.5*f(b) + s)

N = int(input("Enter the number of steps, N: "))
h = (b-a)/N

I = 0

for k in range(1,N-1,2):
    I += f(a+k*h)
    
I_previous = previous_trapezoidal(N, h)
Ii = 0.5*I_previous + h*I # Total in1tegral estimate, from equation 5.34 
print(abs(Ii-0.45))

while (abs(ANALYTIC_SOLUTION - Ii) > epsilon):
    N = 2*N
    h = (b-a)/N
    
    I = 0
    
    for k in range(1,N-1,2):
        I += f(a+k*h)
        
    I_previous = previous_trapezoidal(N, h)
    Ii = 0.5*I_previous + h*I # Total in1tegral estimate, from equation 5.34 
    
    print("\n Integral estimate is: ", Ii, "\n Number of slices: ", N, "\n With approximation error: ", error(Ii, I_previous))
    print(abs(ANALYTIC_SOLUTION - Ii))