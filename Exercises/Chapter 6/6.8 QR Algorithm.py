"""
CH 6 - Page 246
This program implements the QR decomposition algorithm to find the eigenvalues of a square, symmetric matrix (suitable for a wide array of physics applications). 

TODO: Find a faster method to generate the QR decomposition, rather than using nested for loops. 

"""

import numpy as np

# Takes a real matrix A (N x N) and returns two matrices Q and R that form its QR decomposition.
def QRAlgo(A):
    N = len(A)

    # check that the matrix is square and return if not
    assert N == len(A[0]), "Matrix is not square."

    Q = np.zeros((N,N))
    U = np.zeros((N,N))
    R = np.zeros((N,N))

    for i in range(0, N):
        v = 0
        for j in range(0, i):
            v += np.dot(Q[j], A[i]) * Q[j]
        U[i] = A[i] - v
        Q[i] = U[i]/np.linalg.norm(U[i])

        for k in range(0, N):
            if k >= i:
                R[i][k] = np.dot(Q[i], A[k])
            else:
                R[i][k] = 0

    Q = np.transpose(Q)
    return Q, R

# Takes a matrix A and returns the eigenvalues.
def findEigenValsVect(A):
    epsilon = 10E-6 # convegence threshold - algorithm stops when non-diagonal values fall below this constant
    threshold = 1

    while threshold > epsilon:
        Rk,Qk = QRAlgo(A) # reverse the order of these matrices - required for algo to work
        A = np.matmul(Qk,Rk)
        nonDiagMatrix = np.extract(~np.eye(A.shape[0], dtype=bool), A) # creates a boolean mask where diagonal is True, inverts it, and applies mask to A
        threshold = np.amax(nonDiagMatrix)

    return np.diagonal(A)
    
if __name__ == '__main__':
    A = np.array([[1,4,8,4],
                [4,2,3,7],
                [8,3,6,9],
                [4,7,9,2]])

    Lambda = findEigenValsVect(A)
    print("\n\nThe eigenvalues of the matrix are ", Lambda)