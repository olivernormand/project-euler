import numpy as np

def generatediagonal(n):
    if n % 2 == 0:
        print("Error, dimensions must be odd")
        return None
    grid = np.zeros([n,n])
    centre = int((n-1)/2)

    imax = centre + 1
    imin = centre - 1
    jmax = centre + 1
    jmin = centre - 1
    i = centre
    j = centre

    direction = 0

    for k in range(1,n**2 + 1):
        direction = direction % 4
        grid[i,j] = k

        # Move the current square according to the current direction of travel
        # If this then puts us at the end of the square, update the direction of travel as well.
        if direction == 0:
            j += 1
            if j == jmax:
                jmax += 1
                direction += 1
        elif direction == 1:
            i += 1
            if i == imax:
                imax += 1
                direction += 1
        elif direction == 2:
            j += -1
            if j == jmin:
                jmin += -1
                direction += 1
        elif direction == 3:
            i += -1
            if i == imin:
                imin += -1
                direction += 1
        if direction > 4:
            print("Error, direction is incorrect")
            break

    return grid

def sumdiagonals(grid):
    if grid.ndim != 2:
        print("Error, the number of dimensions must equal 2")
        return None
    if grid.shape[0] != grid.shape[1]:
        print("Error, the array must be square")
        return None

    n = grid.shape[0]
    sum = -1

    for i in range(n):
        sum += grid[i,i] + grid[i, n - 1 - i]
    return sum

print(sumdiagonals(generatediagonal(5)))

# There are certainly more efficient ways to do this problem, but as ever - I choose Project Euler as an excuse
# to improve my programming, and when the problems become increasingly computationally difficult, I may well be
# forced to find a better method. It turns out that in this case an analytical formula exists
