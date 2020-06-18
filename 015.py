def nCr(n, r):
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

print(nCr(40,20))




#n! / r! (n-r)!
