from math import sin, sqrt
from random import random

from numpy import var

def f(x):
        return (sin(1/(x*(2-x))))**2

# Given an exact integral, calculate it using a random process (Monte Carlo Simulations)
def hitOrMissMethod():
    N = 10000
    k = 0
    for i in range(N):
        x = 2*random()
        y = random()
        if y<f(x):
            k += 1
    A = 2
    I = A*k/N # we know the integral is over a region x = 2 and y = 1, so the area (A) is 2. The formula is I ~= kA/N.
    sigma = sqrt(I*(A - I))/sqrt(N)
    return I, sigma
    

def meanValueMethod():
    b = 2
    a = 0
    N = 10000
    sum = 0
    sum_squared = 0
    for i in range(0, N):
        x = (b - a)*random()
        y = f(x)
        sum += y
        sum_squared += y**2
    I = (b - a)*sum/N
    var_f = sum_squared/N - (sum/N)**2
    sigma = (b - a)*sqrt(var_f)/sqrt(N)
    return I, sigma

def main():
    I1, sigma1 = hitOrMissMethod()
    print("Approximate integral using 'hit or miss' method = {0} with error = {1}".format(I1, sigma1))
    I2, sigma2 = meanValueMethod()
    print("Approximate integral using mean value method = {0} with error = {1}".format(I2, sigma2))
    print("The mean value method is more precise by a factor of {0}".format(sigma1/sigma2))

if __name__ == '__main__':
    main()