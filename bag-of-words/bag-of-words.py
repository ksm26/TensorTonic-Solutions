import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    if vocab == []:
        return np.array([], dtype=int)
    dict = {}
    for i in tokens: 
        if i in dict.keys():
            dict[i] += 1 
        else : 
            dict[i] = 1 

    ans = []
    for j in vocab :
        if j in dict.keys():
            ans.append(dict[j])
        else : 
            ans.append(0)

    return np.array(ans)