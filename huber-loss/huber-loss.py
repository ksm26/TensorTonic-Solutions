import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    e = np.array(y_true) - np.array(y_pred)

    ans = []
    for i in e : 
        if abs(i) <= delta: 
            loss = i*i/2
        else : 
            loss = delta * ( abs(i) - delta/2)
        ans.append(loss)

    return np.mean(np.array(ans))