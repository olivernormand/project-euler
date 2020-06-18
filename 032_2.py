import numpy as np

def ispandigital(n1, n2):
    n1n2 = n1 * n2
    print(n1, n2, n1n2)
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

ispandigital(39,186)
