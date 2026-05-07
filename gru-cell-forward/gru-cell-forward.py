import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    Wz = params['Wz']
    Wr = params['Wr']
    Wh = params['Wh']

    Uz = params['Uz']
    Ur = params['Ur']
    Uh = params['Uh']

    bz = params['bz']
    br = params['br']
    bh = params['bh']

    z_t = _sigmoid(x@Wz + h_prev @Uz + bz)

    r_t = _sigmoid(x @Wr + h_prev @Ur + br)
    hatt = np.tanh(x@Wh + (r_t*h_prev) @Uh + bh)
    ht = (1-z_t)*h_prev + z_t *hatt

    return ht
    