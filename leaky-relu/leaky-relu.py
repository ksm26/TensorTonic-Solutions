import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    ans = []
    for i in range(len(x)):
        if x[i] >= 0 :
            ans.append(x[i])
        else : 
            ans.append(alpha*x[i])
    return np.array(ans) 