import numpy as np 
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    TP = 0 
    for i in range(len(y_pred)):
        if y_pred[i] == y_true[i]:
            TP += 1 

    FP = len(y_pred) - TP
    FN = FP 

    return (2*TP)/(2*TP + FP + FN)
    