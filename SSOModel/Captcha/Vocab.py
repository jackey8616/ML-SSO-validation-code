import random
import numpy as np

class Vocab():

    def __init__(self):
        self.vocab = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.size = len(self.vocab)
        indices = range(self.size)
        self.index = dict(zip(self.vocab, indices))

    # return random string by given length
    def rand_string(self, length):
        # if len(vocab) == 0 raise exception
        return "".join(random.sample(self.vocab, length))

    # get symbol (char in vocabulary) by its ordinal
    def get_sym(self, idx):
        # if idx >= len(self.vocab) raise exception
        return self.vocab[idx]

    # given a symbol, return its ordinal in given vocabulary.
    def get_index(self, sym):
        return self.index[sym]

    # given 'abc', return [10, 11, 12]
    def to_indices(self, text):
        return [self.index[c] for c in text]

    # given [10, 11, 12], return 'abc'
    def to_text(self, indices):
        return "".join([self.vocab[i] for i in indices])

    # given '01', return vector [1 0 0 0 0 0 0 0 0 0 ... 0 \n 0 1 0 0 0 0 ... 0]
    def text_to_one_hot(self, text):
        num_labels = np.array(self.to_indices(text))
        n = len(text)
        categorical = np.zeros((n, self.size))
        categorical[np.arange(n), num_labels] = 1
        return categorical.ravel()

    # translate one hot vector to text.
    def one_hot_to_text(self, onehots):
        text_len = onehots.shape[0] // self.size
        onehots = np.reshape(onehots, (text_len, self.size))
        indices = np.argmax(onehots, axis = 1)
        return self.to_text(indices)
    
