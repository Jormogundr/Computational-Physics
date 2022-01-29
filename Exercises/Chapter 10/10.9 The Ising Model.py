"""
"""

import numpy as np
from random import choice
import matplotlib.pyplot as plt

# Constants
J = 1 # positive interaction
T = 1 # temperature
kb = 1 # boltzmann 
N = 10000 # number of MC iterations to run

# Given dimensions of lattice n and m, generate a 2D array where the elements are either magnetic pole with spin up (1) or spin down (-1). Return this 2D array.
def initializeRandomLattice(m, n):
    lattice = np.zeros((m, n), dtype=int)
    for i in range(0, m):
        for j in range(0, n):
            lattice[i][j] = choice([1, -1]) 
    return lattice

def calculateLatticeEnergy(L):
    m, n = len(L), len(L[0])
    E = 0
    for row in range(0, n):
        for col in range(0, m):
            directions = [[row,col - 1], [row - 1,col], [row,col + 1], [row + 1,col]]
            for dir in directions:
                i, j = dir[0], dir[1]
                adjE = 0
                if i >= 0 and j >= 0 and i < m - 1 and j < n - 1: # lattice bounds check
                    adjE = L[i,j]*L[i - 1,j] + L[i + 1,j]*L[i,j] + L[i,j + 1]*L[i,j] + L[i,j]*L[i,j - 1]
                E += adjE
    return -J*E

def calculateMagnetization(L):
    M = 0
    m, n = len(L), len(L[0])
    for i in range(0, m):
        M += np.sum(L[i])
    return M


def main():
    L = initializeRandomLattice(20, 20)
    M = []
    E = calculateLatticeEnergy(L)

    # Main loop
    for k in range(0, N):
    
        # choose random particle to flip/move
        i = choice(range(0, len(L)))
        j = choice(range(0, len(L[0])))
        s = L[i][j] # initial spin

        # calculate energy before and after spin change
        Ei = calculateLatticeEnergy(L)
        L[i][j] = s*(-1) 
        Ej = calculateLatticeEnergy(L)
        
        if Ej <= Ei: # accept the move
            E += Ej - Ei
        else: # reject the move
            L[i][j] = s
        
        magnetization = calculateMagnetization(L)
        M.append(magnetization)
    
    xaxis = range(0, N)
    plt.plot(xaxis, M)
    plt.xlabel("Number of iterations, N")
    plt.ylabel("Total Magnetization, M")
    plt.show()

if __name__ == '__main__':
    main()