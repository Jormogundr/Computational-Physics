# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:16:39 2020

@author: Nathan

Wave interference example for a 1 x 1 m region of pond with two wave sources
"""
from math import sqrt,sin,pi
from numpy import empty
from pylab import imshow, gray,show

wavelength = 5.0
k = 2*pi/wavelength
xi0 = 1.0
separation = 20.0 # separation of centers in cm
side = 100.0 # side of the square in cm
points = 500 # number of grid points along each side
spacing = side/points # spacing of points in cm

# Calculate the positions of the centers of the circles
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Make an array to store the heights
xi = empty([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = sqrt((x-x1)**2+(y-y1)**2)
        r2 = sqrt((x-x2)**2+(y-y2)**2)
        xi[i,j] = xi0*sin(k*r1) + xi0*sin(k*r2)
        
# Make the plot
imshow(xi, origin="lower", extent =[0,side,0,side])
gray()
show()
                    


