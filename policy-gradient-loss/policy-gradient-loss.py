import numpy as np 
def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    G = []
    running = 0 
    
    for r in reversed(rewards):
        running = running* gamma + r
        G.append(running)

    G.reverse()
    gmean = np.mean(G)

    At = [i - gmean for i in G]

    
    loss = -np.mean([i * j for i,j in zip(log_probs,At)])

    return float(loss)
    