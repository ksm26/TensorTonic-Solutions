import math
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    total_log_prob = 0
    for i in range(len(actual_tokens)):
        p = prob_distributions[i][actual_tokens[i]]
        total_log_prob += math.log(p)

    N = len(actual_tokens)
    H = -(total_log_prob / N)

    return math.exp(H)