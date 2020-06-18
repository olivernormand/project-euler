"""
    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
import time

t0 = time.time()

numlist = []
for i in range(1,1000000):
    numlist.append(str(i))
separator = ''
digits = separator.join(numlist)

def nthdigit(digits, n):
    return digits[n-1]

criticaldigits = []
criticaldigits.append(nthdigit(digits, 1))
criticaldigits.append(nthdigit(digits, 10))
criticaldigits.append(nthdigit(digits, 100))
criticaldigits.append(nthdigit(digits, 1000))
criticaldigits.append(nthdigit(digits, 10000))
criticaldigits.append(nthdigit(digits, 100000))
criticaldigits.append(nthdigit(digits, 1000000))

print(criticaldigits)
product = 1
for digit in criticaldigits:
    product = product * int(digit)
print(product)
tf = time.time()

print(tf-t0)
