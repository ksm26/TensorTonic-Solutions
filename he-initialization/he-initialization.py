def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    L = np.sqrt(6/fan_in)

    W = np.array(W, dtype=float)
    W2 = W * (2*L) - L 
    return W2