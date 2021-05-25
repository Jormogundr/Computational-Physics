# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:24:10 2020

The hermite polynomials H(n) get enormous very quickly as n increases. This is a big
problem for computing time. 

NOTE: The computing time for generating the values in Hn is quite high. The author notes
that this should not be the case. Not sure how to improve the speed of the calculation 
of the 0 < n < 30 and -10 < x < 10 situation, in this case. 

THE PROGRAM IS INCOMPLETE.

@author: Nathan
"""


from numpy import e, sqrt
from math import factorial
from pylab import plot, show, xlabel, ylabel


# Write the recursive function for the hermite polynomial
def H(n,x):
    if n == 0:
        return 1
    if n == 1:
        return 2*x
    else: 
        return 2*x*H(n-1,x) - 2*(n-1)*H(n-2,x) # This line was NOT intuitive to me - took 
    # a good few moments of analysis to come up with this.
        
     
# Collect values in a list for 0 > n > 3 and -4 > x > 4
Hn = []
for k in range(0,31): # iterator for n
    if k == 1:
        Hn.append(1)
    for m in range(-10,11): # iterator for x
        print("n is ", k)
        print("x is ", m)
        print("H(n,x) is ", Hn, "\n")
        Hn.append(H(k,m))

# Plot the hermite polynomial lists
plot(Hn)
show()

