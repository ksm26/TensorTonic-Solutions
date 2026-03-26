import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Write code here
    q_stable = [item + eps for item in q] 
    summation = 0 
    for i in range(len(p)):
        if p[i] > 0 :
            summation += p[i] * np.log(p[i]/q_stable[i])

    return summation