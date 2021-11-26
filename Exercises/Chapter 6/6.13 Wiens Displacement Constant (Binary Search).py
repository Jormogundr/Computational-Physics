"""
This exercise demonstrates binary search, or bissection search, to find the zeros of a nonlinear function, in this case the roots of the function that give the maximum wavelength (peak intensity)
of a blackbody emitter at temperature T. The function is therefore the derivative of Wien's displacement function set equal to 0. 

Here, we set x = hc/(kb*Lambda*T).

We do not look for roots below 0 - we know that 0 must be a solution to the function 5*np.exp(-x) + x -5 = 0 by inspection, so the search bracket [x1, x2] is adjusted accordingly to ensure that
x1 and x2 have different signs (a requirement of binary search to find roots). Note that binary search does NOT work when f(x) has an even number of roots, so we set our left bracket to a position
just past 0, effectively ignorning the x = 0 root.

Once the root is found, compute the surface temperature of the sun. Wien's displacement law is the basis of of the optical pyrometry methodoly, which is used to estimate temperatures of an object 
from the peak wavelength they emit (Lambda of the sun ~ 502 nm).
"""

import numpy as np

# The function to find the roots of.
def f(x):
    return 5*np.exp(-x) + x -5

# Given two points, check that they have opposite signs after evaluating the function f(x) at those points. Returns True if the signs are different.
def oppSigns(x1, x2):
    fx1, fx2 = f(x1), f(x2)
    return np.sign(fx1) != np.sign(fx2)

def binarySearch(bracket):
    x1, x2 = bracket[0], bracket[1]
    accuracy = 1E-6
    error = 1
    zeros = []
    x = 0

    # Check if 0 is a root. 
    if f(x) == 0: 
        zeros.append(0)

    N = 0 # track number of iterations to complete binary search
    while error > accuracy and oppSigns(x1, x2):
        xp = 0.5*(x1 + x2)
        y = f(xp)

        if not oppSigns(xp, x1):
            x1 = xp
        else:
            x2 = xp
        
        error = np.abs(x1 - x2)
        N += 1
        
    zeros.append(0.5*(x1 + x2))
    print('Binary search completed in ', N, ' steps.')
    return zeros

# Given the position x of the non-zero root of f(x), use the fact that T = b/(lambda * x) to compute the surface temperature of the sun, where the peak wavelength Lambda is 502nm
def sunSurfaceTemp(y):
    kb = 1.3806E-23
    Lambda = 502E-9
    c = 2.99E8
    h = 6.626E-34
    b = h*c/kb
    T = b/(Lambda * y)
    return T


if __name__ == '__main__':
    bracket = [0.5, 10]
    solve = binarySearch(bracket)
    print("The surface temp of the sun is ", sunSurfaceTemp(solve[1]), "K computed from root x of f(x), x =", solve[1])