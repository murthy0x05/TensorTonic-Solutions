import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    p_arr = np.maximum(np.array(p, dtype=np.float64), eps)
    q_arr = np.maximum(np.array(q, dtype=np.float64), eps)
    return float(np.sum(p_arr * np.log(p_arr / q_arr)))