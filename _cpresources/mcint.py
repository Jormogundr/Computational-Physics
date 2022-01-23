from math import sin
from random import random

# Given an exact integral, calculate it using a random process (Monte Carlo Simulations)
def f(x):
    return (sin(1/(x*(2-x))))**2

N = 10000
count = 0
for i in range(N):
    x = 2*random()
    y = random()
    if y<f(x):
        count += 1
I = 2*count/N # we know the integral is over a region x = 2 and y = 1, so the area (A) is 2. The formula is I ~= kA/N.
print(I)
