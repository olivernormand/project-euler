import math as m
plimit = 1000

pnumber = [0 for i in range(plimit+1)]

for a in range(1, plimit + 1):
    for b in range(a, plimit + 1):
        c = m.sqrt(a**2 + b**2)
        p = a + b + c
        if p > plimit:
            # prevents further incrementation of b if already above the perimeter limit
            break
        if c.is_integer() == True:
            c = int(c)
            p = int(p)
            pnumber[p] += 1
            print("a", '\t', a,'\t', "b", '\t', b,'\t', "c", '\t', c,'\t', 'p', '\t', p)

maxnumber = 0
maxp = 0
for i in range(0, plimit + 1):
    if pnumber[i] != 0:
        print(i, '\t', pnumber[i])
        if pnumber[i] > maxnumber:
            maxnumber = pnumber[i]
            maxp = i
print(maxp, '\t', maxnumber)
