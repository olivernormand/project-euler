import math as m

def trianglenumber(n):
    sum = int(n * (n+1) / 2)
    return sum

def returnfactorslist(factorise):
    i = 1
    factors = []
    limit = m.sqrt(factorise)

    while i <= limit:
        if factorise % i == 0:
            factors.append(i)
            factors.append(int(factorise / i))
        i += 1
    factors.sort()
    return factors


i = 1
maxfactors = []
while len(maxfactors) <= 500:
    i = i + 1
    factors = returnfactorslist(trianglenumber(i))
    # print(i, '\t', trianglenumber(i), '\t', len(factors), '\t', factors)
    if len(factors) > len(maxfactors):
        maxfactors = factors
print(i, '\t', trianglenumber(i), '\t', len(factors), '\t', factors)
