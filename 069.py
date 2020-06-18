limit = 100000
# List used to contain factors of numbers up to limit
factors = []

with open("primes.txt") as f:
    primes = f.read().splitlines()
primes = [int(i) for i in primes]

def primefactors(factorise):
    i = 0
    factors = [1]
    while primes[i] <= factorise:
        if factorise % primes[i] == 0:
            factorise = factorise / primes[i];
            if primes[i] != factors[-1]:
                factors.append(primes[i])
        else:
            i += 1
    factors.remove(1)
    return factors

def generatefactors(factors):
    for i in range(limit + 1):
        factors.append(set(primefactors(i)))

def phi(n):
    relprime = []
    for i in range(1,n):
        if len(factors[i] & factors[n]) == 0:
            relprime.append(i)
    return len(relprime)

generatefactors(factors)


maxnoverphin = 0

for i in range(2,limit):
    noverphin = i / phi(i)
    if noverphin > maxnoverphin:
        print(i, noverphin)
        maxnoverphin = noverphin
print(maxnoverphin)
