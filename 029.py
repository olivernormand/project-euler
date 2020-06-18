numbers = []
alimit = 100
blimit = 100

for a in range(2, alimit + 1):
    for b in range(2, blimit + 1):
        numbers.append(a**b)
numbers = list(set(numbers))
print(len(numbers))
