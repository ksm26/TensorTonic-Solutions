import numpy as np

def dropout(x, p=0.5, rng=None):
    x = np.array(x, dtype=float)

    # 🔥 KEY FIX: element-wise randomness
    rand = rng.random(x.shape) if rng else np.random.random(x.shape)

    mask = (rand < (1 - p)).astype(float)
    scale = 1 / (1 - p)

    y = x * mask * scale
    pattern = mask * scale

    return y, pattern