"""
Truncatable primes

The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""
import time
t0 = time.time()

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

primelist = primes(1000000)
print("primelist calc complete")
truncatableprimes = []

def truncations(prime):
    emptylist = []
    prime = str(prime)
    for i in range(1, len(prime)):
        emptylist.append(int(prime[i:]))
        emptylist.append(int(prime[:i]))
    return emptylist

"""
def istruncatableprime(primelist, prime):
    return all(truncation in primelist for truncation in truncations(prime))
# Gonna try a different method, too inefficient
"""
def istruncatableprime(primelist, prime):
    truncationz = truncations(prime)
    truncationz.sort() # figure this is easy for small lists and will lead to searching small values first
    for truncation in truncationz:
        if truncation not in primelist:
            return False
    return True
    # only marginally faster it turns out.



for prime in primelist:
    if istruncatableprime(primelist, prime):
        truncatableprimes.append(prime)
        if len(truncatableprimes) == 15:
            break

for i in [2,3,5,7]:
    truncatableprimes.remove(i)


print(truncatableprimes)
tf = time.time()
print(tf-t0)


"""
Reliably, there are more efficient ways to solve this which do not take 3 mins
Truncated primes must build on previous ones. 
"""
