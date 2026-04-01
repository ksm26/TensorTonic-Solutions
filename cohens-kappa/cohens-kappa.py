import numpy as np
from collections import Counter

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    r1 = np.array(rater1)
    r2 = np.array(rater2)

    n= len(r1)

    p_0 = np.sum(r1==r2)/n

    c1 = Counter(r1)
    c2 = Counter(r2)

    labels = set(c1.keys()).union(set(c2.keys()))

    p_e = 0.0 

    for k in labels : 
        p1 = c1.get(k,0)/n
        p2 = c2.get(k,0)/n
        p_e += p1 * p2 

    if 1 - p_e == 0:
        return 1.0
        
    kappa = (p_0 - p_e) / ( 1 - p_e)

    return kappa