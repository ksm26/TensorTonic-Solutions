import numpy as np
import math
def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    result = []
    for pos in range(seq_length):
        row = []
        for i in range(d_model):
            theta = pos/(10000**(2*(i//2)/d_model))
            if i %2 == 0 :
                row.append(math.sin(theta))
            else :
                row.append(math.cos(theta))
        result.append(row)

    return np.array(result)
    