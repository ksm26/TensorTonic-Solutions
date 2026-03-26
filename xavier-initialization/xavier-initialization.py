import numpy as np 

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    limit = np.sqrt(6/(fan_in+fan_out))
    Wt = []
    for i in range(len(W)) : 
        row = []
        for j in W[i] :
            row.append(j *(2*limit) - limit)
        Wt.append(row)

    return np.array(Wt)
    