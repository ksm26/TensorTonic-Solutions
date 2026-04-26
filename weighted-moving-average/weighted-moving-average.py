def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    total = sum(weights)
    result = []
    l = len(weights)
    
    for i in range(len(values)-l + 1 ):
        mat = []
        for j in range(l):
            mat.append(values[i+j]*weights[j])

        result.append(sum(mat)/total)

    return result