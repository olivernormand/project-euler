"""
Counting summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

At the heart of this is a recursive function which can successively count up the number of
recursions for a given number. For example to write 5 as the sum of different numbers...

We can write it as 4 + number of different ways we can write 5-4
Also 3 + number of different ways we can write 5-3

"""
import numpy as np
import time

def summations(N):
    N += 1
    # Generate the list and instantiate the first entry
    summations = [[] for i in range(N)]
    summations[2] = [[1,1]]
    for i in range(2,N): # iterate up and generate the summations, starting at the bottom
        #print("i... ", i)
        for k in range(1,i): # for every lower number
            #print(k)
            #print(len(summations[k]))
            if i-k != 1 and i-k >= k:
                summations[i].append([i-k, k])
            for summation in summations[k]: # for every way of making the lower number
                #print("activated")
                if np.max(summation) <= i-k:
                    summations[i].append([i-k] + summation)
    return summations

def summations2(N): # marginally faster
    N += 1 # make list correct size
    # Generate the list and instantiate the first entry
    summations = [[] for i in range(N)]

    for i in range(1,N): # iterate up and generate summations, starting at the bottom
        #print("i.. ", i)
        summations[i].append([i])
        for k in range(1,i): # for every lower number
            for summation in summations[k]:
                #print("activated")
                if np.max(summation) <= i-k:
                    summations[i].append([i-k] + summation)

    summations.pop(0)
    for i in range(len(summations)):
        summations[i].pop(0)


    return summations
"""
    We can see that this doesn't work, the time taken increases exponentially :( so it is fairly unreasonable to expect
    this to be solvable in my lifetime which is a shame.

    Instead, if we forget storing the summations as individual arrays, but instead store a list of how many have a certain number as its maximum,
    then it will be much faster - how much??
"""

def summations3(N):
    N += 1 # make the list the correct size
    summationslist = [[] for i in range(N)] # list of arrays with number of sequences with max value

    for i in range(1, N): # for each summation

        # array of max values which we will append to list
        # index corresponds to the max value
        summations = np.zeros(i+1)
        summations[i] = 1 # since we can always form a number with itself alone


        # for every lower sequence
        # set the number of sequences with max value k to equal the total number of ways
        # we can form i - k from the remainder
        for k in range(1,i):
            summations[i-k] = np.sum(summationslist[k][: i - k + 1])
        summationslist[i] = summations


    return summationslist


"""
for i in range(2,10):
    print("i.. ", i, len(summations2(i)[-1]), np.sum(summations3(i)[-1]) - 1)

t0 = time.time()
for i in range(2,25):
    print(i, np.sum(summations3(i)[-1]) -1)
print(time.time() - t0)
"""
t0 = time.time()
print(np.sum(summations3(100)[-1]) - 1)
print(time.time() - t0)
