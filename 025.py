i = 2
n1 = 1
n2 = 1
while len(str(n2)) < 1000:
    n0 = n1
    n1 = n2
    n2 = n0 + n1
    i += 1
    print(i, '\t', n2)
