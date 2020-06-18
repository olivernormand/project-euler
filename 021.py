import math

def sumproperfactors(n1):
    sum = - n1
    if math.sqrt(n1).is_integer() == True:
        sum = sum - int(math.sqrt(n1))
    sqrt = int(math.sqrt(n1))
    for i in range(1, sqrt + 1):
        if n1 % i == 0:
            sum += i + int(n1 / i)
    return sum

total = 0
for i in range(2,10000):
    b = sumproperfactors(i)
    iprime = sumproperfactors(b)
    if iprime == i and i != b :
        print(i , '\t', b)
        total += i + b

total = total / 2
print(int(total))
