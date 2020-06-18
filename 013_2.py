with open("013.txt") as f:
    numbers = f.read().splitlines()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

sum = 0
for i in numbers:
    sum += i

print(sum)
