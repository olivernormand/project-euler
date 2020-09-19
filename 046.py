"""
    Goldbach's other conjecture.

    Find smallest odd composite number that cannot be written as the sum of a prime and twice a square

    Slow method is to search, for every number, for every prime, for every 2x square.
"""

import numpy as np
import time

def primes(limit):
    limit += 1
    primes = np.arange(0, limit + 1)
    prime_list = []
    nprime = 1
    i = 2
    while i < limit:
        if primes[i] != 0:
            for k in range(2, limit // i + 1):
                primes[k * i] = 0
            prime_list.append(primes[i])
            nprime += 1
        i += 1
    return np.array(prime_list)

def twice_squares(limit):
    max_base = int(np.sqrt(limit / 2))
    return 2 * (np.arange(max_base) + 1) ** 2

def crop_max(limit, array):
    index = np.argmax(array > limit + 1) - 1
    return array[:index]

def odd_composite(limit):
    # can be sped up by passing primes since already calculated to limit
    odd = np.arange((limit + 1) // 2) * 2 + 1
    primes_array = primes(limit)
    odd_composite = np.setdiff1d(odd, primes_array)
    return odd_composite




limit = 40000
odd_composite_limit = odd_composite(limit)
primes_limit = primes(limit)
twice_squares_limit = twice_squares(limit)

sum_limit = np.expand_dims(primes_limit, -1) + np.expand_dims(twice_squares_limit, 0)

for i in odd_composite_limit:
    if not np.any(sum_limit == i):
        print(i)

# Solved, answer = 5777
