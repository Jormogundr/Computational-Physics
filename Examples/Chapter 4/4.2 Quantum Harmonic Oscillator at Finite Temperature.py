# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:05:33 2020

@author: Nathan
"""


from math import exp

terms = 1000
beta = 1/100
S = 0.0
Z = 0.0
for n in range(terms):
    E = n + 0.5 # the energy level of the oscillator at principal quantum number n
    weight = exp(-beta * E) # The weighting function in formula 4.11
    S += weight*E # The sum defined in formula 4.11
    Z += weight # As defined in the question
    print(S/Z) # This gives us <E> for every n