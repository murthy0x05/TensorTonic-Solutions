import numpy as np

def euclidean_distance(x, y):
    return np.linalg.norm(np.array(x) - np.array(y))