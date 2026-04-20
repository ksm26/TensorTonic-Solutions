import numpy as np

def bottleneck_block(x, W1, W2, W3, Ws):
    """
    Returns: np.ndarray with bottleneck residual block output (compress, process, expand + skip)
    """
    x = np.array(x)
    W1 = np.array(W1)
    W2 = np.array(W2)
    W3 = np.array(W3)
    Ws = np.array(Ws)

    a = np.maximum(0, x@W1)
    b = np.maximum(0, a@ W2)
    c = b @ W3
    out = np.maximum(0, c + x @ Ws)
    return out 
    
    
    