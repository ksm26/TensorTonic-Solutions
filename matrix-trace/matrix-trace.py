import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    count = 0 
    for i in range(len(A)):
        row = A[i]
        for j in range(len(row)):
            if i == j :
                count += A[i][j]

    return count
