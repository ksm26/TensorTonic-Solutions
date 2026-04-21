def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    result = []
    for i in range(len(X)):
        row = X[i]
        out = []
        for j in range(len(row)):
            for k in range(j+1,len(row)):
                out.append(row[k]*row[j])

        result.append(row+out)

    return result
            