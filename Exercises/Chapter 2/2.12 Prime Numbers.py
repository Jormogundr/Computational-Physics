# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:25:27 20"20

@author: Nathan

THIS PROGRAM PROVED TOO TIME CONSUMING AT THE TIME, PG 83
"""

from math import sqrt

def Factors(n):
    factorList = []
    k = 2 # iterator to serve as factor checker
    
    while (k <= n): # iterator must be less than n to be a factor
        while (n % k == 0): # condition for when k is a factor of sqrtN
            factorList.append(k)
            n //= k # sqrtN = sqrtN // k
        k += 1
            
    return factorList

primesList = []

for n in range (2,10001):
    if len(Factors(n)) == 1: # condition for determining if n is prime
        primesList.append(n)
        
print(primesList)

for n in range (3,10001):

            
        
    
    
        
    