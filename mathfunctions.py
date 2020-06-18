def primeFactors(factorise): # Returns prime factors as a list
    i = 2
    factors = [1]
    while i <= factorise:
        if factorise % i == 0:
            factorise = factorise / i;
            if factors[-1] != i:
                factors.append(i)
        if factorise % i != 0:
            i += 1
    del factors[0]
    return factors

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

def nCr(n, r): # nCr but works for large numbers
    nC = 1
    rC = 1
    n_rC = 1
    factorial = 1

    while nC <= n:
        factorial = factorial * nC
        nC += 1
        while (rC <= r) and (factorial % rC == 0):
            factorial = factorial / rC
            rC += 1
        while (n_rC <= n - r) and (factorial % n_rC == 0):
            factorial = factorial / n_rC
            n_rC += 1
    return int(factorial)

def isPalendrome(n1): # Returns True if integer input is palendrome, Returns False otherwise
    string = str(n1)
    stringlength = len(string)
    reversestr = string[stringlength::-1]
    if string == reversestr:
        return True
    elif string != reversestr:
        return False

def sumofDigits(n):
    digits = list(str(n))
    sum = 0
    for i in range(len(digits)):
        sum += int(digits[i])
    return sum

def permute(string):
    from itertools import permutations
    return [''.join(p) for p in permutations(string)]

def cyclic(N): # Returns the cyclic permutations of the number in a list
    digits = [int(i) for i in str(N)]
    n = len(digits)
    return [[digits[i - j] for i in range(n)] for j in range(n)]
