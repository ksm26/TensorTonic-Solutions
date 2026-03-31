def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    cos = sum(a*b for a,b in zip(x1,x2))/(math.sqrt(sum(a*a for a in x1))*math.sqrt(sum(a*a for a in x2)))

    if label == 1 :
        loss = 1-cos
    else : 
        loss = max(0,cos-margin)
    return loss
        