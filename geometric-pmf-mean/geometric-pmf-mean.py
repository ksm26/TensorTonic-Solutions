import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    
    pmf = []
    for i in k :
        pmf.append((1-p)**(i-1)*p)

    return (np.array(pmf), 1/p)
        