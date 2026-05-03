import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    classes = set(y_true)
    n = len(classes)

    # map class to index 
    class_to_index = {c:i for i,c in enumerate(classes)}

    # build confusion matrix 
    cm = np.zeros((n,n), dtype=int)

    for t,p in zip(y_true, y_pred):
        i = class_to_index[t]
        j = class_to_index[p]
        cm[i][j] +=1

    # compute TP, FP,FN
    TP = np.diag(cm)
    FP = np.sum(cm,axis=0) - TP
    FN = np.sum(cm,axis=1) - TP
    support = np.sum(cm,axis=1)

    # Accuracy
    accuracy = np.sum(TP) / np.sum(cm)

    # Safe division
    def safe_div(a, b):
        return a / b if b != 0 else 0.0

    precision_per_class = np.array([safe_div(TP[i], TP[i] + FP[i]) for i in range(n)])
    recall_per_class = np.array([safe_div(TP[i], TP[i] + FN[i]) for i in range(n)])
    f1_per_class = np.array([
        safe_div(2 * precision_per_class[i] * recall_per_class[i],
                 precision_per_class[i] + recall_per_class[i])
        for i in range(n)
    ])

    # Step 4: averaging
    if average == "micro":
        TP_total = np.sum(TP)
        FP_total = np.sum(FP)
        FN_total = np.sum(FN)

        precision = safe_div(TP_total, TP_total + FP_total)
        recall = safe_div(TP_total, TP_total + FN_total)
        f1 = safe_div(2 * precision * recall, precision + recall)

    elif average == "macro":
        precision = np.mean(precision_per_class)
        recall = np.mean(recall_per_class)
        f1 = np.mean(f1_per_class)

    elif average == "weighted":
        weights = support / np.sum(support)
        precision = np.sum(precision_per_class * weights)
        recall = np.sum(recall_per_class * weights)
        f1 = np.sum(f1_per_class * weights)

    elif average == "binary":
        if pos_label not in classes:
            raise ValueError("pos_label not found in labels")
        idx = class_to_index[pos_label]
        precision = precision_per_class[idx]
        recall = recall_per_class[idx]
        f1 = f1_per_class[idx]

    else:
        raise ValueError("Invalid average type")

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }


    