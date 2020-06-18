import math as math

def printpythag(limit):
    for a in range(1, limit + 1):
        for b in range(a+1, limit + 1):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer():
                print(a, '\t', b, '\t', int(c))

def printpythagsum(limit1, limit2):
    for a in range(1, limit1 + 1):
        for b in range(a+1, limit1 + 1):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer() and a + b + c == limit2:
                print(a, '\t', b, '\t', int(c))

printpythagsum(1000, 1000)
