import numpy as np



def write_it_out(n):

    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['zeros', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    hundred = int(n / 100)
    ten = int((n - 100 * hundred) / 10)
    one = int((n - 100 * hundred - 10 * ten))

    d = ""

    if hundred != 0:
        d = d + ones[hundred] + 'hundred'
        if ten != 0 or one != 0:
            d = d + 'and'

    if ten == 0 and one == 0:
        pass
    elif ten < 2:
        d = d + ones[ten * 10 + one]
    else:
        d = d + tens[ten]
        if one != 0:
            d = d + ones[one]

    if n == 1000:
        d = 'onethousand'

    return d

def length(n):
    return len(write_it_out(n))

count = 0
for i in range(1, 1001):
    count += length(i)

print(count)
