import time

t0 = time.time()

def reverse(n1):
    string = str(n1)
    stringlength = len(string)
    return int(string[stringlength::-1])

def composedofodddigits(n1):
    n1 = str(n1)
    for digit in n1:
        if int(digit) in {2,4,6,8,0}:
            return False
    return True

def lastndigits(n1):
    return int(str(n1)[-2:])

def sumndigits(n1, n):
    lastndigits = int(str(n1)[-n:])
    return int(str(lastndigits + reverse(lastndigits))[-n:])



count = 0

for i in range(1, 1000000001):
    stringi = str(i)
    if stringi[-1] == '0':
        continue

    """
    if i % 10 + int(stringi[0]) in {8,6,4,2,0}:
        continue

    for j in range(1, len(stringi)):
        if not composedofodddigits(sumndigits(i, j)):
            continue
    """

    if composedofodddigits(i + reverse(i)):
            # print(i, i + reverse(i))
            count += 1

tf = time.time()
print(count)
print(tf-t0)
