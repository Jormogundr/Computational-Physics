# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:07:36 2020

@author: Nathan

This program uses a function to calculate the binomial coefficient of given n,k 
and uses it to display coeffs in the first 20 lines of pascals triangle 
"""
from math import factorial

#Part A, write the function

def binomial(n,k):
    if k == 0:
        return 1
    else: 
        coeff = int((factorial(n)/((factorial(k)*(factorial(n-k))))))
        
    return coeff

n = int(input("Enter the value for n: "))
k = int(input("Enter the value for k: "))
print(binomial(n,k))

# Part B, Pascal's triangle

for n in range (1,21):
    print("Line ", n, " of pascal's triangle includes: ")
    for k in range (0,n+1):
        print(binomial(n, k))
    
# Part C, Coin Flip Probability 
    
x = 100
y = 60

print("The odds of the coin landing on heads 60 times out of 100 flips is ", (binomial(x,y)/2**x)*100, "%")