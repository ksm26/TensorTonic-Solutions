import math

def get_percentile(arr, pct):
    arr.sort()
    n = len(arr)
    k = (n-1) * pct/100
    low_idx = math.floor(k)
    high_idx = math.ceil(k)

    if low_idx == high_idx:
        return arr[low_idx]

    fraction = k - low_idx
    return arr[low_idx] + fraction * (arr[high_idx] - arr[low_idx])
    
def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    original = values[:]

    # sorted copy for percentile calculation
    arr = sorted(values)

    # compute percentile bounds
    lower = get_percentile(arr, lower_pct)
    upper = get_percentile(arr, upper_pct)

    result = []

    # clip values
    for x in original:
        x = max(lower, min(upper, x))
        result.append(x)

    return result


