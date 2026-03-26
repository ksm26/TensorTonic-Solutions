import math 
import numpy as np

def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    losses = []
    for i in range(len(targets)):
        if targets[i] == 0 :
            pt = 1-predictions[i]
        else :
            pt = predictions[i]

        losses.append(-alpha* ((1-pt)**gamma)*math.log(pt))

    return np.mean(losses)