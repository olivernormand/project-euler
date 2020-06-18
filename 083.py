import numpy as np

with open("stuff.txt") as f:
    entries = f.read().splitlines()

temp = [0] * len(entries)
matrix = [ [] for i in range(len(entries)) ]

for i in range(len(entries)):
    temp[i] = entries[i].split(',')
    for k in range(len(temp[i])):
        matrix[i].append(int(temp[i][k]))
matrix = np.array(matrix)

def printmatrix(matrix):
    for row in matrix:
        for k in row:
            print(k, end = '\t')
        print()
def min(indeces):
    # Accepts a list of indexes, and returns the minimum value in the solmatrix
    values = []
    for index in indeces:
        values.append(solmatrix[index])
    values = np.array(values)
    return np.amin(values)

def unassignedneighbours(i,j):
    # Given an entry in the solmatrix, will return a list of indexes as tuples for
    # the values in the solmatrix bordering it that haven't already been asigned.
    neighbours = []
    # above
    if (i - 1 != -1) and solmatrix[i-1,j] == 0:
            neighbours.append((i-1,j))
    # below
    if (i + 1 != matrix.shape[0]) and solmatrix[i+1,j] == 0:
            neighbours.append((i+1,j))
    # right
    if (j + 1 != matrix.shape[1]) and solmatrix[i,j+1] == 0:
            neighbours.append((i,j+1))
    # left
    if (j - 1 != -1) and solmatrix[i, j-1] == 0:
            neighbours.append((i,j-1))
    return neighbours
def assignedneighbours(i,j):
    neighbours = []
    # above
    if (i - 1 != -1) and solmatrix[i-1,j] != 0:
            neighbours.append((i-1,j))
    # below
    if (i + 1 != matrix.shape[0]) and solmatrix[i+1,j] != 0:
            neighbours.append((i+1,j))
    # right
    if (j + 1 != matrix.shape[1]) and solmatrix[i,j+1] != 0:
            neighbours.append((i,j+1))
    # left
    if (j - 1 != -1) and solmatrix[i, j-1] != 0:
            neighbours.append((i,j-1))
    return neighbours
def neighbours(i,j):
    neighbours = []
    # above
    if (i - 1 != -1):
            neighbours.append((i-1,j))
    # below
    if (i + 1 != matrix.shape[0]):
            neighbours.append((i+1,j))
    # right
    if (j + 1 != matrix.shape[1]):
            neighbours.append((i,j+1))
    # left
    if (j - 1 != -1):
            neighbours.append((i,j-1))
    return neighbours
def activeresize(value):
    currentmax = len(active) - 1
    addition = value - currentmax
    adding = [[] for i in range(int(addition))]
    active.extend(adding)
def activeadd(i, j):
    value = int(solmatrix[i,j])
    if value > len(active):
        activeresize(value)
    active[value].append((i,j))
def activerefresh():
    # Resizes the list so that it ends with the minimum active value.
    while len(active[-1]) == 0:
        active.pop()
def smallestactive():
    i = 0
    while len(active[i]) == 0:
        i += 1
    return i

def step():
    sa = smallestactive()
    for index in active[sa]:
        active[sa].remove(index)
        for un in unassignedneighbours(index[0],index[1]):
            solmatrix[un] = matrix[un] + min(assignedneighbours(un[0],un[1]))
            activeadd(un[0],un[1])
    activerefresh()




solmatrix = np.zeros(matrix.shape)
active = [ [] ]

solmatrix[matrix.shape[0] - 1, matrix.shape[1] -1] = matrix[matrix.shape[0] - 1, matrix.shape[1] -1]
activeadd(matrix.shape[0] - 1, matrix.shape[1] -1)

while solmatrix[0,0] == 0:
    step()
    print(solmatrix)
