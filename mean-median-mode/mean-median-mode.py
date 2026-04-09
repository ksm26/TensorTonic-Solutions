import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)

    c = Counter(x)
    mode = [i for i in c.keys() if c[i]==max(c.values())]

    return mean, median,min(mode)