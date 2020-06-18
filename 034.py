# Finding the limit, this will occur when n * 9! < 9999.. n times
# It turns out this happens with 7 * 9! < 9999999
def definingproblem():
    import math as m
    for i in range(10):
        print(i, m.factorial(9) * i)

# Now onto the real part
import numpy as np
import math as m

n = np.arange(10)
nfactorial = [m.factorial(i) for i in n]

def sumfactorialdigits(N):
    return  np.sum([nfactorial[int(i)] for i in str(N)])

for i in range(9999999):
    if i == sumfactorialdigits(i):
        print(i)
