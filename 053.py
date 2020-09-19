import numpy as np
from math import comb

"""
    MODE OF ATTACK

    We do not need to calculate every single combinatoric results. Although there aren't actually too many,
    they all take a really long time to calculate.

    Instead, for each n, find the first value of r for which nCr > 1mil. We then know that all the values from
    r to n-r inclusive will be greater than 1mil = n - 2r + 1
"""

count = 0
for n in range(1, 101):
    r = 0
    while r < n // 2 + 1:
        ans = comb(n, r)
        if ans >= 1000000:
            print(n, r, ans)
            count += n - 2 * r + 1
            break
        r += 1
print(count)
