import math
import numpy as np

def sumdigits1(n):
    s = 0
    while n >= 1:
        print(n)
        s += n % 10
        n = math.floor(n/10)
    return s

def sumdigits2(n):
    n = str(n)
    digits = []
    for digit in n:
        digits.append(n)

for i in range(1,10000):
    sumdigit1(i)
