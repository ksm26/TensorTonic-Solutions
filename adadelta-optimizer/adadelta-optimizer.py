import numpy as np

def adadelta_step(w, grad, E_grad_sq, E_update_sq, rho=0.9, eps=1e-6):
    """
    Perform one AdaDelta update step.
    """
    w = np.array(w)
    grad = np.array(grad)
    E_grad_sq = np.array(E_grad_sq)
    E_update_sq = np.array(E_update_sq)

    # Step 1: Update squared gradient average
    E_grad_sq = rho * E_grad_sq + (1-rho) * (grad**2)

    # Step 2: Compute update
    RMS_update = np.sqrt(E_update_sq + eps)
    RMS_grad = np.sqrt(E_grad_sq + eps)
    delta_w = - (RMS_update / RMS_grad) * grad

    # Step 3: Update squared update average
    E_update_sq = rho * E_update_sq + (1 - rho) * (delta_w ** 2)

    
    w_t = w + delta_w

    return w_t, E_grad_sq, E_update_sq
    
    