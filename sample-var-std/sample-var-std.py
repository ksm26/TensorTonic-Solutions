import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    m = np.mean(x)
    a = [(i-m)**2 for i in x]
    n = len(x)
    s = (1/(n-1))*np.sum(a)

    return s, np.sqrt(s)