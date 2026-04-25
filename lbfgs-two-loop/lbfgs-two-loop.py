def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))

def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """
    m = len(s_list)
    rho = [1.0 / _dot(y_list[i], s_list[i]) for i in range(m)]
    alpha = [0.0] * m

    q = grad.copy()
    
    for i in range(m-1,-1, -1):
        
        alpha[i]= rho[i] * _dot(s_list[i], q)
        q = [qi - alpha[i] * yi for qi, yi in zip(q, y_list[i])]

    gamma = _dot(s_list[-1], y_list[-1])/ _dot(y_list[-1],y_list[-1])

    r = [gamma * qi for qi in q]

    for i in range(m):
        beta = rho[i] * _dot(y_list[i], r)
        r = [ri + s_list[i][j] * (alpha[i] - beta) for j, ri in enumerate(r)]

    return [-ri for ri in r ]

        
