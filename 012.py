
def returnfactors(factorise):
    i = 2
    factors = []
    while i <= factorise:
        if factorise % i == 0:
            factorise = factorise / i;
            if i not in factors:
                factors.append(i)
        if factorise % i != 0:
            i += 1
    return factors

def trianglenumber(n):
    sum = int(n * (n+1) / 2)
    return sum

def returnfactorslist(factorise):
    i = 2
    factors = []
    while i <= factorise:
        if factorise % i == 0:
            factorise = factorise / i;
            factors.append(i)
        if factorise % i != 0:
            i += 1
    return factors
    pass

def returntrianglefactors(n):
    factors1 = returnfactorslist(n)
    factors2 = returnfactorslist(n + 1)
    factors = factors1 + factors2
    factors.remove(2)
    factors.append(1)
    finalfactors = []
    for num in factors:
        if num not in finalfactors:
            finalfactors.append(num)
    finalfactors.sort()
    return finalfactors

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
    pass


i = 300000
maxfactors = []
while len(maxfactors) < 100:
    i = i + 1
    factors = returntrianglefactors(i)
    print(i, '\t', trianglenumber(i), '\t', factors)
    # print(trianglenumber(i))
    if len(factors) > len(maxfactors):
        maxfactors = factors
