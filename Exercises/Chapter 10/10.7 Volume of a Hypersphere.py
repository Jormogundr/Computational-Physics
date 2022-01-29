"""
Monte Carlo integration is best suited for finding the area under the curve of pathological functions. It's accuracy increases at a slower rate with increasing sample points N compared to other integration methods 
(such as trapezoidal). The other scenario best suited for MC is high dimension integration, where the number of sample points rapidly grows N*10^n (where n is the dimension).

This program 
"""
from random import choice

# Constants
n = 10 # number of dimensions
b = 1 # upper limit
a = -1 # lower limit

def f(space):
    r = 0
    for dim in space:
        r += dim**2
    if r <= 1:
        return 1
    else:
        return 0

def generateRndCoords():
    coords = []
    for i in range(0, n):
        t = choice(range(-1000,1000))/1000
        coords.append(t)
    return coords
    
def multiDimensionMonteCarlo():
    N = int(1E4)
    sum = 0
    for i in range(0, N):
        space = generateRndCoords()
        val = f(space)
        sum += val
    I = 2**n*sum/N
    return I

def main():
    I2 = multiDimensionMonteCarlo()
    print("Approximate integral using mean value method = {0}".format(I2))

if __name__ == '__main__':
    main()