import numpy as np

def pN(n):
    return 0.5 * (3 * n - 1) * n

def ipN(y):
    return (1 + np.sqrt(1 + 24 * y)) / 6

def is_pentagonal(y):
    if ipN(y).is_integer():
        return True
    return False


limit = 5000

j = 0
for i in range(1, limit):
    print(i)
    for k in range(i + 1, limit):
        pi = pN(i); #print(pi)
        pk = pN(k); #print(pk)
        if is_pentagonal(pi + pk) and is_pentagonal(pk - pi):
            print(pi, pk)
