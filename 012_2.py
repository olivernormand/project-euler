
def returnfactors(factorise): # Returns prime factors
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
    i = 1
    factors = []
    while i <= factorise:
        if factorise % i == 0:
            factors.append(i)
            i += 1
        if factorise % i != 0:
            i += 1
    return factors
    pass

def returntrianglefactors(n): # Implicitly reduces the number of factors, since factors each can multiply
    factors1 = returnfactorslist(n)
    factors2 = returnfactorslist(n + 1)
    factors = factors1 + factors2
    factors.remove(2)
    finalfactors = []
    for num in factors:
        if num not in finalfactors:
            finalfactors.append(num)
    finalfactors.sort()
    return finalfactors

i = 2
maxfactors = []
while len(maxfactors) < 200:
    i = i + 1
    factors = returntrianglefactors(i)
    # print(i, '\t', trianglenumber(i), '\t', len(factors))
    # print(trianglenumber(i))
    if len(factors) > len(maxfactors):
        maxfactors = factors
print(i, '\t', trianglenumber(i))
