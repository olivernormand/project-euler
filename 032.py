def ispandigital(n1, n2):
    n1n2 = n1 * n2
    if len(str(n1)) + len(str(n2)) + len(str(n1n2)) == 9:
        set1 = set(digits(n1))
        set2 = set(digits(n2))
        set12 = set(digits(n1n2))
        union = set1 | set2 | set12
        if 0 in union:
            union.remove(0)
        if len(union) == 9:
            return True
    return False

def digits(n1):
    digits = []
    for digit in str(n1):
        digits.append(int(digit))
    return digits

products = []

for i in range(10000):
    for k in range(i, 10000):
        if ispandigital(i,k):
            print(i, k, i * k)
            products.append(i * k)



"""
# Single Digits first number
for i in range(10):
    for k in range(10000):
        if ispandigital(i,k):
            products.append(i * k)

for i in range(9, 100):
    for k in range(1000):
        if ispandigital(i,k):
            products.append(i * k)
"""
products = list(set(products))

sum = 0

for product in products:
    sum += product

print(sum)
