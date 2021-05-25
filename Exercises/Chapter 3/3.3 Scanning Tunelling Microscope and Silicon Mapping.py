# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:58:38 2020

@author: Nathan
"""


from numpy import loadtxt
from pylab import imshow, hot,show

data = loadtxt("stm.txt", float)
imshow(data, origin="lower")
hot()
show()