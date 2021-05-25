# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:51:44 2021

@author: Nate
Complete.
"""

import pandas as pd
import matplotlib as mpl 
import matplotlib.pyplot as plt 


def x(v,t): # position
    return v*t
    

data = pd.read_csv('velocities.txt', comment='#', delim_whitespace=True, names=['time(s)', 'velocities (m/s)'])
t = data['time(s)']
v = data['velocities (m/s)']

x = x(v,t) # distance


print(data)
plt.plot(t,x, label='Distance')
plt.plot(t,v, label='Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.legend()
