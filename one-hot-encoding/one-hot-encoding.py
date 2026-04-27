import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    if not num_classes: 
        numclass = max(y) +1 
    else : 
        numclass = num_classes    
    result = []
    for i in y :
        row = [0]*numclass
        row[i] = 1
        result.append(row)

    return result 
        