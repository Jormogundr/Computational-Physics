# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:00:32 2020

@author: Nathan
"""

def Factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*(Factorial(n-1))
    
user_defined_n = int(input("Enter an integer value to calculate its factorial: "))
print(Factorial(user_defined_n))
    
# Now, use float
user_defined_n = float(input("Enter an integer value to calculate its factorial: "))
print(Factorial(user_defined_n))

"""

Why does this occur? Because Python uses arbitrary precision for integer values, meaning
it will roll over to more memory addresses as needed. Essentially, integer values
have infinite precision, so long as enough memory is available. Float values only fill
one memoy address at a time, limiting their values to 64 bits or 32 bits, meaning they are not
infinite in precision. That is why you will see an INF print when calculating the float for
large n as opposed to a number for integers.

"""