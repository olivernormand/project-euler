"""
    Prime power triples

    The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
    In fact, there are exactly four numbers below fifty that can be expressed in such a way:

        28 = 22 + 23 + 24
        33 = 32 + 23 + 24
        49 = 52 + 23 + 24
        47 = 22 + 33 + 24

    How many numbers below fifty million can be expressed as the
    sum of a prime square, prime cube, and prime fourth power?

    Plan:
    Generate the list of prime numbers - method for this exists.
    50,000,000**0.5 = 7071 --> go to 7072 with squares
    50,000,000**0.33333 = 368 --> go to 370 with cubes
    50,000,000**0.25 = 84 --> go to 85 with fourth power.

    7072*370*85 = 222 million numbers which need to be checked.

    Most efficient to add numbers to a numpy array which is zeros, but gets converted to
    a 1 if we find a combination which can generate it.
"""
import math
import numpy as np
triplelimit = 50000000

limit2 = math.floor(triplelimit ** 0.5)
limit3 = math.floor(triplelimit ** (1/3))
limit4 = math.floor(triplelimit ** 0.25)

def primes(limit):
    limit += 1
    primes = list(range(0, limit + 1))
    emptylist = []
    nprime = 1
    i = 2
    while i < limit:
        if primes[i] != 0:
            for k in range(2, int(limit / i) + 1):
                primes[k * i] = 0
            emptylist.append(primes[i])
            nprime += 1
            i += 1
        if primes[i] == 0:
            i +=1
    return emptylist

primes2 = primes(limit2)
primes3 = primes(limit3)
primes4 = primes(limit4)

# Create array triples, will set triples[number] = 1 if we find a combination which can be expressed
# to satisfy the required relation.
triples = np.zeros(triplelimit + 1)

for prime2 in primes2:
    for prime3 in primes3:
        for prime4 in primes4:
            sum = prime2**2 + prime3**3 + prime4**4
            if sum < triplelimit:
                triples[sum] = 1

"""for i in range(len(triples) - 1):
    if triples[i] != 0:
        print(i)"""
print(np.sum(triples))
