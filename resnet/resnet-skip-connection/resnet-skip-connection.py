import numpy as np

def compute_gradient_with_skip(gradients_F: list, x: np.ndarray) -> np.ndarray:
    """
    Compute gradient flow through L layers WITH skip connections.
    Gradient at layer l = sum of paths through network
    """
    x = np.array(x, dtype=float)
    
    y = x.copy()
    
    for F in gradients_F:
        F = np.array(F, dtype=float)
        I = np.eye(F.shape[0])
        y = y @ (I + F)   # <-- key fix
    
    return y


def compute_gradient_without_skip(gradients_F: list, x: np.ndarray) -> np.ndarray:
    """
    Compute gradient flow through L layers WITHOUT skip connections.
    """
    y = np.array(x, dtype=float) 
    for F in gradients_F :
        y = y @ np.array(F, dtype=float) 

    return y
