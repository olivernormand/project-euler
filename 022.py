import string
with open("022.txt") as f:
    data = f.read().split('\",\"')

# Clean data, removing " and \n from entries
data[0] = data[0].strip("\"")
data[-1] = data[-1].strip()
data[-1] = data[-1].strip("\"")

# Sorts data
data.sort()

# Generates a dictionary, which enables lookup of the value of an entry
values = dict()
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1

def namescore(name, position):
    letterscore = 0
    for letter in name:
        letterscore += values[letter]
    return letterscore * position

totalscore = 0

for i in range(len(data)):
    totalscore += namescore(data[i], i + 1)

print(totalscore)
