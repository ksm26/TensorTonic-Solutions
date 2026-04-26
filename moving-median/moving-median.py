def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    median = []

    for i in range(len(values)-window_size +1):
        row = sorted(values[i:i+window_size])
        if window_size %2 != 0 :
            median.append(row[window_size//2])
        else :
            median.append((row[window_size//2 - 1] + row[window_size//2]) / 2)

    return median
        