import numpy as np

def sigmoid(x):
    X = np.asarray(x, dtype = float)
    return 1 / (1 + np.exp(-X))