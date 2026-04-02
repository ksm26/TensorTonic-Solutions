import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    losses = []
    for y, p in zip(y_true, y_pred):
        p = max((min(p, 1-eps), eps))
        l = -(y*math.log(p) + (1-y)* math.log(1-p))
        losses.append(l)

    return losses
    