import numpy as np

#values = np.array([1,2,5,10,20,50,100,200])
Values = np.array([1,2])
Target = 2
Formation = [ np.array([1]) ]

#Formation = [ [ [1, 0] ], [ [2, 0], [0, 1] ] ]

def perms(target, values, formation):
    # target contains the new value to be appended to values
    # formation details how


    print(target, values, formation)
    # Should only pass the values that are

    # Determine how to make target from values.



    for entry in formation:
        for entri in entry:
            entri.append(0)





    print(target, values, formation)
    pass

perms(Target, Values[:2], Formation)
