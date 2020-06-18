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

limit = 28123
abundant = []

for i in range(1,limit + 1):
    if sumproperfactors(i) > i:
        abundant.append(i)

#print(abundant)

for i in range(limit - 2000,limit + 1):
    #print(i)
    k = 0
    bool = True
    while bool and k < len(abundant) and abundant[k] <= i:
        #print(i , '\t', k)
        j = 0
        while bool and j < len(abundant) and abundant[j] <= i:
            #print(i , '\t', k, '\t', j)
            #print(i , '\t', abundant[k], '\t', abundant[j], '\t', abundant[k] + abundant[j])
            if (abundant[k] + abundant[j]) == i:
                #print(i , '\t', abundant[k], '\t', abundant[j])
                bool = False
            j += 1
        k += 1
    if bool:
        print(i)
    else:
        print(":(")
