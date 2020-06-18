# Largest Product in a Grid
length = 4

# Imports the data into matrix form
with open("011.txt") as f:
    entries = f.read().splitlines()

temp = [0] * len(entries)
matrix = [ [] for i in range(len(entries)) ]

for i in range(len(entries)):
    temp[i] = entries[i].split()
    for k in range(len(temp[i])):
        matrix[i].append(int(temp[i][k]))

maxproduct = 0

# Vertical, all the columns, not all the rows
for i in range(len(matrix) - length + 1): # row
    for k in range(len(matrix[1])): # column
        product = 1
        for j in range(0, length):
            product = product * matrix[i + j][k]
            if product > maxproduct:
                maxproduct = product


# Horizontal, all the rows, not all the columns
for i in range(len(matrix)): # row
    for k in range(len(matrix[1]) - length + 1): # column
        product = 1
        for j in range(0, length):
            product = product * matrix[i][k + j]
            if product > maxproduct:
                maxproduct = product

# Diagonal 1, rows increasing, columns increasing
for i in range(len(matrix) - length + 1): # row
    for k in range(len(matrix[1]) - length + 1): # column
        product = 1
        for j in range(0, length):
            product = product * matrix[i + j][k + j]
            if product > maxproduct:
                maxproduct = product

# Diagonal 2, rows increasing, columns decreasing
for i in range(len(matrix) - length + 1): # row
    for k in range(length - 1 , len(matrix[1])): # column
        product = 1
        for j in range(0, length):
            product = product * matrix[i + j][k - j]
            if product > maxproduct:
                maxproduct = product

print(maxproduct)
