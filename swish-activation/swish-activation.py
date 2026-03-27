import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x)
    ans = [x[i] * (1/(1+np.exp(-x[i]))) for i in range(len(x))]

    return np.array(ans)