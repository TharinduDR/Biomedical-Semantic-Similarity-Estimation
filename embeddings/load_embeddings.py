import gensim


def load_word2vec(path):
    word2vec = gensim.models.KeyedVectors.load_word2vec_format(path, binary=True)
    return word2vec
