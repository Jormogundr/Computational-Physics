# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:05:36 2021

@author: Nate
"""

# Limits of integration (lower, upper respectively)
a = 0
b = 2


def f(x):
    return x**4 - 2*x + 1


def error(I1, I2):
    return abs((1/3)*(I2-I1))


# N = 10
N = 10
h = (b-a)/N
t = 0
for k in range(1, N-1):
    t += f(a+ k*h)
    
I1 = h*(0.5*f(a) + 0.5*f(b) + t)
print(I1)

# N = 20
N = 20
h = (b-a)/N
t = 0
for k in range(1, N-1):
    t += f(a+ k*h)
    
I2 = h*(0.5*f(a) + 0.5*f(b) + t)
print(I2)

print("Approximation error ", error(I1,I2))

print('This error includes rounding error!')