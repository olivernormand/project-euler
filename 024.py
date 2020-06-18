from itertools import permutations

# Generates list containing all permutations of the string within
perms = [''.join(p) for p in permutations('0123456789')]

interest = []
for i in range(0, len(perms)):
    if perms[i][0] == '2':
        interest.append(int(perms[i]))
interest.sort()

print(interest[274240 - 1])

"""
# Generates ordered list of corresponding numbers
nums = []
for i in range(0, len(perms)):
    nums.append(int(perms[i]))
    nums.sort()
Sorting of the entire list takes too long. So know that millionth begin with 2, will sort those.
"""
