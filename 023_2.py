import math

def sumproperfactors(n1):
    # Returns the sum of all the proper factors of the argument
    sum = - n1
    if math.sqrt(n1).is_integer() == True:
        sum = sum - int(math.sqrt(n1))
    sqrt = int(math.sqrt(n1))
    for i in range(1, sqrt + 1):
        if n1 % i == 0:
            sum += i + int(n1 / i)
    return sum

def sumlist(l):
    sum = 0
    for item in l:
        sum += item
    return sum

limit = 28123
abundant = []
temp = []

# Generates a list of all the abundant numbers less than and including the limit
for i in range(1,limit + 1):
    if sumproperfactors(i) > i:
        abundant.append(int(i))

# Generates a (not necessarily sorted) list of all the numbers that can be formed from pairs of abundant numbers
for i in range(0, len(abundant)):
    for k in range(i, len(abundant)):
        temp.append(abundant[i] + abundant [k])
abundantsums = set(temp)

# Generates a set of all numbers below and including limit
allnumbers = set(range(0, limit + 1))

# Takes the difference of these two sets, giving an ordered list of all numbers that cannot be formed by the addition of two abundant numbers
nonabundantsums = sorted(list(allnumbers - abundantsums))

print(sumlist(nonabundantsums))
