import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    values, counts = np.unique(y, return_counts=True)
    probs = counts / counts.sum()
    
    entropy = -np.sum(probs * np.log2(probs, where=probs > 0))

    return entropy
    
    