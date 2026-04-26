import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    n,m = A.shape

    matrix = np.zeros((m,n))

    for i in range(n):
        for j in range(m):
            matrix[j][i] = A[i][j]

    return matrix
    
