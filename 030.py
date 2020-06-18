# Playing around with the maths reveals 299999 --> 295277, so we will use this as our upper limit

def sumpowerdigits(number, power):
    sum = 0
    for digit in str(number):
        sum += int(digit) ** power
    return sum

overallsum = 0

for i in range(2,299999):
    if sumpowerdigits(i,5) == i:
        overallsum += i
        print(i)

print(overallsum)
