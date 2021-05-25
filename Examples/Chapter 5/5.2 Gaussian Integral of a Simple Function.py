# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:31:08 2020

@author: Nathan
"""


from gaussxw import gaussxw # Created by the author, Mark Newman

def f(x):
    return x**4 - 2*x  + 1

N = 3 # number of sample points, N is chosen based on degree of polynomial. In this case
# the degree of our polynomial f(x) is 4. So we choose N = 3 because gaussian quadrature
# works for any polynomial up to degree 2N - 1.
a = 0.0
b = 2.0

# Calculate the sample points and weights, then map them to the required integration domain

x, w = gaussxw(N) # formula 5.64 gives w from zeroes of Nth legendre polynomial. This line 
# returns two variables, not just one. x (sample points) and w (weights) are arrays
xp = 0.5*(b-a)*x + 0.5*(b+a) # Rescaled x from formula 5.61
wp = 0.5*(b-a)*w # Rescaled w from formula 5.62

# Perform the integration
s = 0.0

for k in range(N):
    s += wp[k] *f(xp[k])
    
print(s)