import matplotlib.pyplot as plt

def sumofdigits(n):
    digits = list(str(n))
    sum = 0
    for i in range(len(digits)):
        sum += int(digits[i])
    return sum

y = []

for i in range(1000):
    y.append(sumofdigits(2**i))

plt.plot(y)
plt.ylabel("Sum of Digits of 2^x")
plt.xlabel("x")
plt.show()
