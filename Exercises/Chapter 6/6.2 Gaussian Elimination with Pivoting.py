# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:45:33 2021

@author: Nate
Confirmed working.
"""

import numpy as np
import copy

A = np.array([[ 0,  1, 4, 1 ],
           [ 3,  4,  -1,  -1 ],
           [ 1, -4,  1,  5 ],
           [ 2, -2,  1,  3 ]], float)
v = np.array([ -4, 3, 9, 7 ],float)
N = len(v)



# Gaussian elimination
for m in range(N):
    if A[m,m] == 0:
        pivot = np.max(A[:,m]) # find the value of all first row elements which has the maximum value
        ind = np.where(A[:,m]==pivot) # find the row index value which has the maximum first element
        
        temp1 = copy.deepcopy(A[ind,:]) # use deepcopy to avoid using temp as pointer
        temp2 = copy.deepcopy(A[m])
        
        A[m] = temp1 # make the swap
        A[ind] = temp2 # preserve the row that we swapped to
        
        v[m], v[ind] = v[ind], v[m] 
        
    
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
