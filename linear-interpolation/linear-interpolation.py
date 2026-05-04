def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    values = values[:]   # copy list
    n = len(values)

    i = 0

    while i < n:
        if values[i] is None:
            left = i - 1

            # find right boundary
            right = i
            while right < n and values[right] is None:
                right += 1

            # fill missing values
            for j in range(i, right):
                values[j] = (
                    values[left]
                    + (j - left) / (right - left)
                    * (values[right] - values[left])
                )

            i = right
        else:
            i += 1

    return values