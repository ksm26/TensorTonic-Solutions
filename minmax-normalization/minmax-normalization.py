import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    mini = np.min(X,axis, keepdims = True)
    maxi = np.max(X,axis, keepdims = True)

    deno = np.maximum(maxi-mini, eps)

    return (X-mini)/deno