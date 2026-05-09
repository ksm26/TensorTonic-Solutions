import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    if not documents:
        return np.zeros((0, 0)), []
        
    vocab = set()
    for doc in documents:
        row = doc.lower().split()
        for name in row : 
            vocab.add(name)

    vocab = list(vocab)
    vocab.sort()

    # creating work to column index mapping 
    word_to_idx = {word : idx for idx,word in enumerate(vocab)}
    df = Counter()

    # compute document frequency 
    df = Counter()

    for doc in documents:

        unique_words = set(doc.lower().split())

        for word in unique_words:
            df[word] += 1

    # 4) compute IDF
    N = len(documents)

    idf = {}

    for word in vocab:
        idf[word] = math.log(N / df[word])

    #5: Initialize TF-IDF matrix
    tfidf_matrix = np.zeros((N, len(vocab)))

    # 6: Fill matrix

    for row, doc in enumerate(documents):

        words = doc.lower().split()

        tf = Counter(words)

        for word, count in tf.items():

            col = word_to_idx[word]
            tf = count / len(words)

            tfidf_matrix[row][col] = tf * idf[word]

    return tfidf_matrix, vocab
    