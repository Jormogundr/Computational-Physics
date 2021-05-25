# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:34:30 2020

@author: Nathan
"""


# This program defines a function that takes a number n as an argument, 
# and checks to see if that number has any factors besides 1 and itself.
# We could say that this function checks if n is prime. n is prime if
# the return list if empty.

def factors(n):
    
    factorList = [] # empty list
    k = 2 # k is our test number to probe the number n to see if it is prime
   
    while (k <= n): # k can only be a factor of n if less than or equal to n
        while (n % k == 0): # k is only a factor of n if n divided by k has no remainder
            factorList.append(k) # add k to our list of factors of n
            n //= k
        k  += 1
        
    return factorList

a = int(input("Enter a number to test whether the number is prime or not: "))

x = len(factors(a))

if x == 1: # Why 1? Our factors function checks if k divides n when k=n which is always true, so the list must have at least one element, prime or not.
    print("The number is prime! It has no factors other than 1 and itself.")
else:
    print("The number is not prime.")
    