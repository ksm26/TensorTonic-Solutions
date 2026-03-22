import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param = np.array(param) ; grad =np.array(grad) ; m = np.array(m) ; v= np.array(v)
    t = np.array(t)
    mt = beta1*m+(1-beta1)*grad
    vt = beta2*v +(1-beta2)*grad*grad
    mhat = mt/(1-beta1**t)
    vhat = vt/(1-beta2**t)
    param_new = param -(lr*(mhat/(np.sqrt(vhat)+eps)))
    m_new = mt ; v_new = vt
    return (param_new,m_new,v_new)
    pass