# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:26:13 2020

@author: Nathan
"""


from numpy import zeros
N = 1000
C = zeros([N,N], float)

for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i,j] += A[i,k]*B[k,j]