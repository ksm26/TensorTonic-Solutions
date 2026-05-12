import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    def factorial(a):
        total = 1 
        for i in range(1,a+1):
            total *= i 

        return total

    fact_k = factorial(k)
    pdf = np.exp(-lam) * (lam)**k / fact_k

    cdf = 0

    for i in range(k+1):
        fact_i = factorial(i)
        cdf += np.exp(-lam) * (lam)**i / fact_i

    return pdf, cdf