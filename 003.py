def factorise(factorise):
    i = 2
    while i <= factorise:
        if factorise % i == 0:
            factorise = factorise / i;
            print(i)
        if factorise % i != 0:
            i += 1
factorise(16)
