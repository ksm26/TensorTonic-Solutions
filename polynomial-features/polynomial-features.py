def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    result = []

    for v in values :
        row = []
        for i in range(degree+1):
            row.append(v**i)

        result.append(row)

    return result