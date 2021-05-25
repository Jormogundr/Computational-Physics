# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:02:09 2020

@author: Nathan

NOTE: The graphs running averages seems off because the formula provided on pg 98 seems questionable?
"""

# See pg 62 for example on sums from files 

from numpy import loadtxt
from pylab import plot, show, xlabel, ylabel, xlim, ylim

def SunspotAv(y):
    p = 0 # iterator to move our sunspot subspace along
    
    sunsptRunningAvg = []
    
    while(p < 3000):
        yk = 0 # needs to be reset to 0 for every subspace calculation.
        # yk stores our summation for each subspace of 10 sunspots in y
        
        for m in range(0,11):
            m += p
            yk += y[m]
         
        Yk = (1/11)*yk # use Yk to store the list of average sunspots
        sunsptRunningAvg.append(Yk)
        print(Yk)
        
        p += 10 # this is where I increment through the sunspots list

    return sunsptRunningAvg
        
       
        
    # return the sum as float to multiply by the constant

#Collect data        
data = loadtxt("sunspots.txt",float)
x = data[:,0] # load all months from 1st col of txt into x list
y = data[:,1] # load all sunspot counts from 2nd col of txt into y list

# Format graph
xlabel("Months")
ylabel("N Sunspots")
xlim(0,1000)
plot(x,y)
xSunSpt = range(0,300) # The SunspotAv function returns a list of 300 avgs, so we need a matching x dimension, which this accomplishes
plot(xSunSpt,SunspotAv(y))
show()
