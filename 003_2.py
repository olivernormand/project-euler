factorise = 1234
i = 2
y = []

while i <= factorise:
    if factorise % i == 0:
        factorise = factorise / i;
        y.append(i)
    if factorise % i != 0:
        i += 1




plt.plot(y)
plt.ylabel("Sum of Digits of 2^x")
plt.xlabel("x")
plt.show()
