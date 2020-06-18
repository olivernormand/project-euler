# Longest Collatz Sequence

def next(n):
    if n % 2 == 0:
        return int(n/2)
    if n % 2 != 0:
        return (3 * n) + 1

def printsequence(n):
    while n != 1:
        print(n, end = '\t')
        n = next(n)
    print(1)

def printsequences(n):
    for i in range(1,n + 1):
        printsequence(i)

def generatesequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        n = next(n)

def printsequencelengths(n):
    lengths = generatelengths(n)
    for i in range(len(lengths)):
        print(i, '\t', lengths[i])

def generatelengths(n):
    lengths = []
    lengths.append(0)

    for i in range(1,n + 1):
        length = 0
        n = i

        while n != 1 and n >= i:
            length += 1
            n = next(n)

        if n == 1:
            lengths.append(length + 1)
        elif n < i:
            lengths.append(length + lengths[n])
    return lengths

lengths = generatelengths(1000000)
maxlength = max(lengths)
print(max(lengths))
print(lengths.index(maxlength))
