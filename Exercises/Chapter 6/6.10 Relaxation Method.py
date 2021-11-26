"""
This exercises asks us to use the relaxation method to find solutions to the equation:

f(x) = 1 - e^(-cx)

Where c is a free parameter. Use the relaxation method to estimate f(x) while varying c. Plot the output.

Note the regime change from when x = 0 to x > 0 . In physics this a phase transition called the percolation constant. In epidimeology, it is the epidemic threshold.
"""

import numpy as np
from matplotlib import pyplot as plt


def relaxation(consts, accuracy):
    c = consts[0]
    
    points = 300
    cpoints = np.linspace(0, 3, points)
    fx = []

    for c in cpoints:
        error = 1.0
        x1 = 1.0
        while error > accuracy:
            x1, x2 = 1 - np.exp(-c * x1), x1
            error = np.abs((x1 - x2)/(1 - np.exp(-2 * x1)/2))
        fx.append(x1)

    plt.plot(cpoints, fx)
    plt.xlabel('c, free parameter')
    plt.ylabel('x')
    plt.ylim(-0.1, 1.1)
    plt.title('Percolation Tranisition')
    plt.savefig('Exercises/Chapter 6/6.8 percolation_transition.png', format='png')
    plt.show()
    return fx

if __name__ == '__main__':
    
    sol = relaxation(consts = [2], accuracy = 1E-6)
    