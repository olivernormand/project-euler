def distinctprimeFactors(factorise): # Returns distinct factors as a list
    i = 2
    factors = [1]
    while i <= factorise:
        if factorise % i == 0:
            factorise = factorise / i;
            if factors[-1] % i == 0:
                factors[-1] = factors[-1] * i
            elif factors[-1] != i:
                factors.append(i)
        if factorise % i != 0:
            i += 1
    del factors[0]
    return factors

lower = distinctprimeFactors(0)
middle = distinctprimeFactors(1)
upper = distinctprimeFactors(2)
for i in range(3,80000):
    lowest = lower
    lower = middle
    middle = upper
    upper = distinctprimeFactors(i)
    if len(lowest) == 4 & len(lower) == 4 & len(middle) == 4 & len(upper) == 4:
        print(i - 3)
