# Large Sum
path = "013_2.txt"
numbers_file = open(path, 'r')
numbers = numbers_file.read().splitlines()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(numbers)

numbers_file.close()
