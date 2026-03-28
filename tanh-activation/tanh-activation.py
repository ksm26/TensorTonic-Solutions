import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    result = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return np.array(result, ndmin=1)