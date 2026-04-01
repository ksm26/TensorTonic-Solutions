import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    e = np.array(y_true) - np.array(y_pred)
    abs_e = np.abs(e)

    loss = np.where(
        abs_e <= delta,
        0.5*e**2,
        delta * ( abs_e - 0.5*delta)
    )
    
    return np.mean(loss)