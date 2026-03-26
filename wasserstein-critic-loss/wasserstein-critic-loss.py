import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    r = np.array(real_scores)
    f = np.array(fake_scores)
    diff = np.mean(f) - np.mean(r)
    return float(diff)
    