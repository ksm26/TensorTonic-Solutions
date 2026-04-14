def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    result = []
    left = 0

    for i in range(len(values)):
        row = []
        for j in range(degree+1):
            row.append(values[i]**j)
        result.append(row)

    return result 
        