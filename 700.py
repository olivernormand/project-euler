import math
import numpy as np
n1 = 2134
n2 = 123

eulercoin = [n1]
remainder = n1 % n2

while eulercoin[-1] != 1:
    multiple = math.floor(n2 / remainder) + 1
    remainder = (multiple * remainder) % n2
    eulercoin.append(remainder)

print(eulercoin)
eulercoin = np.array(eulercoin)
print(np.sum(eulercoin))
