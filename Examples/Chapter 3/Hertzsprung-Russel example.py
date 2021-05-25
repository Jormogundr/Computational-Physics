# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:00:55 2020

@author: Nathan
"""


from pylab import scatter,xlabel,ylabel,xlim,ylim,show
from numpy import loadtxt

data = loadtxt("stars.txt", float)
x = data[:,0]
y = data[:,1]

scatter(x,y)
xlabel("Temperature")
ylabel("Magnitude")
xlim(13000,0) # Historically, HR diagrams have axes descending in values
ylim(20,-5)
show()