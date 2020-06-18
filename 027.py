# Imports primes less than 1 million, and stores an integers in list
with open("millionprimes.txt") as f:
    numbers = f.read().splitlines()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

def returnprimefactors(factorise):
    factors = []
    i = 0
    while numbers[i] <= factorise:
        if factorise % numbers[i] == 0:
            factorise = factorise / numbers[i];
            if numbers[i] not in factors:
                factors.append(numbers[i])
        if factorise % numbers[i] != 0:
            i += 1
    return factors

def isprime(test):
    if test in numbers:
        return True
    else:
        return False

def f(n , a, b):
    answer = n**2 + (a * n) + b
    return answer



maxlength = 0
bool = True

for a in range(-1001,1001):
    i = 0
    print("a = ", a)
    while numbers[i] < 1001:
        n = 0
        length = -1
        bool = True
        b = numbers[i]
        # print("b = ", b)
        while bool == True:
            bool = isprime(f(n, a, b))
            # print("n = ", n)
            n += 1
            length += 1
        if length > maxlength:
            maxlength = length
            print("x^2 + ", a, "x", " + ", b, '\t', "maxlength = ", maxlength)
        i += 1
print(maxlength)
