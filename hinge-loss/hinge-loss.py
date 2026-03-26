import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    
    loss = []
    for i in range(len(y_score)):
        loss.append(np.maximum(0,margin-y_score[i]*y_true[i]))

    if reduction == "mean" : 
        return float(np.mean(loss))
    else : 
        return float(np.sum(loss))