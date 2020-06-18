with open("081.txt") as f:
    entries = f.read().splitlines()

temp = [0] * len(entries)
matrix = [ [] for i in range(len(entries)) ]

for i in range(len(entries)):
    temp[i] = entries[i].split(',')
    for k in range(len(temp[i])):
        matrix[i].append(int(temp[i][k]))


def min(n1, n2):
    if n1 <= n2:
        return n1
    else:
        return n2

def printmatrix(matrix):
    for row in matrix:
        for k in row:
            print(k, end = '\t')
        print()



for i in range(len(matrix) - 1, -1, -1):
    for k in range(len(matrix[i]) - 1, -1, -1):
        if i == len(matrix) - 1:
            if k != len(matrix[i]) - 1:
                matrix[i][k] += matrix[i][k+1]
        elif k == len(matrix[i]) - 1:
            matrix[i][k] += matrix[i+1][k]
        else:
            matrix[i][k] += min(matrix[i+1][k], matrix[i][k+1])

print(matrix[0][0])
