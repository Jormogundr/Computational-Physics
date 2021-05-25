# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:49:11 2020

@author: Nathan

This program generates a sodium chloride crystal lattice visually, where 
an atom is surrounded by the other type of atom at all perpendicularities. 
Also generates an fcc lattice (part b)

See pg 114


"""

# Na will be red
# Cl will be blue

# Part A, the lattice

from vpython import sphere, vector, color
from math import sqrt

L = 5
R = 0.3
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if (i+j+k) % 2 == 0:
                sphere(pos=vector(i,j,k),radius=R,color=color.red)
            else:
                sphere(pos=vector(i,j,k),radius=R,color=color.blue)
        
                
# Part B, Face center cubic of solid metal
                
R = 0.1
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
                print(i,j,k)
                sphere(pos=vector(i,j,k),radius=R,color=color.red)
                sphere(pos=vector(i*sqrt(2),j*sqrt(2),k*sqrt(2)),radius=R,color=color.red)
                
# There's likely a much better way to do this, but it does work! Not a big deal for such a small lattice.
                
                