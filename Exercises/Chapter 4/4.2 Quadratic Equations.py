# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:06:33 2020

@author: Nathan
"""

from math import sqrt

a = 0.001
b = 1000.0
c = 0.001

# Part A
pos_signed_solution = (-b + sqrt(b**2 -4*a*c))/(2*a)
neg_signed_solution = (-b - sqrt(b**2 -4*a*c))/(2*a)
print(pos_signed_solution,neg_signed_solution)

# Part B 
alt_pos_signed_solution = (2*c)/(-b+sqrt(b**2-(4*a*c)))
alt_neg_signed_solution = (2*c)/(-b-sqrt(b**2-(4*a*c)))
print(alt_neg_signed_solution,alt_neg_signed_solution)


"""
The discrepancy between the two answers appears to be due to an accumulation of error
in the numerator for Part A vs the denominator for part B

Skipped part C for now 

"""