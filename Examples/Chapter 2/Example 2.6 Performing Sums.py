# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:42:10 2020

@author: Nathan
"""

# Create variable to hold the value of the sum 
# Here we want to find the sum of 1/k for k=1 all the way up to k=100
# The sum function is also useful but generally for loops work better for more complicated sums

s = 0.0 # notice Python sets this to a float by default

# For loops are especially useful in summations like this. We can use k as our iterator, since it is also our index and works in the same way.

for k in range(1,101): 
    s += 1/k
    print(s)

