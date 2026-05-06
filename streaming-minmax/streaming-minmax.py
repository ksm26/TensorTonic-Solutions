import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    state_dict = {
        'min': np.full(D, np.inf),
        'max': np.full(D, -np.inf)
    }
    return state_dict

def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    X_batch = np.array(X_batch)

    # Update running min and max feature-wise
    state['min'] = np.minimum(state['min'], X_batch.min(axis=0))
    state['max'] = np.maximum(state['max'], X_batch.max(axis=0))

    # Normalize
    normalized = (
        (X_batch - state['min']) /
        np.maximum(state['max'] - state['min'], eps)
    )

    return normalized
    