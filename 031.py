import numpy as np

values = np.array([200,100,50,20,10,5,2,1])
number = np.zeros([len(values)])
target = 2

# Sorts the values into descending order.
values = np.sort(values)[::-1]
nperms = 0


def total(number, values):
    return np.dot(number, values)

def perms(number, values, target):
    if target == 0:
        return None

    if total(number, values) < target:
        number[0] += 1
        perms(number, values, target)
    if total(number, values) == target:
        nperms += 1
        print(number, '\t', nperms)
        perms(number[1::1], values[1::1], target)
        number[0] += -1
        perms(number, values, target - values[0])

    elif total(number, values) > target:
        number[0] += -1
        number[1] += 1
        perms(number, values, target)

perms(number, values, target)


# Probably need to better understand both recursive functions and also what I'm doing here. 
