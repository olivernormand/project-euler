import time

t0 = time.time()

limit = 50000000
primes = list(range(0, limit + 1))

nprime = 1
i = 2

while i < limit:
    if primes[i] != 0:
        for k in range(2, int(limit / i) + 1):
            primes[k * i] = 0
        print(primes[i])
        nprime += 1
        i += 1
    if primes[i] == 0:
        i +=1

tf = time.time()

print(tf-t0)
