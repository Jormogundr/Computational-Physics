# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:52:28 2020

@author: Nathan
"""

# Here we will calculate the wavelengths for different series of discrete emissions of radiation
# at different excitation levels using a nested for loop.

R = 1.097e-2
for m in [1,2,3]:
    print("For series", m, " the wavelengths are: \n")
    for k in range(1,6): # Could have used same method as line 12
        n = m + k   # This line prevents calculating the equation when m = n, which makes no physical sense
        invLambda = (1/R)**((1/m**2)-(1/n**2))
        print(1/invLambda, " when the electrons falls from excited state", n, "\n")
        n += 1
