import numpy as np 
def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    rolling_std = []
    k = window_size
    n = len(values)
    for i in range(n-k+1):
        std_sum = 0 
        for j in range(i, i+k):
            mean = sum(values[i:i+k])/window_size
            std_sum += (values[j]-mean)**2

        rolling_std.append(np.sqrt(std_sum/window_size))

    return np.array(rolling_std).tolist()
            