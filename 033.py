import numpy as np

for i in range(10,100):
    si1, si2 = str(i)[0], str(i)[1]
    for j in range(10,100):
        sj1, sj2 = str(j)[0], str(j)[1]

        carry_on = False

        if si1 == sj1:
            i_new = int(si2)
            j_new = int(sj2)
            match = int(si1)
            carry_on = True
        elif si1 == sj2:
            i_new = int(si2)
            j_new = int(sj1)
            match = int(si1)
            carry_on = True

        elif si2 == sj1:
            i_new = int(si1)
            j_new = int(sj2)
            match = int(si2)
            carry_on = True

        elif si2 == sj2:
            i_new = int(si1)
            j_new = int(sj1)
            match = int(si2)
            carry_on = True

        if carry_on:
            if match != 0:
                if i != j:
                    if i_new != 0 and j_new != 0:
                        if i / j < 1:
                            if i / j == i_new / j_new:
                                print(match)
                                print(i, j, i_new, j_new)
