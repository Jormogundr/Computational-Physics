"""
This program showcases Newton's method - a numerical computation method to find the roots of a non-linear functiob.

In this case, the non-linear function is the sixth Legendre polynomial (over an interval from 0 to 1), which is a 6th degree polynomial. 

There is no general formula to find the zeros of such a function analytically, but they can be easily found programmtically.

Newton's method will converge to a solution at a quadratic rate, making it much faster than relaxation and binary search when it comes to finding the zeros of a non-linear function.

One downside to the algorithm is that a guess of the roots must be provided. This is easy enough to overcome by plotting the function, then approximating the roots visually. This is done here.

"""

import numpy as np
from matplotlib import pyplot as plt
from numpy.matrixlib import defmatrix

def P(x):
    Px = 924*np.power(x,6) - 2772*np.power(x,5) + 3150*np.power(x,4) - 1680*np.power(x,3) + 420*np.power(x,2) - 42*x + 1
    return Px
    
def dP(x):
     derivative = 42 * (132*np.power(x,5) - 330*np.power(x,4) + 300*np.power(x,3) - 120*np.power(x,2) + 20*x - 1)
     return derivative

# INPUT: A linspace x.
# OUTPUT: Plot of P(x) vs x.
def plot(x):
    y = P(x)
    plt.plot(x, y)
    plt.show()

# INPUT: A list of roots (rough estimates) based on the plot of P(x). 
# OUTPUT: A list of computed roots using Newton's method.
def newtonsMethod(roots):
    accuracy = 1E-10
    x = roots[0]
    computed_roots = []

    for x in roots:
        error = 1
        while error > accuracy:
            dx = P(x)/dP(x)
            x = x - dx
            error = np.abs(dx)
        computed_roots.append(x)

    return computed_roots

if __name__ == '__main__':
    xaxis = np.linspace(0, 1, 100) # start, stop, steps
    roots_guess = [0.03, 0.17, 0.04, 0.62, 0.83, 0.96] # generated from the plot of the function
    solve = newtonsMethod(roots_guess)
    print("Guessed roots are ", roots_guess, " and computed roots are ", solve)