import numpy as np

def concat_product(x, y_array):
    x = x * y_array
    x = x.astype(str)

    return int(''.join(x))

print(concat_product(9327, np.arange(1, 3)))
