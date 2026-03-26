import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.array(x)
    pmf = []
    for i in range(len(x)):
        if x[i] == 0 :
            pmf.append(1-p)
        else :
            pmf.append(p) 

    mean = float(p)
    var = float((p*(1-p)))
    return np.array(pmf),mean,var
    