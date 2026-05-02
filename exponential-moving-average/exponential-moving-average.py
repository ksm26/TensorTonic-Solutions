def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    result = [values[0]]

    for i in range(1,len(values)):
        curr = alpha * values[i] + result[-1]*(1-alpha)
        result.append(curr)

    return result