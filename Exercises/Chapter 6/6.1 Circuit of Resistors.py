# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:06:00 2021

@author: Nate
"""

import numpy as np

A = np.array([[4,-1,-1,-1],
             [-1,3,0,-1],
             [-1,0,3,-1],
             [-1,-1,-1,4]],
             float)
v = np.array([ 5, 0, 5, 0 ],float)
N = len(v)

# Gaussian elimination
for m in range(N):

    # Divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = np.empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print(x)
