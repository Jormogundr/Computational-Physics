# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:07:25 2020

@author: Nathan
"""

# This program is quite possibly incorrect :> See page 74

# This program calculates the electric potential between atoms in a NaCl crystal lattice
# also called the Madelung constant as a summation of all potentials. The crystal
# lattice we say is a cube with side length L

from math import sqrt

epsNought = 8.9876e9 # Nm2/C2
fundE = 1.6022e-19 # C
L = 15 # number of atoms in perpendicular direction
M = 0.0 # initial madelung constant in case of potential felt at origin. Note that M is defined as the total electric potential felt by an atom in a solid
const = epsNought*fundE # fundamental potential constant over permitivity of free space

a = float(input("Enter the distance between the atoms, a = "))


for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
           
            if (i == j == k == 0): # Handles division by zero case when at origin
                continue
          
            V = (1/sqrt((i*a)**2+(j*a)**2+(k*a)**2))*const
            
            if ((i+j+k)%2 != 0): # Check if atom is negatively or positively charged by looking at position in the latice
                V *= -1
        
            M += V
                
print("The madelung constant is ", M)
        