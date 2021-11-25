"""
Incomplete: Cannot reconstruct A=QR from the returned matrices. 
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
    v = 0

    for i in range(0, N):
        for j in range(0, i):
            v = np.dot(Q[j], A[i]) * Q[j]
        U[i] = A[i] - v
        Q[i] = U[i]/np.linalg.norm(U[i])

        for k in range(0, N):
            if k >= i:
                R[i][k] = np.dot(Q[i], A[k])
            else:
                R[i][k] = 0
            print(R)

    return Q, R
    




if __name__ == '__main__':
    A = np.array([[1,4,8,4],
                [4,2,3,7],
                [8,3,6,9],
                [4,7,9,2]])

    Q, U = QRAlgo(A)
    print("Q*R: \n", np.matmul(Q,U), "\n\n A: \n", A)