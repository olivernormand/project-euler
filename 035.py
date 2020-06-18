import numpy as np

def primelist(limit):
    primes = np.arange(limit + 1)
    nprime = 1
    i = 2
    while i < limit:
        if primes[i] != 0:
            for k in range(2, int(limit / i) + 1):
                primes[k * i] = 0
            nprime += 1
            i += 1
        if primes[i] == 0:
            i +=1
    return np.array(list(set(primes)))

def cyclic(N): # Returns the cyclic permutations of the number in a list
    digits = [int(i) for i in str(N)]
    n = len(digits)
    return [[digits[i - j] for i in range(n)] for j in range(n)]

def primedigitlist(limit):
    return [[int(i) for i in str(j)] for j in primelist(limit)]



limit = 1000000
sum = -2

primedigits = primedigitlist(limit)

for i in primelist(limit):
    value = True
    for j in cyclic(i):
        if j not in primedigits:
            value = False
    if value:
        print(i)
        sum += 1

print("The total number of circular primes below " + str(limit) + " is " + str(sum))
