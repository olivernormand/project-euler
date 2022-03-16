import numpy as np

def concat_product(x, y_array):
    x = x * y_array
    x = x.astype(str)

    return int(''.join(x))

def all_the_digits(x):
    x = str(x)
    for i in range(1,10):
        if str(i) not in x:
            return False
    return True

n_array = 2
n = 1
max = 0
x = 0

while True:
    print('a', n, n_array, x)
    n_array += 1
    n = 1

    array = np.arange(1, n_array)

    if len(str(concat_product(n, array))) > 9:
        print('c', n, n_array, x)
        break

    while True:
        print('b', n, n_array, x)
        x = concat_product(n, array)

        length = len(str(x))

        if length > 9:
            break

        elif length < 9:
            n += 1
            continue

        elif all_the_digits(x) and x > max:
            max = x
            saveme = (n, n_array, x)
            print(n, array, x)

        n += 1

print(max, saveme)
