import math as m

def sumofdigits(n):
    digits = list(str(n))
    sum = 0
    for i in range(len(digits)):
        sum += int(digits[i])
    return sum

print(sumofdigits(m.factorial(100)))
