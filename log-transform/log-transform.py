import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    y = []
    for i in values :
        y.append(math.log(1+i))

    return y 