import string

with open("042.txt") as f:
    data = f.read().split('\",\"')

# Clean data, removing " and \n from entries
data[0] = data[0].strip("\"")
data[-1] = data[-1].strip()
data[-1] = data[-1].strip("\"")

values = dict()
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1

def wordvalue(word):
    wordscore = 0
    for letter in word:
        wordscore += values[letter]
    return wordscore

def trianglenumber(n):
    number = int(n * (n+1) / 2)
    return number

# determine maximum word value, used to restrict list of triangle numbers - maxscore is found to equal 192
def maxscore(data):
    mscore = 0
    for word in data:
        if wordvalue(word) > mscore:
            mscore = wordvalue(word)
            mword = word
    return mscore

trianglenumbers = []
for i in range(21):
    trianglenumbers.append(trianglenumber(i))

wordcount = 0
for word in data:
    if wordvalue(word) in trianglenumbers:
        wordcount += 1
        print(word, wordvalue(word))
print(wordcount)
