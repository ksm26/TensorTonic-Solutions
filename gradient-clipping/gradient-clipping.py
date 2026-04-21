import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """

    g = np.array(g, dtype=float)
    
    if max_norm <= 0:
        return g
        
    norm = np.sqrt(np.sum(g**2))
    if norm <= max_norm:
        return np.array(g.tolist())

    scale = max_norm / norm 
    gclipped = g * scale

    return np.array(gclipped.tolist())
    