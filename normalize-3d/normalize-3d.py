import numpy as np
import math

def normalize_3d(v):
    v_arr = np.asarray(v, dtype=float)
    orig_shape = v_arr.shape

    if v_arr.ndim == 1:
        norm = np.linalg.norm(v_arr)
        if norm > 0:
            v_arr = v_arr / norm
        return v_arr

    if v_arr.ndim == 2 and v_arr.shape[1] == 3:
        norms = np.linalg.norm(v_arr, axis=1, keepdims=True)
        return np.divide(
            v_arr,
            norms,
            out=np.zeros_like(v_arr),
            where=norms > 0
        )

