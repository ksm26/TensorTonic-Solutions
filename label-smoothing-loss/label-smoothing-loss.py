import numpy as np
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    k = len(predictions)
    q = []
    for i in range(k):
        if i == target :
            q.append((1-epsilon) + epsilon/k)
        else :
            q.append(epsilon/k)

    loss = -sum(qi * np.log(pi) for qi,pi in zip(q,predictions))

    return loss

    
        