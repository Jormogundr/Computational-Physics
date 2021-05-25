# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:50:06 2020

@author: Nathan

Completed, solutions verified. 
"""


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
   
def catalan(n):
     if n==0:
         return 1
     else:
         return ((4*n-2)/(n+1))*(catalan(n-1))
     
def euclids(m,n):
    if n==0:
        return m
    else:
       return euclids(n, m % n)
   
for n in range(1,101):
    print(n, "! is ", factorial(n))
    
# Part A, Catalan numbers
    
for n in range (1,101):
    print("Cn: ", n, " is ", catalan(n))
    
# Part B, Euclid's Algorithm
    
m = 192
n = 108
print("Via euclid's algorithm, the gcd of ", m, " and ", n , " is ", euclids(m,n))


    
