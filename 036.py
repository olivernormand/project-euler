import numpy as np

def dec_to_bin(x):
    return int(bin(x)[2:])

def is_palendrome(n):
    string = str(n)
    reversestr = string[::-1]
    if string == reversestr:
        return True
    elif string != reversestr:
        return False

count = 0

for n in range(1000000):
    n_bin = dec_to_bin(n)
    if is_palendrome(n) and is_palendrome(n_bin):
        print(n, n_bin)
        count += n
    
print("The count is {}".format(count))