def ispalendrome(n1):
    string = str(n1)
    stringlength = len(string)
    reversestr = string[stringlength::-1]
    if string == reversestr:
        return True
    elif string != reversestr:
        return False

limit = 10000
for i in range(1, limit+ 1):
    for k in range(i, limit + 1):
        if ispalendrome(i * k):
            print(i, '\t', k, '\t', i * k)
