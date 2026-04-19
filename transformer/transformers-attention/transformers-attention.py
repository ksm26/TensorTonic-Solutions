import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    # Your code here
    raw_attn = torch.matmul(Q,K.transpose(-2,-1))
    dk = K.shape[-1]
    attn = F.softmax(raw_attn/math.sqrt(dk), dim=-1)
    return torch.matmul(attn,V)