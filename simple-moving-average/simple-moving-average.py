def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    k = len(values)

    result = []

    for i in range(k-window_size+1):
        result.append(sum(values[i:i+window_size])/window_size)

    return result