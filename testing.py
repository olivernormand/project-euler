import numpy as np

def pN(n):
    return 0.5 * (3 * n - 1) * n

def ipN(y):
    return (1 + np.sqrt(1 + 24 * y)) / 6

def is_pentagonal(y):
    if ipN(y).is_integer():
        return True
    return False
