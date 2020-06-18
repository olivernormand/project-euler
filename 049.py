"""
    Prime Permutations

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
    is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
    exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from itertools import permutations

with open("049.txt") as f:
    entries = f.read().splitlines()
fourdigitprimes = []
for entry in entries:
    fourdigitprimes.append(int(entry))

def perms(permute):
    # Generates list containing all permutations of the inputed number
    temp = [''.join(p) for p in permutations(str(permute))]
    perms = []
    for tem in temp:
        perms.append(int(tem))
    return perms

"""
    The term we increase (k) by must be a multiple of 3 if all three terms are to remain prime.
    This is since, if it isn't then we have two cases:
        1. Our prime n1 = 3n+1
            Then we have
            a. k = 3m + 1
                Hence n2 = 3(n+m) + 2
                n3 = 3(n + 2m) + 3
            Which is divisible by 3 and so not prime
            b. k = 3m + 2
                Hence n2 = 3(n+m) + 3
        2. Our prime is n1 = 3n + 2
            And a similar argument follows.

    So for every 4 digit prime, we should search to see if:
        - for every k such that 2k + n1 <= 9999
            k <= (9999 - n1)/2
        - whether n1, n1 + k, n1 + 2k are both perms of n1 and also prime.
"""

def maxk(prime):
    return int((9999-prime)/2)


for prime in fourdigitprimes:
    primeperms = perms(prime)
    k = 3
    while k <= maxk(prime):
        n2 = prime + k
        n3 = prime + 2*k
        if n2 in primeperms:
            if n3 in primeperms:
                if n2 in fourdigitprimes:
                    if n3 in fourdigitprimes:
                        print(prime, n2, n3, k)
        k += 3
