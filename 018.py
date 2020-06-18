with open("018.txt") as f:
    entries = f.read().splitlines()

temp = [0] * len(entries)
matrix = empty_lists = [ [] for i in range(len(entries)) ]

for i in range(len(entries)):
    temp[i] = entries[i].split()
    for k in range(len(temp[i])):
        matrix[i].append(int(temp[i][k]))

def max(n1, n2):
    if n1 > n2:
        return n1
    if n2 > n1:
        return n2
    if n1 == n2:
        return n1


for row in matrix:
    for k in row:
        print(k, end = '\t')
    print()

i = len(matrix) - 2

while i >= 0:
    for k in range(len(matrix[i])):
        matrix[i][k] += max(matrix[i+1][k], matrix[i+1][k+1])
    i = i - 1

for row in matrix:
    for k in row:
        print(k, end = '\t')
    print()
