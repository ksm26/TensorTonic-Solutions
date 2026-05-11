import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    result = scores.copy()
    T = result.shape[-1]

    for i in range(T):
        for j in range(T) :
            if j > i : 
                result[..., i, j] = mask_value

    return result
            
            