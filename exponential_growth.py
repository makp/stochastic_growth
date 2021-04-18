import numpy as np


def grow_poisson(n0, ave, npaths, nsteps):
    arr = np.empty((npaths, nsteps+1))
    arr[:, 0] = n0
    for j in range(1, nsteps+1):
        arr[:, j] = np.random.poisson(arr[:, j-1]*ave, npaths)
    return arr
